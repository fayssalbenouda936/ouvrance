# La normalisation tourne dans le navigateur de l'Offrant

Les dérivés normalisés que l'ADR-0005 exige sont produits **dans le navigateur de l'Offrant, avant le dépôt**. Le serveur relit les octets reçus, vérifie des bornes mesurables, et **ne convertit jamais**.

Une seule forme de sortie par type :

- **Photo** — JPEG progressif, 1024 px sur le grand côté, sRGB, qualité 0,80, métadonnées supprimées et orientation cuite dans les pixels. ≈ 150 Ko.
- **Greffe vocale** — MP3 mono, 44,1 kHz, 64 kbit/s constant, 30 s au plus, crête normalisée à −1 dBFS. 240 Ko.

**Le fichier d'origine ne quitte jamais l'appareil de l'Offrant.**

## Pourquoi

**Parce que le navigateur est le seul endroit qui contient déjà tous les décodeurs.** Un fichier produit par un appareil est décodable par le navigateur de cet appareil. Le HEIC n'existe que sur iPhone, dont le moteur est contractuellement WebKit — App Review Guidelines 2.5.6, relevé par la recherche sur les capacités web mobile. Côté audio, `decodeAudioData` couvre exactement le domaine que l'ADR-0005 s'est engagé à absorber : sa borne d'entrée n'est pas « tout audio » mais **« tout audio que le navigateur sait produire »**, et les trois conteneurs des navigateurs y sont par construction. Il ne reste qu'un encodeur à fournir, et il tient dans 150 Ko de JavaScript — pas dans les 25 Mo de `ffmpeg.wasm`, dont la variante rapide exigerait de surcroît les en-têtes COOP/COEP.

**Parce que ce placement supprime la seule défaillance qui coûte cher.** Les fichiers ne montent qu'au clic sur payer ; tout ce qui tourne dans le navigateur tourne donc en amont de ce clic. Une conversion serveur asynchrone est gratuite en temps — la Validation est humaine et différée — mais chère en échec : elle rate sur une Commande déjà payée, un humain le découvre à la Validation, et il n'y a plus qu'à écrire à l'Offrant en gardant le Cadeau en otage. C'est le cas que l'ADR-0005 a écrit pour supprimer. Placée avant le clic, la même défaillance est une erreur de formulaire, dite à quelqu'un qui a encore le fichier sous la main et qui n'a rien payé.

**Parce que le format de sortie se choisit sur le mode d'échec, pas sur le poids.** WebP pèserait 25 % de moins que JPEG, mais la spécification HTML n'oblige un canvas à encoder que PNG et JPEG : tout autre type est optionnel et, s'il n'est pas géré, le navigateur **retombe silencieusement sur PNG**, dix fois plus lourd, sans lever d'erreur. De même AAC serait meilleur que MP3 à débit égal, mais le produire dans un navigateur passe par `AudioEncoder` de WebCodecs, dont la prise en charge d'AAC diffère sur les trois moteurs — donc un arbre de repli à trois branches dont deux ne seront jamais jouées par leur auteur. LAME en JavaScript pur rend les mêmes octets partout sans interroger aucune capacité.

**Et parce que garder l'original n'achetait rien.** Il n'a aucun lecteur : la normalisation est une étape du dépôt, le lecteur ne lit que le dérivé, le validateur regarde le dérivé, une re-validation apporte son propre fichier. Il pèse dix fois le dérivé et porte l'EXIF — coordonnées GPS, modèle d'appareil, horodatage — d'une Personne représentée qui n'a rien consenti. Ne pas le téléverser fait mieux que le détruire tôt : il n'entre dans aucune sauvegarde, aucun journal, aucune ligne de l'AIPD.

## Conséquences

- **Aucune conversion ne tourne après le paiement.** La question « que faire quand la normalisation échoue sur une Commande payée » n'a plus d'objet.
- **Le serveur ne fait jamais confiance au champ déclaré : il relit l'octet.** Dimensions lues au marqueur `SOF` du JPEG, durée comptée sur les trames MP3, taille et type recoupés. Aucun WebAssembly côté serveur, aucun décodage dans le Worker.
- **Le Worker de dérivés fixe lui-même le `Content-Type` et ajoute `X-Content-Type-Options: nosniff`.** Le vrai risque n'est pas le fichier malformé, c'est le fichier bien formé servi avec le mauvais type.
- **La clé R2 est opaque.** Le nom du fichier de l'Offrant n'est ni stocké, ni journalisé — il décrit le Cadeau, et l'Extinction détruit tout ce qui le décrit.
- **Cinq bornes au dépôt, toutes mesurables, aucun jugement** : fichier indécodable par ce navigateur, plus de 25 Mo ou 50 mégapixels, plus de 30 s mesurées sur le PCM, silence sous −50 dBFS de crête, tout ce qui n'est ni image ni audio. Un fichier qui ne se normalise pas est un échec technique, jamais un motif de refus.
- **On refuse, on ne tronque pas.** Couper une phrase au milieu est pire que ne pas l'avoir.
- **Un fichier valide peut être refusé parce que ce navigateur-là ne sait pas l'ouvrir** — le vocal WhatsApp en Ogg/Opus déposé depuis Safari passerait depuis Chrome. Asymétrie assumée ; le remède offert est l'enregistrement dans le formulaire, qui est de toute façon le geste que le produit veut.
- **Une seule chaîne de normalisation.** Cloudflare Images n'entre pas comme filet serveur : deux chaînes en font une qui n'est jamais testée.
- **Un dérivé perdu dans R2 est irrécupérable et plus aucun original ne le sauve.** Le remède reste un chemin de suppression unique piloté par un état D1 explicite, jamais par une liste de bucket.
- **Les dérivés vivent en mémoire dans l'onglet jusqu'au clic sur payer** : un rechargement de page les perd et l'Offrant re-choisit ses fichiers.
- **Le téléversement au clic sur payer passe de ~16 Mo à ~1,35 Mo** sur une commande courante, et le plafond de corps de requête du Worker cesse d'être atteignable.
