# Sonde de capacités sur appareils réels

**Ticket [#17](https://github.com/fayssalbenouda936/ouvrance/issues/17).** Comble les cinq trous que [Ce qu'iOS Safari et Android Chrome autorisent vraiment](https://github.com/fayssalbenouda936/ouvrance/issues/3) a laissés ouverts faute de source primaire. Ces chiffres ne se lisent nulle part : ils se mesurent.

La sonde vit dans `sonde/` — une page autonome et cinq clips générés (h264 720×1280, h264 sonore, hevc, av1, vp9). Aucun serveur, aucune dépendance : il suffit de servir le dossier.

---

## Ce que chaque mesure décide

| Mesure | Ce qui en dépend |
| --- | --- |
| **Décodeurs vidéo simultanés** | Toute la stratégie de préchargement entre cinématique d'ouverture, gameplay et cinématique de fuite — [L'architecture du lecteur d'expérience](https://github.com/fayssalbenouda936/ouvrance/issues/10) |
| **Moteur servant le lien, par application** | Si c'est une WebView, `localStorage` peut manquer, le plein écran peut être un no-op, et la partie A entière de la recherche #3 tient ou tombe |
| **Vidéo inline ou plein écran natif forcé** | Si `allowsInlineMediaPlayback` est à `false`, **aucune composition n'est possible** : plus d'overlay, plus de 3D par-dessus. C'est une condition d'existence du produit dans cette application |
| **Plafond mémoire avant éviction** | [Le budget de performance](https://github.com/fayssalbenouda936/ouvrance/issues/12) — le repli WebKit de 840 Mo n'est qu'un repli codé en dur |
| **Plafond de textures WebGL** | Le budget de textures du musée, et le seuil de perte de contexte |
| **Les deux verts** | Amendement de [La direction artistique du braquage](https://github.com/fayssalbenouda936/ouvrance/issues/6) : `#34C77B` (soin) contre `#4FD6C0` (caméra) doivent rester distincts en plein soleil |

## Ce que la page mesure, section par section

**2 · Relevé automatique** — sans geste. User-Agent et ses deux marqueurs de WebView Android (`wv`, `Version/4.0`) ; présence du suffixe `Safari/`, l'indice iOS de `WKWebView` ; `localStorage`, `sessionStorage`, IndexedDB, API Permissions, Service Worker ; `fullscreenEnabled` ; cœurs, `deviceMemory`, plafond du tas JS, quota de stockage ; écran, `devicePixelRatio`, zones sûres, gamut, HDR ; WebGL (version, `MAX_TEXTURE_SIZE`, GPU si non restreint, formats de textures compressées), WebGPU (adaptateur et limites) ; codecs par `canPlayType`, `MediaSource.isTypeSupported` et surtout `mediaCapabilities.decodingInfo`, qui dit `powerEfficient` — le seul signal de décodage matériel accessible au web.

**3 · Ce qu'un tap débloque** — tout part dans le même geste, comme l'exige iOS. `requestFullscreen()` : tenue, rejetée, ou **no-op silencieux** (détecté en comparant `innerHeight` avant / après, parce que la promesse peut se tenir sans que rien ne se passe). `AudioContext` : état avant et après `resume()`. Vidéo muette `playsinline` : joue-t-elle **dans la page**, ou l'événement `webkitbeginfullscreen` révèle-t-il que le lecteur natif a pris l'écran. Vidéo sonore : démarre-t-elle, et l'humain confirme s'il entend. Clips hevc / av1 / vp9 : décodés pour de vrai, ou `play()` rejeté — la vérification terrain de ce que `decodingInfo` prétend.

**4 · Décodeurs** — 40 `<video>` créées et lancées **dans le même tap**, chacune sur son propre `blob:` pour forcer une ressource distincte. Une vidéo compte quand elle joue vraiment (`currentTime > 0` et `videoWidth > 0`), pas quand `play()` se tient. Si les 40 tiennent, le bouton *Ajouter 40 de plus* monte par lots — le plafond n'est trouvé que lorsqu'il casse. Puis la moitié passe en pause et les échouées sont relancées : c'est le test de l'affirmation du bug WebKit 193449, « une vidéo en pause retient toujours son décodeur ».

**5 · Plafonds** — deux rampes destructives. Mémoire : blocs de 32 Mo, chaque page touchée pour qu'elle soit réellement engagée. Textures : 1024×1024 RGBA, 4 Mo pièce, avec `gl.finish()` à chaque pas pour empêcher l'allocation paresseuse, et écoute de `webglcontextlost`. **Le plantage est la mesure** : chaque palier est écrit dans le fragment de l'adresse, donc il survit au rechargement de l'onglet. Si l'onglet meurt, rouvrir la page suffit — le dernier palier s'affiche.

**6 · Les deux verts** — bandes pleines et mire alternée, à juger dehors.

**7 · Rapport** — JSON complet, résumé compact conçu pour la capture d'écran, bouton *Copier* et bouton *Partager* (Web Share, quand l'application le permet).

---

## Protocole

**Un passage par couple (application × appareil).** L'ordre compte : les rampes destructives se font **en dernier**, elles peuvent tuer l'onglet.

1. Ouvrir le lien **depuis l'application**, jamais en le collant dans le navigateur. Dans TikTok : se l'envoyer en message privé et taper dessus. Dans Instagram, WhatsApp, Snapchat : idem.
2. Renseigner l'application et le modèle en haut — ou utiliser un lien préparé, qui les remplit tout seul.
3. Lire le **relevé automatique**, il est déjà complet.
4. Taper **Lancer la sonde**. Observer de ses yeux : la vidéo joue-t-elle dans la page, ou l'écran a-t-il basculé dans le lecteur natif ? Répondre à la question du son.
5. Taper **Monter à 40 vidéos**. Si les 40 tiennent, **Ajouter 40 de plus**, jusqu'à ce que ça casse. Puis **Mettre la moitié en pause**.
6. **Copier le rapport** — et le coller quelque part tout de suite : dans une note, dans un message qu'on s'envoie. C'est le relevé principal, il ne doit pas mourir avec l'onglet.
7. Rampe mémoire, puis rampe textures. Si l'onglet meurt : rouvrir le lien, lire le palier repris en haut de page, le noter.
8. Le test des verts se fait dehors, en plein jour, mode économie d'énergie activé.

**Référence.** Faire d'abord un passage dans le navigateur normal de l'appareil (Safari, Chrome). Sans cette ligne de base, aucun écart mesuré dans une application n'est interprétable.

### Liens préparés

Servie sur le réseau local : `python3 -m http.server 8765 --bind 0.0.0.0` depuis `sonde/`. L'adresse dépend du poste — elle valait `192.168.1.37:8765` au passage du 27/08/2026.

| Application | Lien |
| --- | --- |
| Navigateur (référence) | `http://192.168.1.37:8765/?app=Navigateur&dev=iPhone` |
| TikTok | `http://192.168.1.37:8765/?app=TikTok&dev=iPhone` |
| Instagram | `http://192.168.1.37:8765/?app=Instagram&dev=iPhone` |
| WhatsApp | `http://192.168.1.37:8765/?app=WhatsApp&dev=iPhone` |
| Snapchat | `http://192.168.1.37:8765/?app=Snapchat&dev=iPhone` |

### La limite du HTTP en clair

Servie en HTTP, la page n'est pas un **contexte sécurisé**. WebGPU, le presse-papier, le partage, l'estimation de quota et les Service Workers y sont coupés **par la règle du navigateur**, quelle que soit l'application hôte : la sonde les marque donc `non mesurable en HTTP` au lieu de `false`, pour qu'on ne lise pas un faux négatif. Tout ce qui décide vraiment — moteur, plein écran, vidéo inline, décodeurs, mémoire, textures — reste mesurable en clair. Si une application refuse d'ouvrir une adresse IP nue, passer par un tunnel HTTPS éphémère (`cloudflared tunnel --url http://localhost:8765`) et refaire le passage.

---

## Relevés

Un fichier JSON par passage dans `docs/recherche/releves/`, nommé `APPAREIL-APPLICATION.json`. Le tableau ci-dessous en est l'index.

| Appareil | Application | Moteur | Plein écran | Vidéo inline | Décodeurs | Mémoire | Textures |
| --- | --- | --- | --- | --- | --- | --- | --- |
| iPhone 17 Pro Max, Safari 26.6 | Safari (référence) | WebKit, suffixe `Safari/604.1` | **API absente** | inline, `webkitPresentationMode: inline` | **≥ 42** (relevé par jalon, détail perdu au plantage) | arrêt à **1920 Mo** | 48 Mo — *contaminé* |
| _TikTok_ | | | | | | | |
| _Instagram_ | | | | | | | |
| _WhatsApp_ | | | | | | | |
| _Snapchat_ | | | | | | | |

Le relevé complet : `releves/iPhone17ProMax-Safari.json`.

**Contaminé** : ce passage a enchaîné décodeurs → rampe mémoire → rampe textures sans recharger. Les 48 Mo de textures ont donc été alloués par-dessus 42 vidéos vivantes, et c'est là que l'onglet est mort. Ce chiffre ne dit pas le plafond de textures, il dit qu'à ce niveau d'occupation il ne restait presque plus rien. La sonde interdit désormais ce mélange et exige un rechargement entre deux rampes.

### Les deux verts

| Appareil | Conditions | Verdict |
| --- | --- | --- |
| iPhone 17 Pro Max | à confirmer — plein soleil et mode économie ? | distincts |

---

## Ce que le passage de référence établit déjà

**Il n'y a pas de plein écran sur iPhone. Pas « refusé » : absent.** `requestFullscreen` n'existe sur aucun élément, `fullscreenEnabled` vaut `null`, et seul `video.webkitEnterFullscreen` répond — c'est-à-dire le lecteur natif, celui qui détruit toute composition. Ce n'est donc pas une restriction de navigateur in-app à contourner : **le jeu se joue dans la fenêtre du navigateur, barre d'adresse comprise**, et la mise en page doit être dessinée pour cette hauteur-là. Mesuré : `440×764` CSS, soit `1320×2292` pixels réels à dpr 3.

**Pas de verrou d'orientation non plus** (`screen.orientation.lock` absent). Le portrait imposé de [Le tracé du musée et la jouabilité en portrait](https://github.com/fayssalbenouda936/ouvrance/issues/29) ne peut pas être garanti par l'API : il doit être tenu par la mise en scène et par un écran de rappel si l'appareil bascule.

**Pas de MSE sur iPhone** : `window.MediaSource` est absent. Le plafond de 105 Mo par `SourceBuffer` du § 10.3 de la recherche #3 ne s'applique donc à rien ici — seul `ManagedMediaSource` existe depuis iOS 17.1, et il est désormais sondé.

**Le « 32 décodeurs » du bug WebKit de 2019 est trop bas.** Sur cet appareil, 42 vidéos 720×1280 ont atteint l'état `playing` — les 40 du premier lot, plus deux du second. Le chiffre reste à confirmer proprement : le détail des rejets a disparu avec l'onglet.

**AV1 est décodé en matériel.** `decodingInfo` donne `powerEfficient: true` pour h264, hevc, **av1** et vp9. Le piège AV1 du § 12.3 ne vaut pas pour cet appareil — ce qui rouvre, à la baisse, le poids des cinématiques maîtres. À confirmer sur un appareil plus ancien avant d'en faire un choix d'encodage.

**Textures : `MAX_TEXTURE_SIZE` 16384, WebGL 2, ASTC / PVRTC / ETC / S3TC tous présents**, GPU rapporté « Apple GPU ». Écran P3 et HDR.

**La mémoire tient loin.** L'allocation JS s'est arrêtée à 1920 Mo — bien au-delà du repli de 840 Mo codé en dur dans WebKit. C'est la mesure d'un haut de gamme de 2026 : elle ne dit rien du plancher, et c'est le plancher qui fixe le budget.

## Ce qui reste à mesurer

- **Les quatre applications.** C'est le cœur du ticket et il est intact : aucun passage in-app n'a encore eu lieu. Sans eux, on ne sait pas si TikTok laisse la vidéo jouer dans la page.
- **Un appareil d'entrée de gamme**, pour le vrai plancher mémoire et textures.
- **Tout le volet Android** : l'hypothèse « WebView système » reste non validée.
- **WebGPU, Wake Lock, Service Worker** : non mesurables en HTTP. Le Wake Lock compte — une partie dure six à huit minutes et l'écran ne doit pas s'éteindre.

---

## Lecture des résultats

- **`wv` ou `Version/4.0` présent** → WebView Android, et tout le tableau des défauts hostiles de `WebSettings` s'applique : `localStorage` coupé, `target="_blank"` qui remplace la page, `<meta viewport>` possiblement ignoré.
- **Plein écran refusé sans erreur** → l'application hôte n'implémente pas `onShowCustomView`. Le site ne peut rien y faire : il faut concevoir sans plein écran.
- **Vidéo qui part en lecteur natif** → `allowsInlineMediaPlayback = false`. Aucun overlay ne survit. Si cela arrive dans l'application qui apporte le trafic, c'est une contrainte de conception, pas un détail.
- **Décodeurs simultanés `n`** → le budget de préchargement vaut `n − 1` vidéos, marge comprise, et une vidéo en pause compte toujours si le test de pause l'a montré.
- **Rampe mémoire arrêtée à `m` Mo** → le seuil `Conservative` de WebKit se déclenche à la moitié : viser `m / 2` pour l'empreinte totale, textures et buffers vidéo compris.
