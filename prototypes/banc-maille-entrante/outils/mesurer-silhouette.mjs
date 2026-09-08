#!/usr/bin/env node
/**
 * MESURER — le sujet se DÉTACHE-T-IL du fond, et de combien ?
 *
 *     node outils/mesurer-silhouette.mjs [url-de-base]
 *
 * ════════════════════════════════════════════════════════════════════════════
 * ⚠️⚠️ POURQUOI CE BANC EXISTE. Le legacy a changé de skin de garde un jour
 * d'août ; la capture « paraissait » correcte parce qu'on savait où regarder.
 * Mesuré : 2,0/255 de luminance contre un mur à 8,4. Invisible. Un garde
 * invisible est une mort qu'on ne peut pas raconter.
 * ════════════════════════════════════════════════════════════════════════════
 *
 * ⭐ LA MESURE JUSTE ISOLE LE SUJET — méthode reprise telle quelle de
 * `sonder-gardes.mjs` : on rend DEUX fois la même image, avec et sans lui, et
 * on ne compare que les pixels qui ont changé. Ce sont les siens. La première
 * version de `sonder-arme.mjs` avait conclu que l'arme était « plus claire dans
 * le noir » en mesurant en réalité le FOND.
 *
 * ⚠️⚠️ ET LE BON INDICATEUR N'EST PAS L'ÉCART MOYEN. Un liseré n'éclaircit que
 * les BORDS : ses pixels clairs et ses pixels d'ombre s'annulent presque en
 * moyenne — 1,4 point mesuré alors que la silhouette saute aux yeux. On regarde
 * le p90 et la part de pixels nettement distincts : ce que l'œil fait vraiment,
 * chercher un contour, pas une moyenne.
 *
 * ⭐ CE QUE CE BANC AJOUTE AU LEGACY : il ne rend pas un verdict, il trace une
 * COURBE. Quaternius ne livre aucune peau de garde — le corps arrive nu et
 * l'uniforme est une couleur QU'ON CHOISIT. La question n'est donc plus « ce
 * fournisseur passe-t-il ? » mais « à partir de quel albédo un uniforme
 * devient-il invisible dans cette salle ? ». On balaie, et le seuil sort.
 */
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { createRequire } from 'node:module'

const ICI = path.dirname(new URL(import.meta.url).pathname)
const RACINE = path.resolve(ICI, '..')
const require = createRequire(
  '/home/fayssal/projetCadeau/apps/gifts/_templates/runner-poursuite/package.json')
const puppeteer = require('puppeteer-core')

const base = process.argv[2] ?? 'http://localhost:5199/salle-temoin.html'

/** Ce qu'on exige, et pourquoi — les seuils du legacy, inchangés. */
const SEUILS = {
  partNette: 0.25,   // part des pixels du sujet qui tranchent d'au moins 12/255
  p90: 30,           // le contour doit être franc là où il existe
  ecartNet: 12,
}

const attendre = (ms) => new Promise((r) => setTimeout(r, ms))

/** Luminance perceptuelle, la même formule des deux côtés. */
const lum = (r, g, b) => 0.2126 * r + 0.7152 * g + 0.0722 * b

/**
 * Compare deux rendus identiques à un sujet près.
 * ⚠️ Ne renvoie QUE ce qui se déduit des pixels changés — jamais une moyenne
 * d'image, qui décrirait le fond.
 */
function comparer(avec, sans) {
  const n = avec.length / 4
  const ecarts = []
  let somme = 0, sommeSujet = 0, sommeFond = 0
  for (let i = 0; i < n; i++) {
    const j = i * 4
    const a = lum(avec[j], avec[j + 1], avec[j + 2])
    const s = lum(sans[j], sans[j + 1], sans[j + 2])
    const d = Math.abs(a - s)
    if (d > 0.5) { ecarts.push(d); somme += d; sommeSujet += a; sommeFond += s }
  }
  if (!ecarts.length) return { pixels: 0 }
  ecarts.sort((x, y) => x - y)
  const p = (q) => ecarts[Math.min(ecarts.length - 1, Math.floor(ecarts.length * q))]
  return {
    pixels: ecarts.length,
    partDeLImage: +(ecarts.length / n).toFixed(4),
    ecartMoyen: +(somme / ecarts.length).toFixed(1),
    p50: +p(0.5).toFixed(1),
    p90: +p(0.9).toFixed(1),
    partNette: +(ecarts.filter((d) => d >= SEUILS.ecartNet).length / ecarts.length).toFixed(3),
    luminanceSujet: +(sommeSujet / ecarts.length).toFixed(1),
    luminanceFond: +(sommeFond / ecarts.length).toFixed(1),
  }
}

