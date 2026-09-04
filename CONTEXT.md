# ouvrance

ouvrance met en scène ce qu'on offre. L'offrant achète une formule, la personnalise et reçoit un lien à transmettre ; le destinataire ouvre le lien, vit l'expérience et découvre à la fin la récompense — le message de l'offrant, et son lien de virement s'il en a joint un. L'argent, quand il y en a, ne transite jamais par la plateforme.

Ce fichier est un glossaire et rien d'autre : aucun détail d'implémentation, aucune spécification.

## Language

### Le catalogue

**Formule** :
Un palier tarifaire du catalogue. Elle fixe le prix d'entrée, le quota de Souvenirs et le prix du supplément, et ouvre l'accès à une ou plusieurs expériences.
_Avoid_ : produit, offre, pack, forfait

**Expérience** :
Ce que vit le destinataire quand il ouvre le lien. Elle appartient à une formule et existe indépendamment de toute commande. Une expérience est de nature *carte* ou de nature *jeu* — une carte n'est pas un jeu sans gameplay.
_Avoid_ : cadeau, template, jeu (comme terme générique), gift

**Cinématique maître** :
Le rendu vidéo figé d'une expérience, produit une fois par la chaîne d'auteur et rejoué à l'identique pour toutes les commandes.
_Avoid_ : rendu, vidéo, master, cinématique (employé seul)

**Variante de casting** :
La déclinaison d'une cinématique maître selon la relation représentée. Le scénario, les décors et le gameplay ne changent pas ; seuls les personnages à l'écran changent.
_Avoid_ : version, déclinaison, variante (employé seul)

**Emplacement** :
Une place, prévue par la mise en scène d'une expérience, où un Souvenir de l'offrant peut apparaître — un mur du musée, un polaroïd sur la page de droite de la lettre. Là où la mise en scène est fixe, un emplacement est toujours occupé : il porte un contenu par défaut qu'un Souvenir vient remplacer. Là où elle s'adapte, un emplacement sans Souvenir n'apparaît pas. Jamais de trou dans les deux cas. C'est une capacité de mise en scène, à ne pas confondre avec le quota.
_Avoid_ : slot, champ, zone

**Contenu par défaut** :
Ce qu'un emplacement montre quand aucun Souvenir ne le remplace — une œuvre du musée, une réplique neutre. Il n'est pas un repli de secours : c'est l'état normal de l'expérience, et la personnalisation est ce qui s'y substitue.
_Avoid_ : fallback, placeholder, remplissage

**Quota** :
Le nombre de Souvenirs qu'une formule inclut, et le plafond qu'elle autorise contre supplément. C'est une promesse commerciale, portée par la formule et par elle seule.
_Avoid_ : limite, capacité

**Supplément** :
Un Souvenir au-delà du quota inclus, facturé au moment de la commande.
_Avoid_ : option, extra, devis

**Occasion** :
L'événement que le cadeau célèbre. N'affecte que les mots affichés, jamais la mise en scène ni le casting. Aucune fête religieuse, d'aucune confession.
_Avoid_ : événement, thème

**Relation** :
Le lien entre l'offrant et la personne représentée. Choisit la variante de casting.
_Avoid_ : type de cadeau, cible

### Les personnes

**Offrant** :
La personne qui achète une commande, la personnalise et transmet le lien. Le seul client d'ouvrance.
_Avoid_ : acheteur, client, utilisateur, offreur

**Destinataire** :
La personne qui ouvre le lien et vit l'expérience. N'a pas de compte.
_Avoid_ : receveur, bénéficiaire, joueur

**Personne représentée** :
Toute personne dont le visage ou la voix figure dans un cadeau. Souvent le destinataire, pas toujours. N'a aucune relation avec ouvrance et n'a rien consenti : c'est sur elle que porte la déclaration de l'offrant.
_Avoid_ : tiers, sujet, figurant

### De l'achat à la livraison

**Commande** :
L'achat, côté offrant : une formule, une expérience, une personnalisation, un paiement. Elle existe dès le formulaire, avant tout paiement.
_Avoid_ : achat, panier, instance, gift

**Personnalisation** :
La liste ordonnée de Souvenirs que l'offrant pose par-dessus une cinématique maître, et l'ordre est celui de la rencontre. Elle ne modifie jamais le maître. Sa forme est propre à chaque expérience.
_Avoid_ : config, options, contenu

