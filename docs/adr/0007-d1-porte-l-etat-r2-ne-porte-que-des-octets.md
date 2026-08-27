# D1 porte l'état, R2 ne porte que des octets

L'état de la plateforme — Commande, Paiement, Validation, Cadeau, Lien, et le manifeste des dérivés — vit dans une base **D1**, interrogée par Drizzle. R2 ne stocke plus que des octets : téléversements d'origine et dérivés normalisés.

Ces octets se servent de **deux façons**, et la coupure suit une ligne du domaine :

- **Ce qui appartient à la cinématique maître** — rendus, modèles, textures — est identique pour toutes les commandes d'une expérience et ne contient rien de personnel. Servi depuis un **domaine R2 public**, noms hachés, `immutable`, mis en cache par le CDN.
- **Ce qui appartient à la Personnalisation** — les dérivés des Souvenirs de l'offrant — est personnel et doit mourir avec le Lien. Servi par un **Worker qui vérifie le Lien dans D1**, puis streame depuis R2 avec `Range`.

## Pourquoi

**Parce que le domaine est relationnel et que les requêtes sont réelles.** « Les commandes payées en attente de validation » est l'écran principal de l'atelier. « Ce lien est-il révoqué » est sur le chemin critique de chaque ouverture de cadeau, et un Cadeau peut porter plusieurs Liens au fil du temps. « Les commandes non payées de plus de 24 h » est le cron qu'impose le RGPD. Aucune des trois ne se fait bien en scannant un bucket — et c'est ce que faisait le legacy, où l'atelier listait mille objets puis les lisait un par un, et où le pont « intention Stripe → commande » était un fichier écrit à la main sous `index/stripe/`. Ce pont devient une colonne.

**Parce que Postgres depuis un Worker demande Hyperdrive.** Une pièce mobile de plus, pour un volume qui tient dans SQLite avec trois ordres de grandeur de marge. Le choix se paie en portabilité ; il s'achète en simplicité de runtime, puisque la base est un binding comme le bucket.

**Parce que servir tous les médias de la même façon se trompe sur les deux.** Mettre la cinématique maître derrière un Worker, c'est payer une latence par requête sur les octets les plus lourds, ceux qui sont sur le chemin critique du préchargement séquentiel qu'impose iOS — pour protéger ce qui n'est secret pour personne. Et servir les dérivés de Souvenirs depuis une adresse publique, c'est rendre la révocation d'un Lien décorative : le lien ne mène plus nulle part, les photos de l'offrant restent atteignables. Les dérivés sont petits — une photo normalisée, un vocal de trente secondes — donc le Worker qui les garde ne coûte rien.

## Conséquences

- **R2 cesse d'être une base de données.** Plus de `commande.json` faisant foi, plus d'index écrits à la main, plus de liste de bucket sur un chemin de lecture.
- **Les sauvegardes deviennent une obligation, pas une hygiène** : une commande payée perdue est un remboursement. Time Travel de D1 comme filet principal, plus un export hebdomadaire vers R2 déclenché par le même Cron Trigger que la purge — parce qu'une copie hors du service qu'on restaure coûte dix lignes.
- **La révocation d'un Lien est réelle**, puisqu'elle passe par la seule porte qui sert les dérivés personnels.
- **Les assets d'expérience sont adressés par empreinte**, donc immuables et cachables sans invalidation : publier une nouvelle cinématique maître, c'est publier une nouvelle adresse.
- **Une base de développement distincte de la production**, et le partage état/octets vaut aux deux.