async function rendre(page, params) {
  const url = base + '?mesure=1&' + new URLSearchParams(params).toString()
  await page.goto(url, { waitUntil: 'load', timeout: 30000 })
  await page.waitForFunction('window.__banc && window.__banc.pret', { timeout: 30000 })
  const infos = await page.evaluate(() => window.__banc)
  if (infos.erreur) throw new Error(infos.erreur)
  await attendre(120)
  const png = await page.screenshot({ type: 'png' })
  return { infos, png }
}

/** Décode un PNG en RGBA sans dépendance : on passe par le canvas de la page. */
async function pixels(page, png) {
  return Buffer.from(await page.evaluate(async (b64) => {
    const img = new Image()
    img.src = 'data:image/png;base64,' + b64
    await img.decode()
    const c = document.createElement('canvas')
    c.width = img.width; c.height = img.height
    const x = c.getContext('2d')
    x.drawImage(img, 0, 0)
    return Array.from(x.getImageData(0, 0, c.width, c.height).data)
  }, png.toString('base64')))
}

async function main() {
  const profil = fs.mkdtempSync(path.join(os.tmpdir(), 'banc-'))
  const navigateur = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome',
    headless: 'new',
    defaultViewport: { width: 440, height: 764, deviceScaleFactor: 1 },
    args: ['--no-sandbox', `--user-data-dir=${profil}`, '--use-angle=vulkan',
      '--enable-features=Vulkan', '--ignore-gpu-blocklist'],
  })
  const releve = { url: base, le: new Date().toISOString(), seuils: SEUILS, mesures: [] }
  try {
    const page = (await navigateur.pages())[0]
    page.on('pageerror', (e) => console.error('  ✗ page :', e.message))

    /* ⚠️⚠️ LA CHAUFFE N'EST PAS UNE PRÉCAUTION, C'EST UNE CORRECTION. Au TOUT
       PREMIER chargement, Chrome sans écran perd le contexte WebGL
       (`CONTEXT_LOST_WEBGL`) et rend une image entièrement noire. La première
       navigation étant celle du FOND, la référence de toutes les comparaisons
       était noire — et le banc a alors mesuré la SALLE contre le vide en
       annonçant vingt succès. On brûle donc une navigation, puis on VÉRIFIE. */
    await rendre(page, { sujet: 'aucun' })

    /* ⚠️⚠️ UNE RÉFÉRENCE PAR RECUL. Le recul déplace la CAMÉRA : la salle
       elle-même change d'image. Comparé à une référence prise à 6 m, un garde
       à 9 m « change » 236 000 pixels — la salle entière — et le chiffre ne dit
       plus rien de lui. On garde donc une référence par distance, et le sujet
       reste la seule différence entre les deux rendus. */
    const fonds = new Map()
    /* ⚠️ La référence doit porter TOUT le décor du cas mesuré — le recul, qui
       déplace la caméra, ET le socle, qui est une caisse de 0,7 m. Sans le
       socle des deux côtés, c'est lui qu'on mesure : la sculpture a d'abord été
       créditée d'une luminance de 5,4/255 qui était celle de son piédestal. */
    const decor = (p) => ({ recul: p.recul ?? 6, socle: p.socle ?? 0 })
    const fondPour = async (p) => {
      const d = decor(p)
      const cle = `${d.recul}/${d.socle}`
      if (!fonds.has(cle)) {
        const f = await rendre(page, { sujet: 'aucun', ...d })
        fonds.set(cle, await pixels(page, f.png))
        if (cle === '6/0') fs.writeFileSync(path.join(RACINE, 'captures', 'fond.png'), f.png)
      }
      return fonds.get(cle)
    }

    const pxFond = await fondPour({})
    let maxFond = 0
    for (let i = 0; i < pxFond.length; i += 4)
      maxFond = Math.max(maxFond, lum(pxFond[i], pxFond[i + 1], pxFond[i + 2]))
    /* ⚠️ Une référence noire ne prouve pas une salle sombre : elle prouve
       qu'on n'a rien rendu. On refuse de mesurer plutôt que de publier vingt
       chiffres faux. */
    if (maxFond < 8) throw new Error(
      `référence noire (luminance max ${maxFond.toFixed(1)}/255) — rien n'a été rendu`)
    releve.luminanceMaxDuFond = +maxFond.toFixed(1)
    const cas = []
    // 1. La courbe d'albédo : à partir de quand l'uniforme disparaît-il ?
    for (const albedo of [0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16, 0.22, 0.30, 0.45])
      cas.push({ nom: `garde albédo ${albedo}`, p: { sujet: 'garde', matiere: 'palette', albedo } })
    // 2. Le recul : le garde qu'on voit à 6 m se voit-il encore à 12 ?
    for (const recul of [3, 6, 9, 12])
      cas.push({ nom: `garde à ${recul} m`, p: { sujet: 'garde', matiere: 'palette', albedo: 0.16, recul } })
    /* 3. Les trois origines dans la même pièce, sous la même lumière.
       « origine » = les matières livrées par le fournisseur ; « palette » = la
       maille rebranchée sur l'unique matériau du musée. Le garde change de
       FICHIER entre les deux : `garde.glb` sort de la chaîne déjà dépouillé. */
    const surSocle = (s) => (s === 'sculpture' ? { socle: 1 } : {})
    for (const [nom, sujet] of [['garde', 'garde-texture'], ['banc', 'banc'],
                                ['sculpture', 'sculpture']])
      cas.push({ nom: `${nom} / origine`,
                 p: { sujet, matiere: 'origine', albedo: 0.16, ...surSocle(nom) } })
    for (const sujet of ['garde', 'banc', 'sculpture'])
      cas.push({ nom: `${sujet} / palette`,
                 p: { sujet, matiere: 'palette', albedo: 0.16, ...surSocle(sujet) } })

    /* 4. Le plafond de faces d'une sculpture générée, à DEUX mètres et la nuit —
       la distance que l'énoncé du ticket nomme. On compare chaque décimation à
       la salle (est-elle visible ?) ; la tenue de la SILHOUETTE, elle, se lit
       dans `mesurer-decimation.mjs`, qui compare les rendus entre eux. */
    for (const n of [15000, 4000, 2000, 1000, 500])
      cas.push({ nom: `bronze ${n} tris à 2 m`,
                 p: { sujet: 'sculpture', modele: `./sources/tripo/tripo-${n}-palette.glb`,
                      matiere: 'origine', socle: 1, recul: 2 } })

    for (const c of cas) {
      const r = await rendre(page, c.p)
      const m = comparer(await pixels(page, r.png), await fondPour(c.p))
      const ok = m.partNette >= SEUILS.partNette && m.p90 >= SEUILS.p90
      releve.mesures.push({ nom: c.nom, params: c.p, triangles: r.infos.triangles, ...m, tenu: ok })
      console.log(`  ${ok ? '✅' : '❌'} ${c.nom.padEnd(24)} p90=${String(m.p90).padStart(5)}  ` +
        `partNette=${String(m.partNette).padStart(5)}  moyen=${String(m.ecartMoyen).padStart(5)}  ` +
        `sujet=${m.luminanceSujet}/fond=${m.luminanceFond}  px=${m.pixels}`)
      const nom = c.nom.replace(/[^a-z0-9]+/gi, '-').toLowerCase()
      fs.writeFileSync(path.join(RACINE, 'captures', nom + '.png'), r.png)
    }
  } finally {
    await navigateur.close()
    fs.rmSync(profil, { recursive: true, force: true })
  }
  fs.mkdirSync(path.join(RACINE, 'releves'), { recursive: true })
  fs.writeFileSync(path.join(RACINE, 'releves', 'silhouette.json'),
    JSON.stringify(releve, null, 1))
  console.log('\nrelevé → releves/silhouette.json')
}

main().catch((e) => { console.error(e); process.exit(1) })
