#!/usr/bin/env python3
"""
Ramène une sculpture générée à un plafond de faces, et dit ce qu'elle a perdu.

    ~/.local/blender-4.2/blender --background --python outils/decimer-sculpture.py -- \
        <entree.glb> <dossier-sortie> 15000 4000 2000 1000 500

⚠️ POURQUOI. La résolution de #25 ramène le `face_limit` de Tripo de 15 000 à
2 000 sans l'avoir éprouvé. Un tirage à 0,30 $ ne se re-tire pas pour vérifier :
on DÉCIME celui qu'on a déjà, ce qui isole exactement la variable — même forme,
même texture, même éclairage, un seul plafond qui bouge. Ce que ça ne dit pas :
Tripo pourrait mieux répartir ses 2 000 faces qu'un décimateur. La mesure donne
donc une borne PESSIMISTE, ce qui est le bon sens de l'erreur.
"""
import json
import sys
from pathlib import Path

import bpy


def main() -> int:
    argv = sys.argv[sys.argv.index('--') + 1:]
    palette = '--palette' in argv
    argv = [a for a in argv if a != '--palette']
    src, dest, plafonds = Path(argv[0]), Path(argv[1]), [int(x) for x in argv[2:]]
    dest.mkdir(parents=True, exist_ok=True)
    rapport = {'source': src.name, 'variantes': []}

    for plafond in plafonds:
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(src))
        mailles = [o for o in bpy.context.scene.objects if o.type == 'MESH']
        avant = sum(len(o.data.polygons) for o in mailles)
        tris_avant = sum(sum(max(0, len(p.vertices) - 2) for p in o.data.polygons)
                         for o in mailles)
        if tris_avant > plafond:
            ratio = plafond / tris_avant
            for o in mailles:
                m = o.modifiers.new('decimer', 'DECIMATE')
                m.ratio = ratio
                bpy.context.view_layer.objects.active = o
                bpy.ops.object.modifier_apply(modifier=m.name)
        mailles = [o for o in bpy.context.scene.objects if o.type == 'MESH']
        tris = sum(sum(max(0, len(p.vertices) - 2) for p in o.data.polygons) for o in mailles)
        if palette:
            # Le dépouillement de #25, appliqué ici aussi : c'est LUI qui fait le poids.
            mat = bpy.data.materials.new('MI_Palette_Musee')
            mat.use_nodes = True
            p = mat.node_tree.nodes['Principled BSDF']
            p.inputs['Base Color'].default_value = (0.42, 0.34, 0.18, 1.0)  # bronze
            p.inputs['Roughness'].default_value = 0.45
            p.inputs['Metallic'].default_value = 0.85
            for o in mailles:
                o.data.materials.clear(); o.data.materials.append(mat)
            for img in list(bpy.data.images):
                if img.name != 'Render Result':
                    bpy.data.images.remove(img)
        sortie = dest / f'tripo-{plafond}{"-palette" if palette else ""}.glb'
        bpy.ops.export_scene.gltf(filepath=str(sortie), export_format='GLB')
        rapport['variantes'].append({
            'plafond': plafond, 'faces_avant': avant, 'triangles_avant': tris_avant,
            'triangles': tris, 'octets': sortie.stat().st_size, 'fichier': sortie.name,
            'palette': palette})
        print(f'  {plafond:>6} → {tris:>6} tris, {sortie.stat().st_size:>8} o')

    (dest / ('decimation-palette.json' if palette else 'decimation.json')).write_text(json.dumps(rapport, indent=1, ensure_ascii=False))
    print('RAPPORT ' + json.dumps(rapport, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
