# Une expérience déclare une bande ; le noyau la lit

Une expérience ne fournit pas de code d'affichage : elle déclare une **bande** — une liste ordonnée de segments typés, `cinematique`, `scene-dom`, `scene-3d` — et fournit un rendu pour ses seuls segments non-vidéo. Le noyau enchaîne la bande, et tout ce qui vit *entre* deux segments lui appartient.

La bande est une **donnée**, pas une fonction : un tableau déclaré, que la porte de publication peut lire.

Le noyau porte l'écran d'amorce, le déblocage média, le préchargement, la bascule, la fenêtre et la Récompense. Il ne connaît jamais le schéma de la Personnalisation (ADR-0005).

## Pourquoi

**Parce que les deux produits sont déjà la même bande.** Carte animée : poster → cinématique de dépliage → scène DOM, la table et ses six emplacements → Récompense. Braquage : poster → cinématique d'ouverture → scène 3D → cinématique de fuite → Récompense. Ce n'est pas une abstraction inventée au-dessus de deux cas, c'est la forme que les deux ont déjà.

**Parce que ce qui est dangereux vit entre les segments.** Le déblocage média iOS est par élément et définitif ; un `<video>` en pause **et caché** est purgeable ; la bascule doit tomber entre deux images identiques (ADR-0013). Une bibliothèque d'organes laisserait chaque expérience refaire ces erreurs — et le legacy prouve qu'elles se font : `apps/gifts/_templates/animation-cadeau/src/lettre/lettre.ts` détruit son élément vidéo après lecture et commente qu'« un iPhone n'en lit qu'un à la fois ». Deux croyances que la recherche #3 et la sonde #17 ont démenties, codées en dur dans le seul produit vendable.

**Parce qu'un cadre qui conduit sans savoir ne peut rien armer.** Un noyau qui appellerait `experience.jouer()` sans connaître d'avance les vidéos ne pourrait pas les débloquer toutes dans le geste unique qu'iOS accorde. La déclaration n'est pas de la cérémonie : c'est la condition pour que le tap serve à quelque chose.

**Parce qu'une donnée se vérifie et qu'un code ne se vérifie pas.** Plafond de vidéos, présence des assets, nombre d'emplacements égal au plafond de la formule (ADR-0004) : la porte de publication créée par l'ADR-0005 sait lire un tableau. Elle ne sait pas lire une fonction.

## Conséquences

- **Aucune incrustation sur une vidéo qui joue.** Un segment vidéo est du pixel non personnalisé ; la personnalisation vit dans un segment DOM ou 3D, dont le fond peut être la dernière image de la cinématique servie comme image fixe. Le noyau n'a pas de compositeur, et cet organe sort de son périmètre. C'est aussi ce qui rend l'architecture indifférente au seul angle mort laissé par #17 : si une WebView force le lecteur natif, un relais survit là où une incrustation meurt.
- **Quatre `<video>` au maximum par bande**, déclarées, armées ensemble au premier tap, et **jamais détruites**. Braquage : deux. Carte animée : une.
- **Le noyau seul décide quand précharger.** L'expérience déclare ses vidéos, jamais leur calendrier. La politique reste derrière l'interface du noyau, ce qui laisse le ticket #44 n'en changer qu'un module.
- **Jamais de trou à la bascule** : le noyau tient la dernière image du segment sortant jusqu'à ce que le suivant ait rendu la sienne. C'est l'ADR-0003 appliqué au temps.
- **La Récompense est le dernier segment et appartient au noyau.** Une expérience ne la redessine pas : c'est l'écran qui porte le lien de virement.
- **L'écran d'amorce est hors bande.** Il arme d'un seul geste l'AudioContext, toutes les vidéos de la bande et le bus audio du jeu — sans quoi le braquage est muet sur iPhone (#6).
- **Le noyau porte la fenêtre** : 440 × 764 CSS barre d'adresse comprise, safe zones, et l'écran de rappel en paysage faute de verrou d'orientation (#17). Un segment reçoit une boîte et ne la renégocie pas.
- **Aucune reprise.** Rouvrir le Lien rejoue depuis le début : #18 interdit toute écriture sur le terminal du Destinataire, et une reprise serveur rendrait au canal identifiant exactement ce que #18 lui a retiré. Les points de reprise du braquage (#8) restent internes à la partie et meurent avec l'onglet.
- **L'état muet vit en mémoire** et meurt avec l'onglet. Le `localStorage` du legacy disparaît.
- **Le lecteur reçoit un manifeste unique rendu par le serveur** sur `/cadeau/[lien]` : blocs communs, Personnalisation résolue par le registre, adresses des dérivés et des assets maîtres. Aucune requête avant le premier pixel.
- **La sortie unique du legacy devient une règle du noyau.** `ended`, une erreur de chargement et un `play()` refusé mènent tous au segment suivant : un segment qui ne démarre pas n'escamote jamais le Cadeau en silence, et la Récompense reste atteignable quoi qu'il arrive.
