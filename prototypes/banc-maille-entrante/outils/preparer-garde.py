#!/usr/bin/env python3
"""
LA CHAÎNE DE PRÉPARATION D'UNE MAILLE ENTRANTE, éprouvée sur source Quaternius.

    ~/.local/blender-4.2/blender --background --python outils/preparer-garde.py -- \
        <corps.gltf> <animations.fbx> <sortie.glb> <clip> [<clip>…]

⚠️⚠️ CE QU'ELLE REMPLACE. Le legacy fusionnait CINQ exports Mixamo de ~14 Mo,
chacun portant une copie complète du personnage et de ses textures, puis triait
les clips pour jeter 80 % du fichier. Quaternius ne pose pas ce problème : le
CORPS arrive dans un fichier (`Universal Base Characters`) et TOUTES les
animations dans un autre (`Universal Animation Library`). Il n'y a donc plus de
fusion à faire, seulement un TRANSFERT d'actions — et un tri, qui lui reste.

⭐ CE QUI REND LE TRANSFERT GRATUIT : les deux paquets partagent le squelette au
NOM PRÈS — 65 os, aucune différence, mesuré. Une action Blender est indexée par
nom d'os : elle s'applique donc au corps sans réadaptage, exactement comme les
exports Mixamo entre eux. Aucun retargeting, aucune table de correspondance.

⚠️⚠️ LE PIÈGE `ignore_leaf_bones`. Le legacy importe les FBX Mixamo avec
`ignore_leaf_bones=True` — obligatoire là-bas, mortel ici : sur le rig
Quaternius, il retire 13 os, dont **`Head`**. Le garde marcherait alors avec la
tête soudée au cou, et RIEN ne le signalerait — ni erreur, ni avertissement.
On importe donc avec `ignore_leaf_bones=False`.

⚠️⚠️ LE PIÈGE QUI A COÛTÉ LA PREMIÈRE PASSE — `id_root`. L'importeur FBX
n'assigne au squelette que la PREMIÈRE action ; les 44 autres restent orphelines
et Blender laisse leur `id_root` VIDE. Or l'exporteur glTF ne retient que les
actions dont l'`id_root` vaut `OBJECT`. Sortie : un GLB parfaitement valide,
avec UN SEUL clip sur les six demandés, sans le moindre message. C'est le
« cinquième clip parasite » du legacy retourné et aggravé — là-bas on exportait
un clip de trop, ici on en perd cinq. On assigne donc chaque action au squelette
à tour de rôle, ce qui estampille son `id_root`, et **la chaîne relit sa propre
sortie** : un compte de clips qui ne tombe pas juste arrête tout.

⚠️ LE DÉPOUILLEMENT DES MATIÈRES est une étape de cette chaîne, pas une option :
la règle du dépôt (issue #25) veut que toute maille entrante perde ses matériaux
d'origine et soit rebranchée sur l'unique palette du musée. `--palette` le fait
et écrit la couleur retenue dans le GLB ; sans lui, on exporte tel quel, ce qui
ne sert qu'à comparer les deux.
"""
import json
import sys
from pathlib import Path

import bpy

CLIPS_PAR_DEFAUT = ['Walk_Loop', 'Pistol_Idle_Loop', 'Pistol_Shoot', 'Hit_Chest', 'Death01']


def vider() -> None:
    bpy.ops.wm.read_factory_settings(use_empty=True)


def armature(scene=None):
    for o in (scene or bpy.context.scene).objects:
        if o.type == 'ARMATURE':
            return o
    return None


def importer_corps(chemin: Path):
    """Le corps arrive en glTF : Blender lit son squelette et ses matières."""
    avant = set(bpy.context.scene.objects)
    bpy.ops.import_scene.gltf(filepath=str(chemin))
    return [o for o in bpy.context.scene.objects if o not in avant]


def importer_animations(chemin: Path):
    """⚠️ ignore_leaf_bones=False — sinon `Head` disparaît en silence."""
    avant = set(bpy.context.scene.objects)
    bpy.ops.import_scene.fbx(filepath=str(chemin), ignore_leaf_bones=False,
                             automatic_bone_orientation=False)
    return [o for o in bpy.context.scene.objects if o not in avant]


def nom_court(action) -> str:
    """`Armature|Armature|Walk_Loop` → `Walk_Loop`."""
    return action.name.rsplit('|', 1)[-1]


def os_de(arm) -> set:
    return {b.name for b in arm.data.bones}


def clips_du_glb(chemin: Path) -> list:
    """Relit le GLB écrit et en sort les noms d'animations. Le contrôle final."""
    import struct
    d = chemin.read_bytes()
    off, js = 12, None
    while off < len(d):
        ln, ty = struct.unpack('<II', d[off:off + 8])
        if ty == 0x4E4F534A:
            js = json.loads(d[off + 8:off + 8 + ln])
        off += 8 + ln
    return [a.get('name') for a in (js or {}).get('animations', [])]


