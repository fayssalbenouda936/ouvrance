# Le banc d'essai d'une maille entrante

Salle témoin **jetable** pour [#38](https://github.com/fayssalbenouda936/ouvrance/issues/38).
Ce qui survit d'elle : les chiffres de `releves/`, les planches de `captures/`
et la chaîne de `outils/`.

## Rejouer

```sh
node outils/recolter.mjs          # reconstitue sources/ (voir PROVENANCE.json)
python3 -m http.server 5199       # la salle a besoin d'un serveur, pas de file://
node outils/mesurer-silhouette.mjs
node outils/mesurer-plafond-de-faces.mjs
python3 outils/planches.py
```

La fenêtre est **440 × 764 CSS à ratio de pixels 1** — celle qu'a mesurée la
sonde de [#17](https://github.com/fayssalbenouda936/ouvrance/issues/17), barre
d'adresse comprise, puisqu'il n'y a pas de plein écran sur iPhone. Le champ est
celui de [#29](https://github.com/fayssalbenouda936/ouvrance/issues/29) : FOV
vertical 78°.

## Ce que le banc a trouvé

### 1. L'inventaire, et le compte y est

`Universal Animation Library` **Standard** : **45 clips** au volume 1, **43** au
volume 2, deux miroirs concordants. Le « 250+ » de l'énoncé du ticket n'existe
nulle part ; la page de l'auteur annonce **120+**, ce que le tirage gratuit ne
tient pas non plus. Mais les six mouvements demandés sont **tous** là :

| Il faut | Clip | Volume |
| --- | --- | --- |
| la ronde | `Walk_Loop`, `Walk_Formal_Loop` | 1 |
| le guet | `Pistol_Idle_Loop`, `Idle_Loop`, `Idle_FoldArms_Loop` | 1, 2 |
| le tir | `Pistol_Shoot` + `Pistol_Aim_Up/Neutral/Down`, `Pistol_Reload` | 1 |
| l'impact | `Hit_Chest`, `Hit_Head`, `Hit_Knockback` | 1, 2 |
| la chute | `Death01` | 1 |
| l'accroupissement | `Crouch_Idle_Loop`, `Crouch_Fwd_Loop` | 1 |

**Le retrait de Mixamo ne se rouvre pas.** Une seule réserve : `Death01` est la
**seule** mort du tirage gratuit — six gardes tomberont de la même façon.

### 2. Le squelette est le même, au nom près

**65 os, aucune différence** entre le corps (`Universal Base Characters`) et la
bibliothèque d'animations. Aucun réadaptage, aucune table de correspondance : la
chaîne de préparation perd son étape la plus fragile.

### 3. Les poids, mesurés

| | octets | gzip | triangles | clips |
| --- | ---: | ---: | ---: | ---: |
| garde legacy (Mixamo Ch18) | 789 588 | 594 802 | 41 532 | 4 |
| garde Quaternius, matières du fournisseur | 2 981 000 | 2 123 355 | 14 398 | 6 |
| ⤷ + meshopt | 1 907 684 | 1 772 228 | 14 398 | 6 |
| **garde Quaternius, dépouillé + meshopt** | **184 148** | **91 533** | 14 398 | 6 |
| banc Kenney + meshopt | 3 164 | 1 801 | — | — |
| bronze 2 000 tris, dépouillé + meshopt | 15 336 | 12 871 | 2 000 | — |

Les trois plafonds de l'énoncé (garde 400 ko, salle 250 ko, sculpture 120 ko)
sont tenus **par le dépouillement, pas par la décimation** — voir 5.

Décodeurs, mesurés : **meshopt 8 071 o gzip** en une requête, **Draco 99 880 o
en deux** (11 680 + 88 200). Les chiffres de #25 sont confirmés.

### 4. Le noir a deux régimes, et un angle mort entre les deux

Garde à 6 m, matériau de palette, albédo balayé. La **luminance du mur est de
22,5/255**.

| albédo | luminance du garde | p90 | part nette |
| ---: | ---: | ---: | ---: |
| 0,02 | 6,5 | 22,4 | 0,79 |
| 0,04 | 10,4 | 19,3 | 0,64 |
| 0,06 | 14,6 | 15,8 | 0,34 |
| 0,08 | 18,7 | 13,6 | 0,14 |
| **0,10** | **22,6** | **14,3** | **0,15** |
| 0,13 | 28,2 | 18,5 | 0,23 |
| 0,16 | 33,2 | 23,2 | 0,37 |
| 0,22 | 42,7 | 33,9 | 0,86 |
| 0,30 | 54,0 | 47,1 | 0,96 |
| 0,45 | 72,6 | 68,5 | 0,99 |

À **albédo 0,10 la luminance du garde égale exactement celle du mur** et il
s'éteint. De part et d'autre il se voit — en silhouette sombre d'un côté, en
corps éclairé de l'autre. Le danger n'est donc pas d'être sombre, **c'est d'être
à la luminance du fond**.

⚠️ **Le seuil du legacy ne sait lire qu'un seul des deux régimes.** `p90 ≥ 30`
est inatteignable par le bas : un pixel ne descend pas sous zéro, donc l'écart
maximal qu'une silhouette sombre puisse produire est la luminance du fond
elle-même — **22,5 ici**. Le banc marque « ❌ » un garde à albédo 0,02 que la
planche montre parfaitement lisible. Le liséré du legacy n'était pas un
rafistolage : dans une salle à ce niveau, il était la seule direction ouverte.

### 5. Le plafond de faces se trompe de levier

Silhouette du bronze à 2 m, comparée en masques (intersection sur union) à la
maille pleine :

| triangles | surface à l'écran | IoU à 2 m | IoU à 4 m |
| ---: | ---: | ---: | ---: |
| 15 000 | 1 612 px | 1 | 1 |
| 4 000 | 1 598 px | 0,969 | 0,975 |
| **2 000** | **1 597 px** | **0,957** | **0,973** |
| 1 000 | 1 600 px | 0,949 | 0,948 |
| 500 | 1 596 px | 0,940 | 0,946 |

**La silhouette tient** : de 15 000 à 2 000 triangles, 43 pixels perdus et 28
gagnés sur 1 612. Le `face_limit` à 2 000 de #25 est confirmé — et le vrai
plancher est plus bas encore.

Mais il ne fait pas le poids. Les **trois JPEG du tirage pèsent 378 768 octets,
constants**, quelle que soit la décimation : à 500 triangles le fichier fait
encore 400 696 o, soit **3,3 fois le plafond de 120 ko**. Dépouillé, le même
objet à 2 000 triangles tombe à **15 336 o**. La règle de cohérence de #25 est
donc aussi, et surtout, la règle de budget.

### 6. L'origine ne se voit plus — mais la lisibilité ne survit pas seule

Même pièce, même lumière, albédo 0,16 :

| | luminance | p90 | part nette |
| --- | ---: | ---: | ---: |
| garde, matières du fournisseur | 40,8 | 33,7 | 0,82 |
| garde, palette | 33,2 | 23,2 | 0,37 |
| banc Kenney, atlas d'origine | 88,0 | 107,1 | 1,00 |
| banc Kenney, palette | 34,8 | 29,9 | 0,21 |
| bronze, texture Tripo | 22,9 | 20,5 | 0,54 |
| bronze, palette | 32,3 | 12,1 | 0,18 |

Les trois origines rebranchées sur le même matériau se rangent entre **32,3 et
34,8** de luminance : **elles cessent d'être distinguables**. C'est exactement
ce que #25 avait posé sans le mesurer.

⚠️ **Et c'est aussi la limite de la règle.** Un albédo unique de 0,16 dépose les
trois objets dans l'angle mort du §4 : le banc perd 79 % de sa netteté en étant
dépouillé, et le garde passe sous le seuil que sa texture d'origine tenait.
Dépouiller **et** rebrancher sur une seule valeur, c'est troquer une incohérence
visible contre une invisibilité qui, elle, ne se voit pas.

## Les pièges rencontrés, et ce qu'ils coûtaient

Trois défaillances **silencieuses**, toutes trouvées en relisant une sortie
plutôt qu'en lisant un message d'erreur.

1. **`id_root` vide** — l'importeur FBX n'assigne que la première action ;
   l'exporteur glTF ne retient que les actions estampillées. Sortie : un GLB
   valide avec **un** clip sur six, sans un mot. `preparer-garde.py` relit
   désormais sa propre sortie et refuse un compte qui ne tombe pas juste.
2. **Contexte WebGL perdu à la première navigation** — la référence « salle
   vide » était **entièrement noire**, et le banc a mesuré la salle contre le
   vide en annonçant **vingt succès**. Une navigation de chauffe, puis un refus
   de mesurer si la référence est noire.
3. **Le socle dans la différence** — posé avec la sculpture et absent de la
   référence, c'est lui qu'on mesurait : la sculpture a été créditée d'une
   luminance de 5,4/255 qui était celle de son piédestal. Le décor ne se déduit
   plus du sujet, il se demande.

⚠️ `ignore_leaf_bones=True`, obligatoire sur Mixamo, retire **13 os dont
`Head`** sur le rig Quaternius. Piège évité, jamais payé.
