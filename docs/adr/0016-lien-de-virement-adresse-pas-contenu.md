# Le lien de virement est une adresse, pas un contenu

Le lien de virement ne fait pas partie de la Récompense. La Récompense est ce que l'offrant a **écrit** — son message, et le montant offert s'il a choisi de l'afficher. Le lien de virement se montre au même moment sans en faire partie.

Il est **facultatif** : sont obligatoires l'occasion, la relation, les prénoms et le message final, et rien d'autre. Quand il n'y en a pas, la Récompense n'en parle pas — pas de bouton inerte, pas de mention d'absence.

Il appartient au **Cadeau**, pas à la Personnalisation ni à un bloc de la Commande : le formulaire le recueille, la Commande le porte jusqu'à la Validation, le Cadeau en est propriétaire ensuite. C'est le **seul élément d'un Cadeau que l'offrant révise après la Validation**, depuis `/suivi/[jeton]`, sans repasser la porte.

Il se choisit dans une **liste close de services** : Revolut, PayPal, Lydia. `https` obligatoire, hôte égal à une valeur de la liste, aucun sous-domaine libre, aucune redirection suivie. Les hôtes exacts se recopient des documentations au moment d'écrire le schéma, jamais de mémoire.

## Pourquoi

**Parce qu'une adresse n'a pas le cycle de vie d'un contenu**, et que le cycle de vie est le critère sur lequel l'ADR-0005 a découpé la Commande. Le message et le montant s'écrivent une fois, se lisent à la Validation et meurent avec le Cadeau. Le lien de virement, lui, ne dit rien : il pointe, et il se périme. Un lien de demande Revolut vaut sept jours ; un Cadeau vit deux ans, prolongés de deux ans à chaque ouverture. Les deux seuls Cadeaux livrés qui portaient un lien le portaient sous la forme `revolut.me/p/…` et il est mort dans les deux cas. Ranger le lien avec le message parce qu'ils s'affichent au même instant, c'est refaire `GiftConfig`.

**Parce que le disque dit qu'il est facultatif.** Sur cinq Cadeaux livrés, trois ne portent aucun lien de virement, un porte un montant sans lien, et l'un des trois écrit dans son message *« J'ai pas d'argent : la carte, c'est le cadeau »*. Le formulaire du legacy marquait déjà `lien_paiement` optionnel, et marquait `montant_affiche` obligatoire alors qu'il est vide quatre fois sur cinq. Le glossaire décrivait mal ce que la production faisait déjà.

**Parce que la liste close paie la révision.** La porte de Validation existe pour ce qui se juge. Un lien de virement ne se juge pas — un domaine de collecte crédible ne se distingue pas d'un vrai en trois secondes de lecture humaine, ce qui est la raison pour laquelle il est comparé à une liste plutôt que regardé. Un champ dont la vérification est mécanique n'a rien à demander à une porte humaine. C'est ce qui autorise, pour ce champ seul, l'exception à la règle « modifier un Cadeau, c'est le re-valider ».

**Parce que Wero ne peut pas être révélé par un lien.** Le service fonctionne par numéro de téléphone et par QR code dans son application, et sa page sécurité avertit ses utilisateurs qu'un message annonçant un envoi d'argent par Wero est une arnaque et qu'il ne faut cliquer sur aucun lien. Le citer reviendrait à révéler, au pic émotionnel, un lien que Wero apprend par ailleurs à ne pas ouvrir.

**Ce que ça coûte, et qui est assumé** : ouvrance perd « cadeau en argent mis en scène », la description la plus courte et la plus vendeuse de ce qu'elle fait. Elle garde « votre argent ne passe jamais par nous », qui cesse d'être une accroche pour devenir une promesse — et qui gagne en force à ne plus vendre.

## Conséquences

- **`CONTEXT.md` change en trois endroits** : le paragraphe d'ouverture ne dit plus « transforme un cadeau en argent en expérience numérique », l'entrée **Récompense** perd le lien de virement, l'entrée **Lien de virement** gagne son caractère facultatif, son rattachement au Cadeau et sa liste close.
- **La colonne s'appelle `lien_virement`.** Le glossaire réserve le mot *paiement* à l'achat d'une Commande par l'offrant à ouvrance ; `paymentUrl` et `lien_paiement` sont des violations de vocabulaire.
- **La Récompense a deux mises en page**, et celle avec lien n'est pas une version enrichie de l'autre : le message est composé pour tenir seul, le lien s'y ajoute sans que la composition en dépende.
- **`/suivi/[jeton]` devient une surface d'écriture** — un champ, contre la même liste close, notifié à l'offrant par email à chaque changement, l'ancienne valeur conservée en trace et détruite à l'Extinction.
- **Le jeton de suivi décide désormais où va l'argent.** Le dégât est borné par la liste close — un détournement ne peut viser qu'un autre compte des services acceptés — et rendu visible par la notification. Ce n'est pas une clôture du sujet.
- **Le prix ne dépend pas de ce qui est joint.** Une Formule, un prix, avec ou sans lien de virement : le contraire ferait dépendre le tarif d'ouvrance de ce qu'elle ne fournit pas et n'encaisse jamais.
- **Les mentions légales et la FAQ en production sont fausses** : elles nomment Wero et écrivent « ou toute autre URL ».
