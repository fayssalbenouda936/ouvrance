# La Formule est un palier tarifaire, l'Expérience est son contenu

Le catalogue a deux niveaux : une **formule** fixe un prix et un quota de médias, une **expérience** est ce que le destinataire vit. Une formule ouvre l'accès à une ou plusieurs expériences. Aujourd'hui chacune n'en contient qu'une — c'est délibéré, pas une erreur de modélisation.

## Pourquoi

Parce que **ajouter une expérience ne doit pas ajouter un prix**. Le catalogue plat — une expérience porte son propre prix — était plus simple et a été écarté : il fait de chaque nouveau jeu une décision tarifaire, alors que l'ambition est d'accumuler des expériences sous un palier Premium déjà vendu 69,99 €.

## Conséquences

- Le **quota** de médias vit sur la formule et sur elle seule. La promesse client est à un seul endroit.
- En contrepartie, **toute expérience publiée sous une formule doit pouvoir absorber le plafond de cette formule** — disposer d'au moins autant d'emplacements substituables que la formule vend de médias. C'est une contrainte de conception sur les expériences, pas une exception à gérer à la commande, et il revient à l'atelier de ne publier que des expériences conformes.
- Cette contrainte est faible en pratique, parce que les emplacements portent un **contenu par défaut** : la galerie du braquage expose des œuvres, et la personnalisation en remplace un sous-ensemble. Ajouter des emplacements substituables coûte donc peu — c'est le plancher, pas le plafond, qui contraint réellement la conception (voir ADR-0003).
