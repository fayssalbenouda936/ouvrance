#!/usr/bin/env node
/**
 * LE PLAFOND DE FACES — à 2 000 triangles, la silhouette d'un bronze tient-elle
 * encore à deux mètres, la nuit ?
 *
 *     node outils/mesurer-plafond-de-faces.mjs [url-de-base]
 *
 * ⚠️⚠️ CE QU'IL NE FAUT PAS MESURER. Comparer le rendu décimé au rendu plein en
 * comptant les pixels qui changent mélange DEUX choses : la forme, et l'ombrage.
 * Une maille décimée est plus facettée, donc elle accroche autrement la lumière
 * — et sur un bronze métallique l'écart d'ombrage écrase de loin l'écart de
 * forme. Le premier relevé faisait passer la luminance de 7,6 à 19,7 en
 * décimant, ce qui n'apprend rien sur la silhouette.
 *
 * ⭐ ON MESURE DONC DES MASQUES, pas des couleurs. Pour chaque variante, le
 * masque est l'ensemble des pixels qui diffèrent de la salle VIDE : c'est
 * exactement la surface que l'objet occupe à l'écran. On compare ensuite les
 * masques entre eux par intersection sur union — une silhouette qui tient donne
 * un IoU proche de 1, quel que soit ce que la lumière fait à l'intérieur.
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
const PLAFONDS = [15000, 4000, 2000, 1000, 500]
const RECULS = [2, 4]
/** Un pixel appartient au sujet dès qu'il diffère franchement de la salle vide. */
const SEUIL_MASQUE = 2

const attendre = (ms) => new Promise((r) => setTimeout(r, ms))
const lum = (r, g, b) => 0.2126 * r + 0.7152 * g + 0.0722 * b

async function rendre(page, params) {
  await page.goto(base + '?mesure=1&' + new URLSearchParams(params), { waitUntil: 'load' })
  await page.waitForFunction('window.__banc && window.__banc.pret', { timeout: 30000 })
  const infos = await page.evaluate(() => window.__banc)
  if (infos.erreur) throw new Error(infos.erreur)
  await attendre(120)
  return { infos, png: await page.screenshot({ type: 'png' }) }
}

async function pixels(page, png) {
  return Uint8Array.from(await page.evaluate(async (b64) => {
    const img = new Image(); img.src = 'data:image/png;base64,' + b64; await img.decode()
    const c = document.createElement('canvas'); c.width = img.width; c.height = img.height
    const x = c.getContext('2d'); x.drawImage(img, 0, 0)
    return Array.from(x.getImageData(0, 0, c.width, c.height).data)
  }, Buffer.from(png).toString('base64')))
}

const masque = (avec, sans) => {
  const n = avec.length / 4
  const m = new Uint8Array(n)
  for (let i = 0; i < n; i++) {
    const j = i * 4
    m[i] = Math.abs(lum(avec[j], avec[j + 1], avec[j + 2]) -
                    lum(sans[j], sans[j + 1], sans[j + 2])) > SEUIL_MASQUE ? 1 : 0
  }
  return m
}

function iou(a, b) {
  let inter = 0, union = 0, seulA = 0, seulB = 0
  for (let i = 0; i < a.length; i++) {
    if (a[i] && b[i]) inter++
    if (a[i] || b[i]) union++
    if (a[i] && !b[i]) seulA++
    if (!a[i] && b[i]) seulB++
  }
  return { inter, union, seulA, seulB, iou: union ? +(inter / union).toFixed(4) : 0 }
}

async function main() {
  const profil = fs.mkdtempSync(path.join(os.tmpdir(), 'faces-'))
  const nav = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome', headless: 'new',
    defaultViewport: { width: 440, height: 764, deviceScaleFactor: 1 },
    args: ['--no-sandbox', `--user-data-dir=${profil}`, '--use-angle=vulkan',
      '--enable-features=Vulkan', '--ignore-gpu-blocklist'],
  })
  const releve = { le: new Date().toISOString(), seuilMasque: SEUIL_MASQUE, reculs: {} }
  try {
    const page = (await nav.pages())[0]
    page.on('pageerror', (e) => console.error('  ✗ page :', e.message))
    await rendre(page, { sujet: 'aucun' })          // ⚠️ la chauffe : cf. mesurer-silhouette

    for (const recul of RECULS) {
      const vide = await pixels(page, (await rendre(page, { sujet: 'aucun', socle: 1, recul })).png)
      const masques = {}
      const lignes = []
      for (const n of PLAFONDS) {
        const r = await rendre(page, {
          sujet: 'sculpture', modele: `./sources/tripo/tripo-${n}-palette.glb`,
          matiere: 'origine', socle: 1, recul,
        })
        masques[n] = masque(await pixels(page, r.png), vide)
        lignes.push({ triangles: n, surface: masques[n].reduce((a, b) => a + b, 0) })
      }
      const ref = masques[PLAFONDS[0]]
      for (const l of lignes) Object.assign(l, iou(ref, masques[l.triangles]))
      releve.reculs[recul] = lignes
      console.log(`\n  à ${recul} m — référence ${PLAFONDS[0]} triangles`)
      for (const l of lignes)
        console.log(`    ${String(l.triangles).padStart(6)} tris  surface=${String(l.surface).padStart(5)} px  ` +
          `IoU=${l.iou}  perdus=${l.seulA}  gagnés=${l.seulB}`)
    }
  } finally {
    await nav.close(); fs.rmSync(profil, { recursive: true, force: true })
  }
  fs.writeFileSync(path.join(RACINE, 'releves', 'plafond-de-faces.json'),
    JSON.stringify(releve, null, 1))
  console.log('\nrelevé → releves/plafond-de-faces.json')
}

main().catch((e) => { console.error(e); process.exit(1) })
