# Le Souvenir se dépose pendant le formulaire, pas au clic sur payer

Chaque Souvenir est téléversé et normalisé **au moment où l'offrant le dépose**, un par un, en tâche de fond, pendant qu'il remplit la suite du formulaire. Un brouillon de Commande existe en D1 dès le premier dépôt.

Le clic sur « payer » ne téléverse rien. Il appelle une Action qui revalide la Commande, recalcule le montant depuis la grille, horodate les cases acceptées et crée la Checkout Session — de l'ordre de deux cents millisecondes avant la redirection.

Deux horloges bornent ce qui n'est pas payé :

- un brouillon sans session Stripe est purgé à **24 h** ;
- une Commande avec session Stripe expire à **60 minutes** (`expires_at`), et non aux 24 h par défaut.

La purge ne frappe jamais une Commande dont la session Stripe est ouverte.

## Pourquoi

**Ceci retourne une conséquence écrite de la décision RGPD**, qui posait « ne téléverser les médias dans R2 qu'au clic sur payer » comme « une conséquence de conception qui ne coûte rien ». Elle coûte, et le chiffre le dit : une photo d'iPhone pèse ~3 Mo avant normalisation, une Commande au quota inclus du Jeu Premium en porte cinq et une Commande au plafond en porte dix — soit **17 à 32 Mo**, c'est-à-dire **27 à 51 secondes** en téléversement mobile à 5 Mbit/s, auxquelles s'ajoute la normalisation. Ce mur tombe à l'instant précis où l'offrant vient de décider d'acheter, et il concentre là tout le risque : si l'onglet meurt, tout le formulaire part avec lui. Le legacy a perdu une vraie vente de cette façon.

**Réparti sur dix gestes, le même temps devient invisible**, parce qu'il recouvre du temps de saisie : une photo part pendant que l'offrant tape la phrase du Souvenir suivant.

**L'échec redevient réparable.** Un téléversement raté pendant le formulaire se rejoue sur un seul Souvenir, devant quelqu'un encore présent et encore engagé.

**La normalisation parle à quelqu'un qui peut agir.** Un fichier qui ne se normalise pas est un échec technique, jamais un refus de contenu ; l'annoncer un écran avant Stripe, à quelqu'un qui a déjà décidé de payer, le place à l'endroit où il est le plus cher.

**Le dérivé existe quand le validateur arrive**, comme le contrat de Commande l'exige — un cadeau ne référence jamais le fichier téléversé.

**Ce que ça coûte, et ce qui le borne.** Des photos et des voix de personnes représentées existent désormais dans R2 pour des commandes qui ne seront jamais payées : c'est le passif que la décision RGPD voulait supprimer, et il est réintroduit sciemment. Il reste borné par ce que cette même décision tenait pour la garantie — la purge à 24 h par cron horaire, adossée au plafond `expires_at` de Stripe, avec son test d'acceptation obligatoire. On échange des heures d'exposition contre des secondes d'attente au moment d'acheter, et on resserre dans le sens protecteur la seule horloge qu'on maîtrise : personne ne revient payer une page Stripe six heures plus tard, mais soixante minutes couvrent un aller-retour vers une application bancaire pour un 3-D Secure.

## Conséquences

- **Le clic sur « payer » est court.** Aucun octet ne le traverse ; il ne porte que du calcul serveur.
- **La normalisation s'exécute au dépôt de chaque Souvenir**, avec le temps du formulaire devant elle et non la fenêtre avant Stripe.
- **Le vocal s'enregistre dans la page ; téléverser un fichier audio est le second chemin.** La borne scénique de 30 s devient une propriété de construction, et le cas dur du transcodage passe en marge.
- **Le brouillon vit en D1 avant tout paiement**, adressé par un identifiant tenu en mémoire de page. Rien n'est écrit sur le terminal : il n'y a pas de reprise de brouillon, fermer l'onglet perd le formulaire.
- **La seule reprise est le retour depuis Stripe** : `cancel_url` rouvre la Commande depuis D1 par le jeton créé avec la session.
- **La purge ne frappe jamais une Commande dont la session Stripe est ouverte**, sous peine de détruire une Commande sous les pieds de son propre paiement.
- **Déplacer le dépôt n'ouvre aucune porte de jugement avant le paiement.** On ne vérifie au dépôt que ce qui se mesure — format, taille, durée, décodabilité — et les listes closes. Le seul humain qui juge reste le validateur.
