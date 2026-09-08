#!/usr/bin/env node
/**
 * RÉCOLTE — reconstitue tout ce que `.gitignore` écarte du dépôt.
 *
 *     node outils/recolter.mjs
 *
 * Le banc est jetable, ses octets se refabriquent. Ce qui est versionné, ce
 * sont les outils, les relevés et les planches ; les 9 Mo de mailles et de
 * bibliothèques, non.
 *
 * ⚠️ CE SCRIPT NE PREND RIEN CHEZ L'AUTEUR DES PAQUETS. itch.io oppose un défi
 * Cloudflare à toute requête non navigateur : les fichiers Quaternius viennent
 * de MIROIRS GitHub publics, ce que CC0 autorise et que `PROVENANCE.json`
 * consigne. Un miroir n'est pas la source — avant d'en faire un asset de
 * production, retélécharger depuis quaternius.com et comparer les empreintes.
 */
import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import { pipeline } from 'node:stream/promises'
import { Readable } from 'node:stream'

const RACINE = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..')
const SRC = path.join(RACINE, 'sources')
const NAVIGATEUR = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' +
  '(KHTML, like Gecko) Chrome/140.0 Safari/537.36'

const MIROIR = 'https://raw.githubusercontent.com'
const UBC = `${MIROIR}/kirbycope/godot-3d-player-controller-v2/HEAD/` +
  'assets/universal_base_characters/Base%20Characters'

const A_PRENDRE = [
  ['UAL1_Standard.fbx', `${MIROIR}/IAFahim/quaternius.universalAnimationLibrary.standard/HEAD/UAL1_Standard.fbx`],
  ['UAL2_Standard.glb', `${MIROIR}/Ladoladola/characteractionconcepttest/HEAD/UAL2_Standard.glb`],
  ['kenney_furniture-kit.zip', 'https://kenney.nl/media/pages/assets/furniture-kit/440e0608a4-1677580847/kenney_furniture-kit.zip'],
  ...['Superhero_Male_FullBody.gltf', 'Superhero_Male_FullBody.bin',
      'T_Superhero_Male_Dark.png', 'T_Superhero_Male_Normal.png',
      'T_Superhero_Male_Roughness.png', 'T_Eye_Brown.png', 'T_Eye_Normal.png',
      'T_Hair_1_BaseColor.png', 'T_Hair_1_Normal.png']
    .map((f) => [path.join('ubc', f), `${UBC}/${f}`]),
]

async function prendre(rel, url) {
  const dest = path.join(SRC, rel)
  if (fs.existsSync(dest) && fs.statSync(dest).size > 0) return console.log('  ·', rel)
  fs.mkdirSync(path.dirname(dest), { recursive: true })
  const r = await fetch(url, { headers: { 'User-Agent': NAVIGATEUR } })
  if (!r.ok) throw new Error(`${rel} : HTTP ${r.status}`)
  await pipeline(Readable.fromWeb(r.body), fs.createWriteStream(dest))
  console.log('  ↓', rel, fs.statSync(dest).size, 'o')
}

console.log('Récolte →', SRC)
for (const [rel, url] of A_PRENDRE) await prendre(rel, url)

// Le banc Kenney sort du zip ; on n'en garde qu'une pièce.
const banc = path.join(SRC, 'kenney-bench.glb')
if (!fs.existsSync(banc)) {
  execFileSync('python3', ['-c', `
import zipfile, sys
z = zipfile.ZipFile(sys.argv[1])
open(sys.argv[2], 'wb').write(z.read('Models/GLTF format/bench.glb'))
`, path.join(SRC, 'kenney_furniture-kit.zip'), banc])
  console.log('  ↓ kenney-bench.glb', fs.statSync(banc).size, 'o')
}

console.log(`
⚠️ DEUX CHOSES QUE CE SCRIPT NE PEUT PAS ALLER CHERCHER :

  · sources/tripo-oeuvre.glb — le tirage Tripo vient du legacy,
    apps/gifts/_templates/infiltration/essais-assets/oeuvre-3d.glb
  · vendor/three — copié depuis le même legacy, vendor/three (r185)
    vendor/meshopt — meshopt_decoder.module.js de npm meshoptimizer@0.25.0

Puis, pour refabriquer les mailles mesurées :

  ~/.local/blender-4.2/blender --background --python outils/preparer-garde.py -- \\
      sources/ubc/Superhero_Male_FullBody.gltf sources/UAL1_Standard.fbx \\
      sources/garde-palette.glb Walk_Loop Pistol_Idle_Loop Pistol_Shoot \\
      Hit_Chest Death01 Crouch_Idle_Loop --palette
  npx gltfpack@1.2.0 -i sources/garde-palette.glb -o sources/garde.glb -cc

  ~/.local/blender-4.2/blender --background --python outils/decimer-sculpture.py -- \\
      sources/tripo-oeuvre.glb sources/tripo 15000 4000 2000 1000 500 --palette
`)
