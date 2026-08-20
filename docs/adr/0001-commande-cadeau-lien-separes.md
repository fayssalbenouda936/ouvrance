# Commande, Cadeau et Lien sont trois entités distinctes

Le legacy confondait les trois : une commande *était* le cadeau, et son URL en était un champ. Nous les séparons — la **commande** est l'achat côté offrant, le **cadeau** est l'expérience personnalisée validée et publiée, le **lien** est l'adresse révocable qui y mène.

## Pourquoi

Trois raisons, chacune suffisante seule :

- **Le cadeau naît de la validation, pas du paiement.** La porte de validation humaine est obligatoire avant chaque livraison. Avec un objet unique, cet intervalle n'existe que comme un booléen ; avec deux objets, une commande payée non validée est simplement une commande sans cadeau.
- **La purge RGPD devient triviale.** Une commande jamais payée n'a pas de cadeau : il n'y a rien à révoquer, seulement des fichiers à effacer. Aucune logique de suppression n'a à distinguer « livré » de « pas encore livré » sur un même objet.
- **Un lien est révocable, un cadeau ne l'est pas.** L'offrant peut renvoyer, faire expirer ou remplacer l'adresse sans que le cadeau change. Un même cadeau porte plusieurs liens au fil du temps.

## Ce que ça coûte

Trois types à faire vivre au lieu d'un, et deux jointures pour remonter d'un lien à l'offrant. Accepté : le legacy prouve qu'un objet unique finit par mélanger l'état d'achat et l'état de livraison dans les mêmes champs.
