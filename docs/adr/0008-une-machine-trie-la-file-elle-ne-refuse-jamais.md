# Une machine trie la file de validation, elle ne refuse jamais un Souvenir

La Validation humaine est la seule porte de jugement sur ce qu'un Offrant dépose. Aucun classifieur, aucun service de modération, aucun modèle ne prononce de refus — ni au dépôt, ni avant le paiement, ni à la Validation. Le jour où le volume l'exigera, une machine pourra **ordonner** la file ; le refus reste humain.

Un refus porte sur un **Souvenir**, jamais sur une Commande : le Souvenir sort de la liste ordonnée, son emplacement retombe sur son contenu par défaut, et le Cadeau est livrable.

## Pourquoi

**Parce que la porte humaine existe déjà et voit tout.** Un filtre en amont n'améliore pas la détection — il change seulement qui prononce le refus. Or les deux prononcés n'ont pas le même coût d'erreur. Un faux positif de tri coûte un ordre de lecture. **Un faux positif de refus accuse un client au moment exact où il paie**, seul devant un formulaire, sans personne en face. Et les classifieurs de contenu se trompent très précisément sur les occasions d'ouvrance : une naissance, c'est un nourrisson ; un mariage, c'est une plage et des épaules nues.

**Parce qu'un service de modération est un destinataire de plus pour tous les visages du produit**, dont aucun n'appartient à quelqu'un qui ait consenti à quoi que ce soit. Cela ajoute une finalité, un sous-traitant à contracter, une ligne à l'AIPD obligatoire avant la première vente, une ligne à la politique de confidentialité, et très probablement un transfert hors UE — pour un risque que quatre commandes n'ont pas encore produit.

**Parce que le seul outil automatique au profil de faux positifs acceptable ne voit rien de ce qui compte.** L'analyse CSAM de Cloudflare est gratuite sur tous les forfaits et ne juge pas : elle compare des empreintes floues à une base connue. Mais elle traite **les images qui entrent dans le cache de Cloudflare**, alors que les dérivés de Souvenirs sont servis par un Worker en `Cache-Control: private, no-store` précisément pour que révoquer un Lien révoque les photos, et que le cache est réservé à la cinématique maître. Les seules images mises en cache sont celles que personne ne téléverse. Faire passer les dérivés par le cache pour l'activer rendrait la révocation décorative — le défaut exact que l'ADR-0007 corrigeait.

**Parce que le refus par Souvenir découle de l'ADR-0003.** Une expérience tient debout avec zéro personnalisation et un emplacement vide n'existe pas. Refuser une Commande entière fabriquerait un cas — le client payé, non livré, en attente d'arbitrage — que l'architecture avait déjà supprimé.

## Conséquences

- **Le seuil est nommé et calculé** : environ vingt Commandes par jour, six cents par mois, sur la base de trois à cinq minutes de validation au plafond de dix Souvenirs — dont le vocal de trente secondes, seul média qu'on ne peut pas survoler. Au-delà, un second validateur humain d'abord ; un tri automatique ensuite ; jamais un refus automatique.
- **La borne de trente secondes du vocal (ADR-0005) est aussi le budget de modération du produit.** L'allonger allonge la porte.
- **Les motifs de refus sont une énumération fermée de quatre valeurs**, publiée dans la clause « usages interdits » des CGV et reprise telle quelle dans l'exposé des motifs dû par l'art. 17 du DSA. Pas de champ libre : ce qui se compte et ce qui se rédige ne se mélangent pas.
- **L'exposé des motifs indique qu'aucun moyen automatisé n'est intervenu.** L'art. 17 exige la mention ; ne pas automatiser la rend vraie sans effort.
- **Un Souvenir refusé ouvre sept jours pour un remplacement**, qui repasse la porte entière comme une re-validation. Passé ce délai, le Cadeau part sans lui : le silence vaut renoncement. Seul le supplément est remboursé ; le quota est un plafond, pas une promesse de contenu.
- **Le délai de livraison annoncé ne vaut que pour la première passe de Validation**, et les CGV doivent l'écrire.
- **La porte humaine coûte l'immunité d'hébergeur** : un examen préalable n'est ni automatique ni passif, donc ouvrance répond de ce qu'elle publie comme un éditeur. Le prix étant payé de toute façon, il faut en prendre le bénéfice — c'est-à-dire refuser réellement.
- **La disponibilité d'une personne devient un passage obligé du délai de livraison**, et le seul point de défaillance unique du produit vendable.