def main() -> int:
    argv = sys.argv[sys.argv.index('--') + 1:]
    palette = '--palette' in argv
    argv = [a for a in argv if a != '--palette']
    if len(argv) < 3:
        print(__doc__)
        return 2
    corps, anims, sortie = Path(argv[0]), Path(argv[1]), Path(argv[2])
    clips = argv[3:] or CLIPS_PAR_DEFAUT

    vider()
    objets_corps = importer_corps(corps)
    arm_corps = armature()
    if arm_corps is None:
        print('✗ aucun squelette dans le corps'); return 1

    objets_anims = importer_animations(anims)
    arm_anims = next(o for o in objets_anims if o.type == 'ARMATURE')

    # ── La vérification qui autorise le transfert ──────────────────────────
    a, b = os_de(arm_corps), os_de(arm_anims)
    rapport = {
        'corps': corps.name, 'animations': anims.name,
        'os_corps': len(a), 'os_animations': len(b),
        'os_communs': len(a & b),
        'os_manquants_dans_le_corps': sorted(b - a),
        'os_non_animes': sorted(a - b),
    }
    if b - a:
        print(f"✗ {len(b - a)} os animés absents du corps : {sorted(b - a)[:6]}…")
        print('  → un réadaptage serait nécessaire ; la chaîne s\'arrête ici.')
        return 1

    # ── Le transfert : une action est indexée par nom d'os, rien à faire ───
    disponibles = {nom_court(ac): ac for ac in bpy.data.actions}
    absents = [c for c in clips if c not in disponibles]
    if absents:
        print(f"✗ clips absents de la bibliothèque : {absents}")
        print(f"  disponibles : {sorted(disponibles)}")
        return 1

    gardees = []
    for c in clips:
        ac = disponibles[c]
        ac.name = c              # ⚠️ le nom du clip devient le nom lu par le jeu
        ac.use_fake_user = True  # sans quoi l'export ne le voit pas
        gardees.append(ac)

    # ⚠️ LE TRI. Tout ce qui n'est pas demandé part MAINTENANT : une action
    # laissée en place est exportée, et le fichier ne maigrit pas.
    for ac in list(bpy.data.actions):
        if ac not in gardees:
            bpy.data.actions.remove(ac)

    # Le mannequin gris de la bibliothèque n'a rien à faire dans la sortie.
    for o in objets_anims:
        bpy.data.objects.remove(o, do_unlink=True)

    if arm_corps.animation_data is None:
        arm_corps.animation_data_create()
    # ⚠️ L'assignation N'EST PAS décorative : elle estampille `id_root`, seul
    # critère que l'exporteur glTF regarde. Sans ce tour, il n'en sort qu'une.
    for ac in gardees:
        arm_corps.animation_data.action = ac
    arm_corps.animation_data.action = gardees[0]

    # ── Le dépouillement ──────────────────────────────────────────────────
    if palette:
        mat = bpy.data.materials.new('MI_Palette_Musee')
        mat.use_nodes = True
        p = mat.node_tree.nodes['Principled BSDF']
        p.inputs['Base Color'].default_value = (0.16, 0.16, 0.18, 1.0)
        p.inputs['Roughness'].default_value = 0.75
        p.inputs['Metallic'].default_value = 0.0
        for o in bpy.context.scene.objects:
            if o.type == 'MESH':
                o.data.materials.clear()
                o.data.materials.append(mat)
        for img in list(bpy.data.images):
            if img.name != 'Render Result':
                bpy.data.images.remove(img)
        rapport['palette'] = {'base_color': [0.16, 0.16, 0.18], 'roughness': 0.75}

    tris = sum(sum(max(0, len(p.vertices) - 2) for p in o.data.polygons)
               for o in bpy.context.scene.objects if o.type == 'MESH')
    rapport['triangles'] = tris
    rapport['clips_exportes'] = [ac.name for ac in gardees]

    sortie.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=str(sortie), export_format='GLB',
        export_animations=True, export_animation_mode='ACTIONS',
        export_nla_strips=False, export_optimize_animation_size=True,
        export_image_format='AUTO' if not palette else 'NONE',
    )
    rapport['octets'] = sortie.stat().st_size

    # ── La chaîne relit sa sortie ─────────────────────────────────────────
    relus = clips_du_glb(sortie)
    rapport['clips_relus'] = relus
    Path(str(sortie) + '.rapport.json').write_text(
        json.dumps(rapport, indent=1, ensure_ascii=False))
    print('RAPPORT ' + json.dumps(rapport, ensure_ascii=False))
    if sorted(relus) != sorted(clips):
        print(f"✗ le GLB écrit ne contient pas les clips demandés : "
              f"{sorted(relus)} ≠ {sorted(clips)}")
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
