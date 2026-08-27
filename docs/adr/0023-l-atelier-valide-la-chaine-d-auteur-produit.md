# L'atelier valide, la chaîne d'auteur produit

L'atelier est la console web sous Cloudflare Access : la file des Commandes payées, la porte de validation, la fiche d'un Cadeau. Il ne fabrique rien.

La chaîne d'auteur — fiches personnages, prompts, rendus, montage, publication d'une Expérience ou d'une variante de casting — reste une **trousse en ligne de commande sur la machine de l'auteur**, avec son journal append-only. Publier au catalogue est un **déploiement**, pas un bouton : Formules, Expériences, Emplacements et variantes de casting vivent en code. D1 ne porte que ce qui varie par Commande.

## Pourquoi

**Parce que les deux métiers ne partagent aucun runtime.** La chaîne d'auteur pilote un Chrome local par Puppeteer, capture des PNG, appelle ffmpeg. Un Worker Cloudflare ne fait tourner aucune de ces trois choses. Réunir les deux n'est pas une simplification : c'est un portage complet de la chaîne vers un runtime qui la refuse, pour un outil qu'une seule personne utilise sur sa propre machine.

**Parce qu'ils ne partagent pas non plus le mode de défaillance**, ce qui est la meilleure preuve qu'ils ne partagent pas un logiciel. L'invariant économique fige la cinématique maître et fait de la personnalisation une couche posée par-dessus : un échec de validation porte sur un Souvenir de l'Offrant et ne déclenche jamais un rendu. Le rendu raté, coûteux et rejouable n'existe que dans la chaîne d'auteur.

**Parce qu'un catalogue en base peut casser un Cadeau vivant par un `UPDATE`.** Un Emplacement retiré d'une Expérience déjà vendue laisse une personnalisation qui pointe dans le vide. En code, la porte de qualité en intégration continue attrape cela avant le déploiement, gratuitement — et le catalogue change une fois par mois, alors qu'un éditeur en base serait à écrire, à valider et à maintenir pour un seul saisisseur.

**Parce que le goulot de la chaîne d'auteur est le goût, pas le débit.** Le coût mesuré est de 4,7 € dépensés pour 1 € servi, entièrement dans les essais jetés, avec un facteur 4,7 entre l'exploration à froid et une direction déjà validée. Aucun automatisme ne fait converger un cadrage plus vite ; seule la mémoire des essais évite de les refaire.

## Conséquences

- **La planche de contrôle est la porte**, pas la relecture intégrale : chaque Souvenir montré **dans son Emplacement**, dans l'ordre de la rencontre, puis le message final. Rejouer l'expérience coûterait ses cinquante secondes de cinématiques plus le gameplay, sans survol possible, pour revoir une mise en scène identique à toutes les Commandes. Un lien « voir comme le Destinataire » reste disponible pour les cas de doute — sans lui, la planche devient la seule vérité et plus personne ne vérifie qu'elle dit vrai.
- **La planche suppose une capacité qui n'existe pas encore** : obtenir l'image fixe d'un Emplacement hors du parcours.
- **La passe est l'unité du refus, pas le Souvenir.** Le validateur marque au fil de la planche, un motif par marque parmi les quatre de l'ADR-0008, puis soumet en un geste : un seul email listant les Souvenirs refusés par leur rang. Avant la soumission tout se démarque, après plus rien — c'est la seule fenêtre de rétractation possible sans dételer l'email dû dans l'heure. Contrepartie : une passe interrompue à mi-planche se recommence.
- **La passe porte le nom de qui l'a prononcée** — l'email du jeton Access, l'horodatage, les motifs. Non par surveillance interne, mais parce qu'un acte éditorial dont l'art. 17 du DSA exige l'exposé des motifs se défend mal sans auteur, et parce qu'un second validateur rendra un jour nécessaire de comprendre pourquoi deux Commandes semblables ont reçu deux réponses différentes.
- **Trois écrans, et aucun chiffre.** La file, la recherche par email / Lien / prénom — qui est l'instrument concret du droit d'une Personne représentée à faire éteindre un Cadeau —, et la fiche d'un Cadeau avec ses trois gestes irréversibles : révoquer un Lien, en émettre un nouveau, éteindre. Un atelier qui affiche du chiffre d'affaires devient l'endroit où on regarde les ventes, et cesse d'être l'endroit où on vide une file.
- **La Validation livre.** Passe soumise sans marque, le Lien est émis et l'email part, seuls. Un second bouton « publier » fabriquerait un état validé-mais-non-livré qui n'a aucune règle et dont la seule propriété serait de retenir des Cadeaux payés.
- **Le journal append-only de la chaîne d'auteur est repris tel quel du legacy.** Reliant chaque plan à son prompt et à son modèle, il permet de rejouer un plan raté sans rejouer les treize. C'est la seule pièce de la chaîne dont la perte se paie en euros.
- **La validation des fiches personnages reste manuelle**, et se fait dans la trousse : son validateur est l'auteur devant ses rendus, jamais le validateur devant une file.
