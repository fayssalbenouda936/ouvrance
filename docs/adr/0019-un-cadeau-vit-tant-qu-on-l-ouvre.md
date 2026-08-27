# Un Cadeau vit tant qu'on l'ouvre

Un **Cadeau** est éteint **deux ans après sa dernière ouverture** — et deux ans après sa **Validation** s'il n'a jamais été ouvert. Chaque ouverture repart pour deux ans. Une colonne dans D1, écrasée, initialisée à la Validation. Elle s'écrit sur l'appel `commencer` — le tap du Destinataire — **jamais sur le `GET` du document** : les robots d'aperçu de WhatsApp, iMessage et Signal récupèrent l'URL pour fabriquer leur carte, et prolongeraient sinon un Cadeau de deux ans à chaque partage.

Le téléversement d'origine est détruit **dès que la Validation a rendu son verdict**, quel que soit le verdict. Le Cadeau ne référence que le dérivé normalisé (ADR-0005) : après le verdict, plus aucun code ne lit l'original.

Deux gestes distincts, et il faut les deux :

- **Révoquer un Lien** est un geste d'adressage. Le Cadeau vit, ses dérivés aussi, un nouveau Lien peut être émis. Réversible.
- **Éteindre un Cadeau** révoque tous ses Liens et détruit ses octets dans R2, ainsi que tout ce qui le décrit dans D1 — phrases des Souvenirs, message de la Récompense, prénoms, lien de virement. Irréversible.

**La révocation d'un Lien n'efface rien, donc elle ne répond jamais à une demande d'effacement.**

## Pourquoi

**Parce que « à vie » n'est pas une durée.** L'article 5 §1 e) du RGPD exige une durée « limitée » ; l'infini n'en est pas une. Et le jour où l'on purge quoi que ce soit, « à vie » devient une pratique commerciale trompeuse au sens de l'article L121-2 du Code de la consommation, la durée du service étant une caractéristique essentielle. Publier « à vie » et purger à douze mois est le pire des deux mondes.

**Le coût de stockage n'entre pas dans la balance.** Un Cadeau pèse ~1,5 Mo de dérivés (~4 Mo au plafond de dix emplacements). R2 facture 0,015 $ par Go-mois, sortie gratuite, dix premiers gigaoctets offerts : il faut ~5 000 Cadeaux vivants simultanés pour dépasser le palier gratuit, et 100 000 Cadeaux coûteraient 3 $ par mois. Ce que « à vie » coûte est une exposition, pas une facture : des visages et des voix de personnes qui n'ont rien consenti, gardés sans terme, chacun étant un référé de l'article 9 du Code civil ou une infraction à l'article 226-8 en puissance.

**Une fenêtre glissante plutôt qu'une durée fixe**, parce que la durée fixe produit le pire moment client possible : un cadeau rouvert chaque année meurt à une date que personne ne lui a annoncée. La fenêtre glissante aligne la conservation sur l'usage réel — on garde ce qui sert, on jette ce qui ne sert plus, et c'est la machine qui constate.

**Deux ans plutôt que douze mois**, contre la proposition de la recherche RGPD. Le raisonnement de minimalité — « le plus petit nombre qui couvre exactement un anniversaire » — est juste quand la conservation n'est qu'un passif. Il se retourne ici : la finalité est d'être rouvert, donc la durée nécessaire est celle qui sert la réouverture. Un cadeau offert en décembre et rouvert le décembre suivant se présente au jour 365 : douze mois tue les cadeaux le jour exact où ils comptent.

**L'original meurt tôt parce qu'il ne sert plus rien et coûte le plus.** Les originaux pèsent dix fois les dérivés et portent l'EXIF — coordonnées GPS, modèle d'appareil, horodatage — que la normalisation supprime. Les garder, c'est garder la géolocalisation d'une personne qui n'a rien consenti, pour un fichier que personne ne lira. Le bénéfice écarté — re-normaliser sans redemander le fichier — est mince : la chaîne de normalisation changera trois fois dans la vie du produit, et modifier un Souvenir après livraison est déjà une re-validation qui apporte son propre dépôt (ADR-0005).

## Conséquences

- **« En ligne à vie » sort du vocabulaire d'ouvrance.** Le microtexte devient « Un simple lien à partager · en ligne tant qu'on l'ouvre ». Le libellé long, pour la FAQ et les CGV : « Votre cadeau reste en ligne tant qu'on l'ouvre : chaque ouverture le prolonge de deux ans. S'il reste deux ans sans être ouvert, nous vous prévenons par email avant de le retirer — il suffit de l'ouvrir pour le garder. »
- **Un seul rappel, à J-30, à l'Offrant** — la seule adresse que la plateforme détienne, le Destinataire n'ayant pas de compte. Il ne porte aucun mécanisme nouveau : il porte le Lien du cadeau, et l'ouvrir suffit à le prolonger.
- **Deux délais de destruction, parce que les causes ne se valent pas.** Extinction demandée — tiers, Offrant, contenu illicite : hors ligne dans la seconde, octets détruits sous vingt-quatre heures, aucun sursis. Extinction par inactivité : hors ligne à l'échéance, octets détruits trente jours plus tard. **Ce sursis ne se publie pas** : le publier déplacerait la falaise à deux ans et un mois.
- **L'adresse d'un Lien révoqué n'est jamais réémise.** Sa ligne reste en D1 comme pierre tombale : un 404 est indiscernable d'une faute de frappe, et réutiliser une adresse ressusciterait l'accès pour quiconque détient l'ancienne. Deux phrases distinctes — « Ce lien n'est plus valable, demandez le nouveau lien » pour un Cadeau vivant, « Ce cadeau n'est plus en ligne » pour un Cadeau éteint. **La page ne dit jamais qu'un tiers a demandé le retrait** : l'écrire apprendrait au Destinataire quelque chose sur une personne qui vient d'exercer un droit.
- **Le Worker de dérivés répond en `Cache-Control: private, no-store`.** Sans quoi un Lien révoqué laisse les photos servies depuis le cache du téléphone, et la révocation redevient décorative — le défaut même que l'ADR-0007 corrigeait en refusant l'adresse publique. Coût : ~1,5 Mo re-téléchargés à chaque réouverture.
- **Éteindre un Cadeau ne touche jamais un octet de la cinématique maître**, sous peine de casser tous les autres cadeaux de la même Expérience.
- **L'extinction garde le squelette commercial et rien d'autre** : pièces comptables (dix ans, L123-22 C. com.), enregistrement minimal de la Commande (cinq ans, L110-4 C. com.), horodatage des cases acceptées avec la version du libellé, et la trace de l'effacement (article 5 §2). Prouver le contrat n'exige pas le texte du message : tout ce qui décrit le contenu du cadeau meurt avec le cadeau.
- **Le Cron Trigger horaire porte quatre balayages**, tous pilotés par un état D1, aucun par une liste de bucket : commandes non payées de plus de 24 h, rappels à J-30, mises hors ligne à échéance, destructions d'octets échues. *Le balayage des originaux a disparu en cours d'arbitrage : la normalisation tournant dans le navigateur de l'Offrant, l'original ne quitte jamais son téléphone et il n'y a plus rien à détruire.*
- **Un chemin de suppression unique.** Un dérivé effacé par erreur est irrécupérable et l'original ne l'aurait pas sauvé — le même balayage fautif aurait emporté les deux. Time Travel de D1 permet de reconstituer quelle décision a été prise, même quand les octets sont partis.
- **Le remboursement « au prorata » promis en CGV a enfin un dénominateur : deux ans.**
