# On budgète sur l'appareil qu'on n'a pas mesuré

Le budget de performance d'ouvrance se calcule sur un **Samsung Galaxy A17** — Exynos 1330, Mali-G68 MC2, 4 Go, écran 1080 × 2340. La **conformité média** — déblocage par élément, absence de plein écran, tampons purgeables, absence de verrou d'orientation — continue de se juger sur iPhone.

Deux appareils de référence, deux rôles distincts, et le premier n'a jamais été branché.

## Pourquoi

**Parce que le Destinataire ouvre le Lien sur son téléphone à lui.** Personne ne le choisit, et il n'y a pas de compte pour le connaître à l'avance. StatCounter donne 65 % d'Android en France en mars 2026 ; le seul segment où iOS passe devant est celui des 18-24 ans, à 52 %. Un budget calculé sur iOS est un budget calculé sur un tiers du parc.

**Parce que les deux familles ne font pas peser le même genre de risque.** Sur iOS les contraintes sont *comportementales* — un `<video>` se débloque par élément, il n'existe pas de plein écran composable, un élément en pause et caché voit ses tampons marqués purgeables. Elles ne dépendent d'aucun chiffre, la sonde #17 les a relevées, et elles valent pour tous les iPhone. Sur Android elles sont *quantitatives* — mémoire, GPU, thermique — et personne n'a rien mesuré. Le budget est un objet quantitatif : il appartient au côté quantitatif.

**Parce que budgéter sur le haut de gamme mesuré aurait été pire que de ne pas budgéter.** La sonde a relevé 1920 Mo d'allocation JS sur un iPhone 17 Pro Max et recommandait de retomber sur les 840 Mo du repli codé en dur dans WebKit, soit ≈ 400 Mo d'empreinte. Ce repli prévient avant de reprendre ; Chrome sur un Android à 4 Go ne prévient pas, il tue l'onglet. Un chiffre confortable adossé au mauvais moteur donne l'illusion d'un budget.

**Parce que l'appareil coûte moins cher qu'un rendu raté.** Le Galaxy A17 est à ~135-151 € et c'est le best-seller entrée de gamme en France. Un maître Seedance coûte 35-160 $ (#5). L'argument du prix ne se plaide pas.

## Conséquences

- **250 Mo d'empreinte totale**, textures et tampons vidéo compris — et non 400. C'est une **hypothèse de travail, pas un relevé**, et elle le reste tant que la sonde n'a pas tourné sur l'A17.
- **30 images/s au 95e centile de trame**, pas en moyenne : sur un FPS à visée manuelle (#8), c'est la trame longue isolée qui fait rater un tir.
- **Un seul levier de dégradation, continu et automatique** : le `renderScale` entre 1,0 et 0,5, asservi au framerate mesuré, ombres et post-traitement au même seuil. Pas de profils — un profil est un second chemin de rendu à valider en double à la porte de #16, où une seule personne regarde chaque Cadeau.
- **Aucun refus d'appareil.** Un Destinataire qui tombe sur « votre téléphone ne suffit pas » est un cadeau raté, et c'est l'Offrant qui a payé.
- **Les budgets statiques vivent dans la bande** (ADR-0021) et cassent la **porte de publication**, pas d'abord la CI : c'est là qu'un maître hors budget arriverait, et un maître n'entre pas par un commit. Cadeau complet ≤ 20 Mo pour le braquage, ≤ 8 Mo pour la carte animée.
- **Les budgets dynamiques n'ont pas de dents** : framerate et empreinte partent par le canal anonyme de #18 — aucun identifiant, aucune écriture sur le terminal, aucun outil tiers — et ne produisent qu'un rapport. Ils ne tiennent que si quelqu'un le lit.
- **Une sonde Android est due**, et c'est la dette explicite de cette décision. Le ticket #43 ne la couvre pas : il ne mesure que les quatre WebViews iOS.
