# Le coût réel d'une expérience maître

Recherche pour l'issue [#5](https://github.com/fayssalbenouda936/ouvrance/issues/5), sous la carte [#1](https://github.com/fayssalbenouda936/ouvrance/issues/1).
Relevé des tarifs : **20 août 2026**. Analyse du journal : **journal complet, 285 appels, du 06/08/2026 au 16/08/2026**.

## Comment lire ce document

Deux natures de chiffres, jamais mélangées :

- **[MESURÉ]** — vient de `/home/fayssal/projetCadeau/outils/.fal-journal.jsonl`, du contenu du disque legacy, ou des atomes MP4 des fichiers produits. Ce sont des faits.
- **[ESTIMÉ]** — vient d'un tarif public appliqué à un paramètre mesuré. Le journal **ne consigne aucun montant** : il consigne `modele`, `entree`, `fichiers`, `secondes` (voir `outils/fal.mjs:339`). Tout euro de ce document est donc un recalcul, jamais une facture.

Quand une fourchette est donnée, la borne basse et la borne haute correspondent à deux hypothèses explicitées, pas à une marge d'erreur décorative.

Taux de change utilisé : **1 USD = 0,854 EUR** (source secondaire, confiance moyenne — la BCE ne publiait au moment du relevé qu'une valeur au 19/07/2026, 1 EUR = 1,1605 USD). Une variation de ±3 % du taux ne change aucune conclusion de ce document.

Scripts d'analyse reproductibles : `scripts/analyse-journal.py`, `scripts/analyse-projets.py`, `scripts/chiffrer-journal.py`, `scripts/sonder-videos.py`.

---

## 0. Le chiffre qui résume tout

**[MESURÉ + ESTIMÉ]** Le journal contient 285 appels fal.ai, qui ont produit 411 fichiers. **Trois fichiers vidéo sont réellement servis en production aujourd'hui** :

| Fichier servi | Durée | Poids | Appels qui l'ont produit | Coût |
|---|---|---|---|---|
| `combat-3d/films/ouverture.mp4` | 30,14 s | 6,73 Mo | `ouverture-libre` (1 appel Seedance 2.5, 30 s) | 13,87 $ |
| `combat-3d/films/fin.mp4` | 20,10 s | 3,82 Mo | `fin-libre`, 2ᵉ appel de 20 s (le 1ᵉʳ, à 9,24 $, a été jeté) | 9,24 $ |
| `animation-cadeau/public/films/depliage.mp4` | 10,08 s | 2,81 Mo | `film2h-bordure` (1 appel de 10 s, précédé de 6 essais) | 4,62 $ |

- Coût des rendus **servis** (les 4 appels ci-dessus) : **27,73 $ ≈ 23,7 €**
- Coût **total du journal** : **125,87 – 136,36 $ ≈ 107,5 – 116,5 €**

> **Il faut dépenser environ 4,7 € pour obtenir 1 € de rendu servi.**
> 4 appels sur 285 (**1,4 %**) produisent ce qui est en ligne.

C'est la réponse à la question du ticket : *« le nombre d'essais jetés est le vrai coût, pas le rendu final »*. Le facteur mesuré est **4,7×**, pas 1,2×.

---

## 1. Volumétrie du journal

**[MESURÉ]**

| | |
|---|---|
| Appels journalisés | **285** |
| Période | 2026-08-06T11:35 → 2026-08-16T18:56 (**11 jours**) |
| Fichiers produits | **411** |
| Fichiers encore présents sur disque | **213 (52 %)** |
| Fichiers disparus / supprimés | **198 (48 %)** |
| Temps machine cumulé (champ `secondes`) | **18 350 s = 5,10 h** |

Répartition par modèle :

| Modèle | Appels | Fichiers | Sur disque | Unités facturables mesurées | Durée médiane / appel |
|---|---|---|---|---|---|
| `fal-ai/nano-banana-pro/edit` | 97 | 175 | 103 | 175 images | 32,3 s |
| `fal-ai/bytedance/seedance/v1/lite/image-to-video` | 90 | 90 | 66 | 450 s de vidéo, 720p, sans audio | 42,2 s |
| `fal-ai/nano-banana-pro` | 63 | 107 | 30 | 107 images (dont 1 en 4K) | 29,4 s |
| `fal-ai/bytedance/seedance/v1.5/pro/image-to-video` | 9 | 9 | 0 | 45 s de vidéo | 89,2 s |
| `bytedance/seedance-2.5/reference-to-video` | 9 | 9 | 7 | 108 s de vidéo, audio actif | **281,8 s** |
| `bytedance/seedance-2.5/image-to-video` | 6 | 6 | 5 | 49 s de vidéo, audio actif | **225,8 s** |
| `bytedance/seedance-2.0/mini` + `/fast` | 4 | 4 | 0 | 20 s de vidéo | 110–192 s |
| `fal-ai/bytedance/seedream/v4` + `v5` | 5 | 8 | 0 | 10 images | 32,3 s |
| `minimax/h3/image-to-video` | 1 | 1 | 0 | 6 s | 171,4 s |
| `tripo3d/tripo/v2.5/image-to-3d` | 1 | 2 | 2 | 1 mesh | 101,4 s |

**Fait opérationnel à retenir** : un appel Seedance 2.5 prend **entre 2,5 et 7 minutes** (médiane 4,2 min, max 425,7 s), contre 42 s pour Seedance 1.0 lite. Ce n'est pas seulement 12× plus cher, c'est **6× plus lent**. Une boucle d'itération artistique sur 2.5 coûte 5 min d'attente par essai.

### Limite de la mesure « sur disque »

L'absence d'un fichier du disque n'est **pas une preuve de rejet** : il a pu être déplacé, renommé ou déployé ailleurs. Inversement, un fichier présent n'est pas forcément utilisé. J'utilise donc la présence disque comme **borne basse du gaspillage**, et les manifestes de montage (`cinematique/montage.json`, le dossier `retenus/`, `public/films/`) comme **signal faisant autorité** sur ce qui est réellement servi.

---

## 2. Les tarifs publics fal.ai, relevés le 20/08/2026

**[ESTIMÉ — sources primaires, pages `fal.ai/models/...`]**

> ⚠️ La page https://fal.ai/pricing **ne liste aucun** de ces modèles. Les tarifs à jour ne vivent que sur les pages de modèle individuelles. Vérifié le 20/08/2026.

| Modèle | Unité | Prix | Source | Confiance |
|---|---|---|---|---|
| **Seedance 2.5** (t2v / i2v / ref2v) | 1 000 tokens | **0,0214 $** — 480p et 720p | [/models/bytedance/seedance-2.5/reference-to-video](https://fal.ai/models/bytedance/seedance-2.5/reference-to-video) | Élevée |
| **Nano Banana Pro** (t2i et edit) | image | **0,15 $** (1K/2K), **0,30 $** (4K), +0,015 $ si web search | [/models/fal-ai/nano-banana-pro](https://fal.ai/models/fal-ai/nano-banana-pro) | Élevée |
| **Seedance 1.5 pro** | M tokens | **2,40 $** avec audio, **1,20 $** sans | [/models/fal-ai/bytedance/seedance/v1.5/pro/image-to-video](https://fal.ai/models/fal-ai/bytedance/seedance/v1.5/pro/image-to-video) | Élevée |
| **Seedance 1.0 lite** | M tokens | **1,80 $** — ⚠️ *endpoint déprécié, requêtes re-routées vers Seedance 1.0 Pro Fast (1,00 $/M)* | [/models/fal-ai/bytedance/seedance/v1/lite/image-to-video](https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/image-to-video) | Élevée sur la dépréciation, moyenne sur le tarif applicable en août |
| **Seedance 2.0** standard | 1 000 tokens | **0,014 $** (480p–1080p), 0,008 $ (4K) → 0,3024 $/s à 720p | [/models/bytedance/seedance-2.0/image-to-video](https://fal.ai/models/bytedance/seedance-2.0/image-to-video) | Élevée |
| **Seedance 2.0** fast | seconde | **0,2419 $/s** (max 720p) | idem | Élevée |
| **Seedance 2.0** *mini* | — | **non tarifé publiquement** | — | **Nulle** — borné dans les calculs entre 0,007 $/1000 tok et le tarif *fast* |
| **Seedream v4** (edit / t2i) | image | **0,03 $** | [/models/fal-ai/bytedance/seedream/v4/edit](https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit) | Élevée |
| **minimax/h3**, **tripo3d v2.5** | — | non relevé | — | **Nulle** — fourchettes larges assumées (2 appels au total, non structurant) |

### Formules de facturation — points qui changent les calculs

**Seedance 2.5** : `tokens = (hauteur × largeur × (durée_vidéo_entrée + durée_sortie) × 24) / 1024`

Trois clauses vérifiées mot pour mot sur la page fal :

1. *« Image and audio references are not billed »* — **les images de référence sont gratuites.** Les 9 appels `reference-to-video` du journal, qui passaient 3 images de référence chacun, n'ont pas payé pour ces références.
2. *« If any video references are provided, the price is multiplied by 0.6 »* — la remise ×0,6 s'applique **uniquement aux références vidéo**. Aucun appel du journal n'en utilise → **aucune remise appliquée dans mes calculs.**
3. **L'audio ne coûte rien de plus** : *« generate_audio does not change your token count — audio is generated in the same pass »*. Les 15 appels 2.5 du journal ont tous `generate_audio: true`. La décision de la carte de retirer ElevenLabs est donc gratuite en plus d'être simplificatrice.

**Résolutions 2.5** : uniquement `480p` et `720p`. **1080p n'existe pas** sur ce modèle. Le maître servi plafonne donc à 720×1280 — ce qui est cohérent avec un usage 9:16 sur téléphone, mais ferme la porte à un master 1080p sans changer de modèle.

**Durées 2.5** : entier de **4 à 30 s**, ou `"auto"`. Une cinématique de 50 s **ne peut pas** être produite en un seul appel — d'où le découpage mesuré en ouverture 30 s + fin 20 s.

### Prix à la seconde en 9:16 (le seul format qui nous concerne)

720p 9:16 = 720 × 1280 = 921 600 px. 480p 9:16 = 496 × 864 = 428 544 px.

| Modèle | 9:16 720p | 9:16 480p | Rapport au moins cher |
|---|---|---|---|
| **Seedance 2.5** (audio inclus) | **0,4622 $/s** | 0,2149 $/s | ×12,5 |
| Seedance 2.0 standard | 0,3024 $/s | — | ×8,2 |
| Seedance 2.0 fast | 0,2419 $/s | — | ×6,5 |
| Seedance 1.5 pro (avec audio) | 0,0518 $/s | — | ×1,4 |
| Seedance 1.5 pro (sans audio) | 0,0259 $/s | — | ×0,7 |
| **Seedance 1.0 lite** (704×1248 mesuré) | **0,0371 $/s** | — | **×1 (référence)** |

> **Seedance 2.5 coûte 12,5 fois le prix de Seedance 1.0 lite à la seconde.** C'est le fait tarifaire le plus structurant du dossier.

---

## 3. Coût réel par cinématique produite

Le journal contient **deux chaînes de production complètes** pour la même expérience (`combat-3d`), ce qui donne un point de comparaison rare.

### 3.1 — Chaîne A : montage 18 plans, Seedance 1.0 lite (servie jusqu'au 12/08/2026)

**[MESURÉ]** Traces : `combat-3d/plans/` (54 PNG candidats), `combat-3d/retenus/` (19 PNG promus), `combat-3d/rushes/` (18 MP4 de 5,04 s), `combat-3d/films/precedents-18-plans/` (ouverture 39,69 s + fin 18,86 s).

| Étape | Appels | Unités produites | Unités retenues | **Taux de retenue** | Coût [ESTIMÉ] |
|---|---|---|---|---|---|
| Images de plan (Nano Banana Pro) | 33 | 66 images | **19** (`retenus/`) | **29 %** | 9,90 $ |
| Rushes vidéo (Seedance 1.0 lite, 5 s, 720p) | 35 | 35 clips | **18** (`rushes/`) | **51 %** | 3,60 – 6,49 $ |
| **Total chaîne A** | **68** | | | | **13,50 – 16,39 $** (11,5 – 14,0 €) |

Film obtenu : **58,5 s** de cinématique en deux séquences.

- **1,94 appel Seedance par plan retenu**
- **3,5 images générées par image retenue**
- Coût par seconde de film servi : **0,23 – 0,28 $/s**

### 3.2 — Chaîne B : une passe, Seedance 2.5 (servie depuis le 12/08/2026)

**[MESURÉ]** `cinematique/montage.json` porte l'avertissement : *« CE FICHIER NE DÉCRIT PLUS LE FILM SERVI. Depuis le 12/08/2026, `films/ouverture.mp4` et `films/fin.mp4` sont générés en UNE PASSE par Seedance 2.5, audio natif compris. »* Les durées mesurées sur les MP4 confirment (30,11 s / 30,14 s, 20,10 s / 20,10 s).

| Appel | Durée demandée | Résultat | Coût [ESTIMÉ] |
|---|---|---|---|
| `fin-libre` (1ᵉʳ essai) | 20 s | **jeté** (écrasé par le 2ᵉ) | 9,24 $ |
| `fin-libre` (2ᵉ essai) | 20 s | **servi** → `films/fin.mp4` | 9,24 $ |
| `ouverture-libre` | 30 s | **servi** → `films/ouverture.mp4` | 13,87 $ |
| **Total chaîne B** | **70 s demandées** | **50 s servies** | **32,36 $** (27,6 €) |

- **1,5 appel par plan retenu**
- Coût par seconde de film servi : **0,645 $/s** (contre 0,462 $/s de tarif nu → **+40 % de surcoût d'essai**)
- **La chaîne B coûte 2,3× la chaîne A pour 8 s de film en moins**, mais elle apporte l'audio natif et supprime le montage.

⚠️ **La chaîne B est artificiellement bon marché.** Elle n'a eu besoin que de 1,5 essai par plan **parce que la chaîne A avait déjà payé le repérage** : découpage validé, direction artistique verrouillée, 19 images de référence retenues. On ne peut pas extrapoler ce taux à un film écrit à froid.

### 3.3 — Chaîne C : la carte animée, Seedance 2.5 à froid

**[MESURÉ]** C'est le seul chantier du journal où Seedance 2.5 a été utilisé **sans repérage préalable**. C'est donc la mesure honnête du coût d'exploration.

| Plan | Appels 2.5 | Durées | Issue | Coût [ESTIMÉ] |
|---|---|---|---|---|
| « parfum » (`film1`, `film1b`) | 2 | 10 s + 10 s | **direction entièrement abandonnée** | 9,24 $ |
| « dépliage » (`film2` → `film2h`) | 7 | 5+5+5+10+10+10+10 s | 1 retenu : `film2h-bordure` → `public/films/depliage.mp4` | 25,42 $ |
| **Total 2.5 carte** | **9** | **75 s demandées** | **10,08 s servies** | **34,67 $** |
| Décors, papiers, écritures (Nano Banana Pro) | 38 | 38 images | toutes conservées, 1 servie | 5,70 $ |
| **Total maître « carte animée »** | **47** | | | **40,37 $ (34,5 €)** |

- **7 rendus Seedance 2.5 pour un plan de 10 s retenu**, plus une direction complète abandonnée à 2 rendus.
- Coût du seul rendu servi : **4,62 $** — coût des 8 autres essais : **30,05 $** → **ratio 7,5×**
- Coût par seconde de film servi : **4,00 $/s**, soit **8,7× le tarif nu** de 0,462 $/s.

### 3.4 — Synthèse : que coûte une cinématique ?

**[ESTIMÉ à partir de taux d'essai MESURÉS]** Pour 50 s de cinématique en Seedance 2.5 720p 9:16 (le format du braquage, ouverture 30 s + fin 20 s) :

| Hypothèse de taux d'essai | Fondement | Coût |
|---|---|---|
| **Plancher théorique** — 0 essai, 1 appel par plan | tarif nu × 50 s | **23,10 $** (19,7 €) |
| **Basse** — 1,5 essai/plan | mesuré chaîne B (direction pré-validée par une chaîne bon marché) | **34,65 $** (29,6 €) |
| **Haute** — 7 essais/plan | mesuré chaîne C (exploration à froid) | **161,70 $** (138,1 €) |

**Le facteur 7 entre les deux bornes n'est pas du bruit : c'est une décision d'architecture de production.** Le taux d'essai dépend de la maturité de la direction artistique au moment où on engage Seedance 2.5, pas du modèle.

> **Conséquence opérationnelle directe** : dérisquer la direction artistique sur Seedance 1.0 lite (0,0371 $/s, **12,5× moins cher**) avant d'engager 2.5 divise le coût réel d'une cinématique par ~4. C'est exactement ce que la chaîne A a fait sans le formuler. Le surcoût de la carte animée (8,7× le tarif nu) est le prix de ne pas l'avoir fait.

---

## 4. Coût des fiches personnages (Nano Banana Pro)

**[MESURÉ]** Le journal contient deux fiches personnages réelles, produites le 06/08/2026. Les 8 appels de préfixe `affiche*` sont des planches promo, exclus de ce calcul.

| Personnage | Appels | Images | Sur disque | Progression observée dans les prompts | Coût [ESTIMÉ] |
|---|---|---|---|---|---|
| `illies` (`illies-fiche` → `illies-fiche7`) | **7** | **18** | 18/18 | passe 1 = création, passes 2–7 = corrections nommées (âge, proportions 7,5→7 têtes, cheveux, moustache, tache de cambouis, carnation) | **2,70 $** (2,31 €) |
| `crevette` (`crevette-fiche`) | **1** | **3** | 3/3 | convergence en une passe | **0,45 $** (0,38 €) |
| **Total** | **8** | **21** | 21/21 | | **3,15 $** (2,69 €) |

**Lecture** : le premier personnage d'une direction artistique coûte **7 passes** ; le second, une fois le style verrouillé, **1 passe**. L'écart est de **6×**.

**Coût d'un casting de 2 personnages** [ESTIMÉ] :

| Cas | Calcul | Coût |
|---|---|---|
| Style déjà verrouillé (variante de casting) | 2 × 1 passe × 3 images | **0,90 $** (0,77 €) |
| Style à créer (nouvelle expérience) | 1 × 7 passes + 1 × 1 passe | **3,15 $** (2,69 €) |
| Pire cas observé | 2 × 7 passes | **5,40 $** (4,61 €) |

**Fourchette retenue : 0,90 – 5,40 $ pour un casting de deux personnages.** C'est **négligeable** devant le coût vidéo — moins de 3 % du coût d'un maître. Une fiche personnage n'est pas un poste de coût, c'est un poste de *temps de validation humaine*.

Pour référence, l'ensemble des 160 appels Nano Banana Pro du journal (282 images, tous chantiers confondus) coûte **42,45 $ (36,3 €)**.

---

## 5. Coût marginal d'une commande

C'est la question qui décide de la grille tarifaire. Réponse courte : **hors frais de paiement, il est inférieur à un centime.**

### 5.1 — Compositing de texte : 0 €

**[MESURÉ]** `combat-3d/cinematique/montage.json` porte la contrainte, écrite noir sur blanc :

> *« AUCUN TEXTE N'EST GRAVÉ DANS LA VIDÉO. Les deux répliques sont posées en calque DOM par-dessus, aux instants `dialogues` ci-dessous : celle du plan 15 contient le PRÉNOM DU CLIENT, elle vient de `gift.config.json`. Un texte gravé obligerait à réencoder le film pour chaque commande. »*

L'invariant de la carte #1 est donc **déjà implémenté** dans le legacy, pas seulement souhaité. Le compositing est du CSS sur un `<video>`, exécuté par le téléphone du destinataire.

**Coût serveur : zéro appel fal, zéro CPU d'encodage, zéro fichier écrit.** Aucune ligne de ce poste dans le journal — et c'est précisément ce qu'on veut vérifier.

### 5.2 — Stockage R2

**[MESURÉ]** Poids réel des commandes livrées dans le legacy :

| Commande | Poids `public/` | Composition |
|---|---|---|
| `sirine-mounir` (carte) | **0,06 Mo** | config + photos + voix |
| `mohamed-lina` (carte) | **3,0 Mo** | dont **2,6 Mo de `musique.mp3`**, 0,40 Mo de souvenirs |
| `ily-driax` | **4,6 Mo** | dont **4,3 Mo de `musique.mp3`** |
| `kiwi-amel` | **5,4 Mo** | dont **4,2 Mo de `musique.mp3`** |
| `illies-crevette` (jeu sur mesure) | **16 Mo** | dont 8,9 Mo de cinématiques + 3,9 Mo d'affiche + 2,3 Mo de musique |

**Deux lectures s'imposent :**

1. **Le poids par commande est dominé par le MP3 de musique (2,3 – 4,3 Mo, soit 78–93 % du total).** La décision de la carte #1 de passer la musique par **URL YouTube** supprime ce poste. Charge résiduelle par commande = photos + audios téléversés : **0,06 à 1,0 Mo**.
2. **Les 8,9 Mo de cinématiques d'`illies-crevette` sont dupliqués par commande dans le legacy** (un dossier pnpm par cadeau). Sous l'architecture de la carte #1, ils deviennent un maître partagé — ils sortent du coût marginal et entrent dans le coût fixe.

**[ESTIMÉ]** Tarif R2 Standard, relevé le 20/08/2026 sur https://developers.cloudflare.com/r2/pricing/ :

| Poste | Tarif | Palier gratuit permanent |
|---|---|---|
| Stockage | 0,015 $ / Go-mois | **10 Go-mois** |
| Opérations classe A (écriture, liste) | 4,50 $ / million | **1 M/mois** |
| Opérations classe B (lecture) | 0,36 $ / million | **10 M/mois** |
| **Egress (sortie Internet)** | **Gratuit** | illimité |

Coût marginal de stockage d'une commande, hypothèse haute (1,0 Mo, conservé 12 mois) :

```
1,0 Mo × 12 mois × 0,015 $/Go-mois = 0,00018 $  →  0,00015 €
```

**Arrondi : 0,0002 €.** Et sous le palier gratuit, littéralement **0 €** jusqu'à ~10 000 commandes conservées un an.

Opérations : ~50 PUT à l'écriture (classe A) + ~200 GET par ouverture (classe B) →
`50 × 4,50/10⁶ + 200 × 0,36/10⁶ = 0,00030 $`. **Sous palier gratuit : 0 €.**

### 5.3 — Bande passante : 0 €, et c'est structurel

**[ESTIMÉ]** Citation verbatim de la doc Cloudflare, relevée le 20/08/2026 :

> *« Egressing directly from R2, including via the Workers API, S3 API, and r2.dev domains does not incur data transfer (egress) charges and is free. »*

**[MESURÉ]** Poids servi à l'ouverture d'une expérience :

| Expérience | Maître vidéo | + médias de la commande | Total téléchargé |
|---|---|---|---|
| Carte animée | 2,81 Mo (`depliage.mp4`) | 0,06 – 1,0 Mo | **~3 Mo** |
| Jeu braquage (par analogie combat-3d) | 10,55 Mo (ouverture + fin) | 0,06 – 1,0 Mo | **~11 Mo** |

À 1 000 ouvertures par mois d'un jeu : 11 Go de transfert → **0,00 $**.

> **C'est le fait qui rend l'invariant économique de la carte #1 vrai et pas seulement élégant.** Sur un CDN facturant l'egress (S3/CloudFront à ~0,085 $/Go), 11 Go coûteraient 0,94 $/mois et la réutilisation d'un maître aurait un coût qui croît linéairement avec les ventes. Sur R2, **elle a un coût nul**. Le choix de R2 n'est pas un détail d'infrastructure, c'est ce qui permet le modèle « générer une fois, revendre indéfiniment ».

### 5.4 — Email

**[ESTIMÉ]** Relevés du 20/08/2026 :

| Fournisseur | Palier gratuit | Coût à ~100 commandes/mois (2 emails/commande) |
|---|---|---|
| **Resend** (https://resend.com/pricing) | 3 000/mois, **plafonné à 100/jour** | **0 €** |
| **Amazon SES** à la carte (https://aws.amazon.com/ses/pricing/) | aucun palier permanent affiché | 200 emails × 0,10 $/1000 = **0,02 $/mois** → **0,0001 $/email** |
| **Postmark** (https://postmarkapp.com/pricing) | 100/mois | 15 $/mois fixe → 0,075 $/email à ce volume |

**Coût marginal retenu : 0,0002 $ par commande (0,0002 €).** Le plafond Resend de **100 emails/jour** est le vrai facteur limitant en cas de pic viral TikTok — pas le quota mensuel. À surveiller, mais sans conséquence de coût.

⚠️ La confirmation de commande par email est notée comme **jamais mise en place à ce jour** dans la carte #1. Ce poste est donc à créer, pas à migrer. Son coût de fonctionnement est nul ; son coût est un coût de développement.

### 5.5 — Le socle Cloudflare Workers : un coût **fixe**, pas marginal

**[ESTIMÉ]** https://developers.cloudflare.com/workers/platform/pricing/, relevé le 20/08/2026 :
Workers Paid = **5 $/mois plancher**, 10 M requêtes incluses, 0,30 $/M au-delà, egress gratuit, assets statiques gratuits et illimités.

| Volume mensuel de commandes | Quote-part Workers par commande |
|---|---|
| 10 | 0,50 $ (0,43 €) |
| 50 | 0,10 $ (0,09 €) |
| 100 | 0,05 $ (0,04 €) |
| 500 | 0,01 $ (0,01 €) |

À faible volume, **l'hébergement coûte plus cher par commande que tout le reste de l'infrastructure réunie** — et reste dérisoire devant le prix de vente.

### 5.6 — Frais de paiement : le seul poste marginal qui compte

**[ESTIMÉ]** https://stripe.com/fr/pricing, relevé le 20/08/2026 — carte européenne standard : **1,5 % + 0,25 €**.

| Formule | Prix | Frais Stripe | Net encaissé |
|---|---|---|---|
| Carte animée | 14,99 € | **0,47 €** | 14,52 € |
| Jeu premium | 69,99 € | **1,30 €** | 68,69 € |

⚠️ Une carte européenne **commerciale** est facturée 2,8 % + 0,25 € (1,21 € sur 14,99 €, 2,21 € sur 69,99 €). Confiance moyenne sur cette ventilation ; sans effet sur les conclusions.

⚠️ La carte #1 signale un **ancien lien Stripe à 49,99 € encore actif** pour un produit vendu 69,99 €. Ce n'est pas un problème de coût, c'est une perte de recette de **20 €/vente** — vingt fois le coût marginal total. Le corriger a plus d'impact économique que toute optimisation de rendu.

### 5.7 — Récapitulatif du coût marginal

| Poste | Nature | Coût par commande |
|---|---|---|
| Compositing de texte | [MESURÉ] calque DOM, aucun re-rendu | **0 €** |
| Rendu vidéo | [MESURÉ] maître figé, aucun appel fal par commande | **0 €** |
| Stockage R2 (12 mois) | [ESTIMÉ] 0,06 – 1,0 Mo | **0 – 0,0002 €** |
| Opérations R2 | [ESTIMÉ] ~250 ops | **0 – 0,0003 €** |
| Bande passante | [ESTIMÉ] egress R2 gratuit | **0 €** |
| Email de confirmation | [ESTIMÉ] 2 envois | **0 – 0,0002 €** |
| Quote-part Workers (à 50 cmd/mois) | [ESTIMÉ] coût fixe réparti | **0,09 €** |
| **Sous-total technique** | | **≈ 0,09 €** (dont 0,001 € vraiment marginal) |
| Frais Stripe (jeu 69,99 €) | [ESTIMÉ] | **1,30 €** |
| **Total commande jeu premium** | | **1,39 €** |
| **Total commande carte animée** | | **0,56 €** |

**Marge brute unitaire : 68,60 € sur le jeu (98,0 %), 14,43 € sur la carte (96,3 %).**

> **Le poste marginal absent de ce tableau, et c'est le seul qui compte vraiment : la porte de validation visuelle humaine avant chaque livraison**, décidée dans la carte #1. Le journal ne la mesure pas — c'est du temps humain. À 5 minutes par commande et 25 €/h chargés, elle coûte **2,08 € par commande**, soit **50 % de plus que Stripe et 2 000 fois l'infrastructure**. Toute discussion sur le coût marginal qui ignore ce poste se trompe d'ordre de grandeur. **C'est le seul coût marginal à optimiser.**

---

## 6. Coût d'une variante de casting

Définition (carte #1) : *« La relation est un axe de variantes de cinématique, pas de catalogue. Le musée reste le musée ; seul le casting du film change. »* Donc : nouvelles fiches personnages + re-rendu des cinématiques, **zéro ligne de jeu**.

**[ESTIMÉ à partir de taux MESURÉS]**

| Poste | Fondement de la mesure | Bas | Haut |
|---|---|---|---|
| Fiches personnages (2, style déjà verrouillé) | mesuré `crevette-fiche` : 1 passe | 0,90 $ | 5,40 $ |
| Re-rendu 50 s de cinématique en Seedance 2.5 | chaîne B : 1,5 essai/plan → chaîne C : 7 essais/plan | 34,65 $ | 161,70 $ |
| Décors / accessoires additionnels (Nano Banana) | mesuré `infiltration` : 7 appels = 1,05 $ | 0,00 $ | 5,70 $ |
| **Total variante de casting** | | **35,55 $** | **172,80 $** |
| **en EUR** | | **30,4 €** | **147,6 €** |

**Le cas réaliste est la borne basse.** Une variante de casting est par définition une expérience dont le décor, le découpage, le rythme et le montage sont **déjà validés** : c'est exactement la configuration de la chaîne B (1,5 essai/plan), pas celle de la chaîne C. Retenir **~35 – 60 $ (30 – 51 €)**.

> **Une variante de casting est amortie par UNE SEULE vente à 69,99 €** (68,69 € nets couvrent 30 à 51 € de coût). Même dans le pire cas modélisé (147,6 €), **3 ventes suffisent**.
>
> Réponse au point ouvert de la carte #1 (« à partir de quel signal de demande on déclenche le segment `amis` ») : **le coût n'est pas le facteur limitant.** Le seuil de déclenchement doit être fixé sur le temps humain de direction artistique et de validation, pas sur la facture fal. Une variante coûte moins cher qu'une demi-journée de travail.

---

## 7. Seuil d'amortissement d'une expérience maître à 69,99 €

### 7.1 — Coût d'un maître « braquage du musée », variante `couple`

**[ESTIMÉ à partir de postes MESURÉS sur des chantiers comparables]**

| Poste | Source de la mesure | Bas | Haut |
|---|---|---|---|
| Fiches personnages (2) | mesuré : `illies` 7 passes + `crevette` 1 passe | 0,90 $ | 5,40 $ |
| Décors, accessoires, œuvres (Nano Banana Pro) | mesuré : carte 38 appels = 5,70 $ ; `illies-crevette` 55 appels = 17,40 $ | 5,70 $ | 17,40 $ |
| Repérage / storyboard sur modèle bon marché | mesuré chaîne A : 68 appels = 13,50 – 16,39 $ | 0,00 $ (sauté) | 16,39 $ |
| Cinématiques Seedance 2.5, 50 s en 720p 9:16 | chaîne B (1,5×) → chaîne C (7×) | 34,65 $ | 161,70 $ |
| Assets 3D (tripo3d) | mesuré `infiltration` : 1 appel | 0,05 $ | 0,30 $ |
| **Total maître (IA seule)** | | **41,30 $** | **201,19 $** |
| **en EUR** | | **35,3 €** | **171,8 €** |

Point de comparaison réel, entièrement mesuré : **le maître « carte animée » a coûté 40,37 $ (34,5 €)** pour 10 s de film servi et 38 images. Un maître de jeu, avec 5× plus de vidéo, se situe dans le haut de la fourchette si l'exploration est faite à froid, dans le bas si le repérage passe par un modèle bon marché.

### 7.2 — Le seuil

Marge unitaire nette sur le jeu premium : **69,99 − 1,30 (Stripe) − 0,09 (infra) = 68,60 €**

| Scénario de production | Coût du maître | Ventes pour amortir |
|---|---|---|
| **Optimiste** — repérage sur modèle bon marché, direction verrouillée avant 2.5 | 35,3 € | **0,51 → 1 vente** |
| **Médian** — point milieu de la fourchette du §7.1 (121,2 $) | 103,5 € | **1,51 → 2 ventes** |
| **Pessimiste** — exploration à froid directement sur 2.5 (le cas mesuré de la carte) | 171,8 € | **2,50 → 3 ventes** |

> # Le seuil d'amortissement d'une expérience maître à 69,99 € est de **1 à 3 ventes**.

### 7.3 — Le même calcul pour la carte animée à 14,99 €

**[MESURÉ]** Coût du maître : **40,37 $ = 34,5 €** (chiffre réel, pas une extrapolation).
Marge unitaire : 14,99 − 0,47 (Stripe) − 0,09 (infra) = **14,43 €**.

**Seuil : 34,5 / 14,43 = 2,39 → 3 ventes.**

⚠️ **La carte à 14,99 € s'amortit moins vite que le jeu à 69,99 €**, alors que son maître coûte 2 à 5 fois moins cher. C'est mécanique : le rapport prix de vente / coût du maître est de **0,43** pour la carte contre **0,41 à 1,98** pour le jeu. À taille de maître constante, **le jeu premium est le produit qui finance la plateforme** ; la carte est un produit d'acquisition.

### 7.4 — Ce que ce seuil ne dit pas

Le seuil de 1 à 3 ventes ne couvre **que le coût de calcul**. Il ignore volontairement, faute de mesure dans le journal :

- **Le temps humain de direction artistique, d'écriture et de montage.** Le seul proxy disponible est le champ `secondes` : **5,10 h de temps machine fal cumulé sur 11 jours calendaires**. Le temps humain est de plusieurs ordres de grandeur supérieur. À 25 €/h chargés, **une seule journée de travail (≈ 200 €) coûte plus cher que le maître le plus cher modélisé ici.**
- **Le coût de développement du jeu Three.js / R3F**, hors périmètre de ce ticket.
- **Le coût d'acquisition.** La carte #1 le rappelle : les seules ventes réalisées viennent d'un TikTok à ~60 000 vues, les autres plafonnant à ~500.

> **La vraie conclusion économique n'est pas « le maître coûte 35 à 172 € ». C'est : le coût de calcul est structurellement négligeable devant le temps humain et le coût d'acquisition.** Toute décision de production doit s'optimiser sur le temps de validation humaine, jamais sur la facture fal. Le seul levier de coût de calcul qui vaille — dérisquer sur un modèle 12,5× moins cher avant d'engager Seedance 2.5 — vaut ~100 € par maître, soit environ **une heure et demie de travail humain**.

---

## 8. Réponses en une ligne aux six questions du ticket

| Question | Réponse | Nature |
|---|---|---|
| **Coût réel par cinématique produite, essais compris** | **35 – 162 $ pour 50 s** en Seedance 2.5 (nu : 23,10 $). Taux d'essai mesuré : **1,5×** avec repérage préalable, **7×** à froid | [MESURÉ] taux, [ESTIMÉ] prix |
| **Coût des fiches personnages, essais compris** | **0,45 $ par personnage** si le style est verrouillé, **2,70 $** pour le premier (7 passes mesurées). Casting de 2 : **0,90 – 5,40 $** | [MESURÉ] appels, [ESTIMÉ] prix |
| **Tarifs publics fal.ai** | Seedance 2.5 : **0,0214 $/1000 tokens** = **0,4622 $/s en 720p 9:16**, audio inclus, 480p/720p seulement, 4–30 s. Nano Banana Pro : **0,15 $/image** | [ESTIMÉ], sources primaires, 20/08/2026 |
| **Coût marginal d'une commande** | **≈ 0,001 € de technique** (compositing DOM 0 €, egress R2 0 €, stockage 0,0002 €, email 0,0002 €) + **1,30 € de Stripe**. Total **1,39 €** | [MESURÉ] poids, [ESTIMÉ] tarifs |
| **Coût d'une variante de casting** | **35 – 60 $ (30 – 51 €)** dans le cas réaliste. **Amortie par 1 vente** | [ESTIMÉ] |
| **Seuil d'amortissement à 69,99 €** | **1 à 3 ventes.** (Carte à 14,99 € : **3 ventes**) | [ESTIMÉ] |

---

## 9. Ce qui reste incertain, et de combien

| Incertitude | Amplitude | Impact sur les conclusions |
|---|---|---|
| **Taux d'essai d'un futur maître** | 1,5× à 7× — **facteur 4,7** | **Le plus gros facteur du dossier.** Ne change pas le seuil (reste 1–3 ventes) mais quadruple le coût absolu |
| Tarif Seedance 1.0 lite appliqué en août 2026 | 1,00 $/M (rerouté) ou 1,80 $/M (lite) | ±7,4 $ sur le total du journal. Non structurant |
| Tarif Seedance 2.0 *mini* — non publié | borné entre 0,49 $ et 1,21 $ pour 3 appels | ±2,2 $. Non structurant |
| Tarifs `minimax/h3` et `tripo3d` — non relevés | fourchettes larges assumées, 2 appels | ±0,85 $. Non structurant |
| Taux USD/EUR au 20/08/2026 | source secondaire, 1 USD ≈ 0,854 EUR | ±3 % → ±5 € sur un maître. Non structurant |
| **« Absent du disque » = « jeté » ?** | 198 fichiers concernés | Borne **basse** du gaspillage. Le gaspillage réel est **supérieur** à mes chiffres, jamais inférieur |
| Dimensions de sortie Seedance 1.0 lite en 1080p | 1 appel, dimensions non mesurables (fichier absent) | ±0,3 $. Non structurant |
| **Temps humain** | **totalement absent du journal** | **Domine tout le reste d'un ordre de grandeur.** Voir §7.4 |
| Palier gratuit permanent d'Amazon SES | absence constatée, pas niée par l'éditeur | Non structurant (0,02 $/mois dans tous les cas) |

---

## 10. Sources

### Journal et disque legacy — lecture seule, périmètre architecture

- `/home/fayssal/projetCadeau/outils/.fal-journal.jsonl` — 285 lignes, 06→16/08/2026
- `/home/fayssal/projetCadeau/outils/fal.mjs` — format du journal (ligne 339 : `journal({ modele, prefixe, entree, empreinte, fichiers, secondes })`)
- `/home/fayssal/projetCadeau/apps/gifts/_templates/combat-3d/cinematique/montage.json` — manifeste de montage, avertissement du 12/08/2026, contrainte « aucun texte gravé »
- `/home/fayssal/projetCadeau/apps/gifts/_templates/combat-3d/{plans,retenus,rushes,films}/`
- `/home/fayssal/projetCadeau/apps/gifts/_templates/animation-cadeau/{essais-decors/films,public/films}/`
- `/home/fayssal/projetCadeau/apps/gifts/{illies-crevette,mohamed-lina,kiwi-amel,ily-driax,sirine-mounir}/public/`

### Tarifs — sources primaires, toutes relevées le 20/08/2026

- https://fal.ai/models/bytedance/seedance-2.5/reference-to-video
- https://fal.ai/models/bytedance/seedance-2.5/image-to-video
- https://fal.ai/models/bytedance/seedance-2.0/image-to-video
- https://fal.ai/models/fal-ai/nano-banana-pro
- https://fal.ai/models/fal-ai/nano-banana-pro/edit
- https://fal.ai/models/fal-ai/bytedance/seedance/v1.5/pro/image-to-video
- https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/image-to-video (dépréciation)
- https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit
- https://developers.cloudflare.com/r2/pricing/
- https://developers.cloudflare.com/workers/platform/pricing/
- https://resend.com/pricing
- https://aws.amazon.com/ses/pricing/
- https://postmarkapp.com/pricing
- https://stripe.com/fr/pricing

### Scripts d'analyse (dans ce dépôt)

| Script | Ce qu'il produit |
|---|---|
| `scripts/analyse-journal.py` | volumétrie, appels par modèle, détail vidéo, empreintes dupliquées, présence disque |
| `scripts/analyse-projets.py` | vue par chantier × famille de modèle, détail Seedance 2.5, fiches personnages |
| `scripts/chiffrer-journal.py` | application des formules de facturation publiées, fourchettes bas/haut |
| `scripts/sonder-videos.py` | dimensions, durées et poids réels des MP4, par lecture des atomes MP4 (sans ffprobe) |

Aucun de ces scripts n'écrit dans le dépôt legacy.
