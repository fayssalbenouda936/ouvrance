# Le contrat de Commande : trois blocs, dont un seul est propre à l'expérience

Ce que l'offrant remplit n'est pas un objet, c'est trois :

- **Ce qui choisit** — occasion, relation, prénoms. La relation sélectionne la variante de casting, donc elle sélectionne un fichier vidéo.
- **Ce qui se rencontre** — la Personnalisation, c'est-à-dire la liste ordonnée de Souvenirs, et rien d'autre.
- **Ce qui conclut** — la Récompense : message, montant, et ce que l'ADR à venir sur le lien de virement y ajoutera.

Le noyau de lecture connaît le premier et le troisième. Il ne connaît **jamais** le deuxième : le schéma de la Personnalisation est propre à chaque expérience, enregistré par elle dans un **registre** indexé par son identifiant au catalogue. Une Commande se valide donc en deux temps — les blocs communs d'abord, strictement typés ; la Personnalisation ensuite, résolue par le registre.

Les médias d'un Cadeau sont des **dérivés normalisés, figés à la Validation**. Un Cadeau ne référence jamais le fichier téléversé.

## Pourquoi

**Trois blocs plutôt qu'un**, parce que les trois n'ont pas le même cycle de vie. La relation est immuable dès le paiement — elle a choisi un maître. Un Souvenir reste modifiable jusqu'à la Validation. Un objet plat mélange les deux et rejoue `GiftConfig`, l'interface legacy qui accumulait un champ optionnel par expérience (`lettre?`, `combat?`, `convoyage?`) jusqu'à ce que plus personne ne sache ce qu'une commande contenait vraiment.

**Un registre plutôt qu'une union discriminée.** L'union est exhaustive par construction, ce qui est un vrai bénéfice : on ne peut pas oublier une expérience. Mais elle impose un fichier central qui importe le schéma de chacune — donc la troisième expérience modifie le noyau, exactement ce que l'architecture du lecteur cherche à éviter. Le registre déplace l'exhaustivité du compilateur vers la publication au catalogue : une expérience dont l'identifiant n'a pas de schéma enregistré ne se publie pas. On échange une garantie statique contre une porte de publication, et cette porte existe déjà.

**Des dérivés figés**, parce que l'alternative est pire qu'elle n'en a l'air. Si un Cadeau lit l'original, il faut le re-valider à chaque lecture et savoir quoi faire d'un média devenu invalide *pendant une partie*. En lisant un dérivé produit une fois, le cas disparaît : la Validation est un événement daté, pas un contrôle permanent, et le lecteur lit un manifeste déjà vrai. C'est aussi ce qui absorbe le HEIC de l'iPhone et les trois conteneurs audio que produisent les navigateurs, sans que l'expérience ait à les connaître.

## Conséquences

- **`Commande` remplace `GiftConfig`.** Le bloc de personnalisation y est `unknown` tant que le registre ne l'a pas résolu ; aucun `any`, aucun champ optionnel par expérience.
- **Le noyau est générique sur la Personnalisation** et ne la nomme jamais. C'est le joint : une expérience apporte son schéma et son lecteur, le noyau apporte le reste.
- **Modifier un Souvenir après livraison n'est pas une édition, c'est une re-validation.** Il n'existe pas de chemin qui change un Cadeau sans repasser la porte.
- **La normalisation est une étape du dépôt**, pas de la lecture : une seule forme stockée par média.
- **Une expérience ne se publie qu'avec un schéma enregistré.** La publication au catalogue porte la vérification que le compilateur ne fait plus.
- **Bornes d'entrée** : images JPEG, PNG, WebP, HEIC ; tout audio que le navigateur sait produire ; 25 Mo par fichier ; vocal de 30 s maximum. La borne du vocal est scénique, pas technique — un vocal se déclenche à l'approche, et personne ne reste une minute devant un cadre.
- **Le cas zéro reste payable.** Sont obligatoires : occasion, relation, prénoms, message final. Tout le reste est facultatif, Souvenirs compris.