**Souvenir** :
L'unité de personnalisation, la même pour toute expérience : un support — une photo **ou** une phrase, jamais les deux — et, facultativement, une greffe. C'est ce que l'offrant dépose, ce que le destinataire rencontre, et ce que la personnalisation ordonne.
_Avoid_ : média, souvenir (employé seul pour désigner un fichier), item

**Greffe** :
Ce qui s'attache à un support sans le remplacer ni devenir un Souvenir à part. Sa forme appartient à l'expérience : un vocal entendu à l'approche dans le braquage, une légende manuscrite sous le polaroïd dans la carte animée. Une greffe n'existe jamais seule.
_Avoid_ : annotation, légende (comme terme générique), vocal (comme terme générique)

**Paiement** :
L'achat d'une commande par l'offrant à ouvrance. Rien d'autre ne s'appelle un paiement.
_Avoid_ : virement, transaction

**Date promise** :
La date à laquelle un cadeau sera livré, calculée avant le paiement sur les jours d'ouverture de l'atelier et figée au paiement. C'est une date et jamais une durée, un engagement et jamais une estimation. Rien de ce qu'ouvrance ne contrôle pas ne la repousse : un souvenir refusé ne la décale pas, il sort du cadeau.
_Avoid_ : délai, ETA, estimation, date de production

**Validation** :
L'examen humain d'une commande payée avant qu'elle ne devienne un cadeau. Obligatoire, sans exception.
_Avoid_ : contrôle, review

**Livraison** :
Le nom que le contrat donne à la validation, vue depuis l'offrant : l'instant où le lien lui est remis. Validation et livraison sont le même instant — le premier mot est celui de l'atelier, le second celui des conditions de vente — et rien ne s'intercale entre eux.
_Avoid_ : envoi, expédition, délivrance, mise à disposition

**Cadeau** :
L'expérience personnalisée, validée et publiée, prête à être vécue. Un cadeau naît de la validation, pas du paiement.
_Avoid_ : commande, livraison, instance

**Lien** :
L'adresse par laquelle un destinataire atteint un cadeau. Révocable ; un même cadeau peut en porter plusieurs au fil du temps.
_Avoid_ : URL, jeton, token

**Rétractation** :
L'annulation d'une commande par l'offrant, sans motif et remboursée intégralement, ouverte jusqu'à la livraison. Elle porte sur une commande et ne détruit rien, là où l'extinction détruit un cadeau déjà vécu et ne rembourse qu'au prorata.
_Avoid_ : annulation, remboursement, résiliation, rétraction

**Extinction** :
La destruction des dérivés d'un cadeau et de tout ce qui le décrit — ses phrases, son message, son lien de virement. Elle révoque tous ses liens et ne se défait pas. À distinguer de la révocation d'un lien, qui ne détruit rien et laisse le cadeau vivant.
_Avoid_ : suppression, purge (pour un cadeau), désactivation, retrait

**Récompense** :
Ce que le cadeau révèle à la fin : le message de l'offrant, et le montant offert s'il a choisi de l'afficher. Le message est le seul contenu qu'un destinataire reçoit à coup sûr. Le lien de virement se montre au même moment sans faire partie de la récompense — c'est une adresse, pas un contenu. Dans le braquage, la récompense est l'œuvre dérobée.
_Avoid_ : reveal, écran de fin, cagnotte

**Lien de virement** :
L'adresse de virement de l'offrant, facultative, montrée au destinataire au moment de la récompense. Elle appartient au cadeau et non à la personnalisation : elle se périme, et c'est le seul élément d'un cadeau que l'offrant révise après la validation, sans en repasser la porte. Elle se choisit dans une liste close de services. ouvrance la montre et ne l'encaisse jamais.
_Avoid_ : cagnotte, don, paiement, transfert, lien de paiement

### La production

**Atelier** :
La console interne où le catalogue se publie et où les commandes passent la validation. Elle ne fabrique pas les cadeaux.
_Avoid_ : admin, back-office, studio

**Chaîne d'auteur** :
La production d'une nouvelle expérience : fiches personnages, prompts, rendus, montage, publication au catalogue. Se distingue du traitement d'une commande, qui n'appelle jamais un modèle génératif.
_Avoid_ : pipeline, production, génération
