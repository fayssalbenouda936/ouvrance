# La feuille de la carte, couchée ou debout — le banc de raccord

Prototype jetable du ticket
[#42](https://github.com/fayssalbenouda936/ouvrance/issues/42).
Il ne se lit pas, il se manipule : `python3 -m http.server` dans ce dossier,
puis `http://localhost:8000/`.

Il joue **les vrais films** et fait la passe film → lettre en direct. C'est la
seule différence qui compte avec le banc de [#30](https://github.com/fayssalbenouda936/ouvrance/issues/30),
qui ouvrait sur une image d'arrivée figée : le raccord ne se juge pas sur une
image fixe.

## Les cinq voies — `?v=C|G|R|F|N`

| | film | feuille | colonne | budget à 15 px | Emplacements |
| --- | --- | --- | --- | --- | --- |
| **C** couchée (statu quo) | prod, inchangé | double page, 1,35 | 117 px | **32 car.** | 6 |
| **G** debout par croissance | prod, inchangé | une colonne, hauteur libre | **232 px** | **303 car.** | 6 * |
| **R** debout par redressement | prod, inchangé | se redresse en 0,78 s | 232 px | 303 car. | 6 * |
| **F** debout, film re-tiré | `film2b`, déjà tiré | une colonne étroite | 133 px | 242 car. | 3 |
| **N** debout, pleine largeur | **aucun — à tirer** | quatre bords fixés | 232 px | **344 car.** | 6 * |

\* six seulement si le polaroïd passe de 104 px à 74 px — photo au plancher de 64 px.

## Ce que le banc mesure au lieu de l'estimer

- **Le cadrage où chaque film laisse sa feuille**, décodé sur la dernière image
  par projection de gradient. Le seuillage par luminance ne marche pas ici : le
  lin est presque aussi clair que le papier, Otsu tombe à 163 et le drap passe
  avec. Ce sont les bords **droits** du papier qui le trahissent, pas sa clarté.
- **L'erreur de raccord bord par bord**, en pixels.
- Le budget du message, par dichotomie sur une feuille clonée hors écran.
- Les caractères par ligne, à la sonde, dans la Parisienne réellement chargée.
- Ce que la table porte encore une fois la feuille posée.

## Les deux films, et leurs dernières images

`films/depliage-double.mp4` est **bit pour bit** le film servi en production
(md5 `29c4071e…`, c'est `essais-decors/films/film2h-bordure.mp4` du legacy) :
10 s, prompté pour finir sur une **double page couchée**, fausse écriture et
faux polaroïds peints dessus → `derniere-image-film-prod.png`.

`films/depliage-portrait.mp4` est `film2b-depliage.mp4`, une passe **antérieure**
du même dépliage : 5 s, papier **vierge**, feuille **portrait** →
`derniere-image-film2b.png`. La voie F n'est donc pas une dépense à consentir :
elle est déjà tirée, et elle dormait dans le legacy.

## Deux bugs trouvés en construisant le banc, gardés en commentaire

- `seeked` ne garantit pas qu'une image neuve soit décodée : `drawImage()` y
  rendait encore l'image **zéro**. Les deux films rendaient alors le même
  cadrage — c'est ce qui a trahi le bug.
- `requestVideoFrameCallback` ne se déclenche pas sur un `<video>` détaché du
  document. En tête sans écran, la promesse ne se résolvait jamais.
