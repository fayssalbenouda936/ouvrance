# Un plan est un appel Seedance ; un film est un montage

Une cinématique maître ne se commande pas en une passe. Elle s'écrit en plans de **4 à 8 secondes**, un plan par appel `image-to-video`, et le film est l'assemblage déterministe de ces plans — concaténation, nappe sonore continue, gel de fin — produit par la chaîne d'auteur et jamais par un modèle.

Le montage a lieu **à l'écriture**. Le lecteur ne reçoit qu'un MP4 par cinématique et par variante de casting : il tient **deux éléments `<video>`**, quel que soit le nombre de plans.

## Pourquoi

**Parce que le prix est à la seconde, pas à l'appel.** La facturation de Seedance 2.5 relevée sur les tarifs publics est `tokens = (hauteur × largeur × durée × 24) / 1024` : le coût est strictement proportionnel à la durée de sortie et il n'existe aucun forfait d'appel. Tirer 29 s en un plan ou en six coûte le même prix nu — 13,40 $. Le découpage fin est donc **gratuit**, et la formulation courante « chaque plan ajouté coûte de l'argent » est fausse : ce sont les secondes qui coûtent.

**Parce que la granularité de l'échec est le vrai coût.** Le journal de 285 appels du legacy mesure que 1,4 % des appels produisent les rendus servis : les essais jetés *sont* le coût. Un plan de 5 s manqué se re-tire pour 2,31 $ ; les 30 s d'ouverture tirées en une passe se re-tirent pour 13,87 $, parce qu'un détail faux à la seconde 22 jette les trente. Le découpage n'est pas un budget, c'est une **résolution du risque** — et c'est le même geste, à une autre échelle, que dérisquer sur un modèle 12,5× moins cher.

**Parce que la variante de casting se paie au plan.** Un plan sans personnage au cadre — des mains gantées, un objet, un décor — est partagé par toutes les variantes et ne se re-tire jamais. Un film tiré en une passe n'a pas de plan partagé : la moindre nouvelle relation le re-tire en entier. Découper, c'est isoler le casting.

**L'alternative était sérieuse.** Une passe unique donne un raccord parfait par construction, une bande son continue gratuite, et aucune étape de montage à écrire. Le legacy l'a servie ainsi depuis le 12/08/2026. Mais elle rend chaque essai indivisible, chaque variante intégrale, et elle demande au modèle de tenir seul une continuité de trente secondes — ce qu'aucune mesure ne garantit.

**Le montage doit être sonore, sinon il se voit.** Chaque appel génère sa propre bande son ; treize appels, c'est treize ambiances indépendantes qui sautent à chaque raccord. Le saut sonore désigne la couture que l'image, elle, tenait. C'est pourquoi le montage pose une nappe continue : elle n'est pas un embellissement, c'est la condition de possibilité du découpage fin.

## Conséquences

- **Aucun plan sous 4 secondes ni au-dessus de 30**, la durée demandée à Seedance 2.5 étant un entier borné. Une coupe sèche d'une seconde s'obtient **au montage, en taillant dans un plan de 4 s tiré**, jamais en commande.
- **Le maître plafonne à 720 × 1280.** Seedance 2.5 ne propose que 480p et 720p ; il n'existe pas de version 1080p sans changer de modèle.
- **Chaque plan porte une image clé** produite en amont (0,15 $), et les plans dont la première image doit être exacte — les bascules — se tirent en `image-to-video` sans exception : l'écart au raccord mesuré est de 4,2/255 contre 48,6/255 en `reference-to-video`, dont les références sont un jeu sans ordre.
- **Tout plan passe par le modèle bon marché avant le modèle cher.** Une passe complète en Seedance 1.0 lite sur un film de 61 s coûte 2,26 $ ; un seul plan de 6 s raté en 2.5 en coûte 2,77 $. La règle n'est pas de la prudence, c'est une inégalité arithmétique.
- **Le montage pose une nappe sonore continue** du premier au dernier plan, et l'audio natif de Seedance n'est conservé que sur les plans qui portent une réplique à l'image. Contrepartie : le film n'a pas de bruitage par plan.
- **La chaîne d'auteur gagne une étape et un artefact** : un manifeste ordonné de plans — identifiant, durée, prompt, blocs recollés, dépendance de casting — qui est à la fois la commande de tirage et le plan de montage. Une variante de casting est ce manifeste filtré sur les plans dépendants du casting.
- **Le lecteur tient deux éléments `<video>`**, jamais un par plan : treize décodeurs à débloquer au premier tap sont impossibles sur iOS, où une vidéo en pause retient un décodeur matériel.
- **Le dernier plan de chaque cinématique se termine sur un demi-second de plan fixe**, pour que la permutation vers le moteur se fasse entre deux images identiques et qu'un moteur en retard produise un gel plutôt qu'un trou.
