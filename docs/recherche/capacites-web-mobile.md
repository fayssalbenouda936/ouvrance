# Android WebView, Custom Tabs et Chrome — ce qu'un lien ouvert dans une app autorise

**Recherche partielle du ticket [#3](https://github.com/fayssalbenouda936/ouvrance/issues/3).** Vérifié le 20/08/2026 sur sources primaires. Cette page ne couvre **que le volet Android WebView / Custom Tabs**. Le volet iOS Safari, les décodeurs simultanés, les codecs et le réseau restent à faire.

**Convention de fiabilité** : `[OFF]` = documentation officielle Google/Chromium · `[SRC]` = code source Chromium (officiel, non documentaire) · `[COM]` = inférence, non confirmé sur source primaire.

## 1. Quel moteur rend le contenu

`[OFF]` [WebView overview](https://developer.chrome.com/docs/webview) (MàJ 18/12/2024) : « The WebView component is based on the Chromium open source project. WebView shares the same rendering engine as Chrome for Android [...] **WebView has an APK so it can be updated separately from Android.** »

Et, décisif : « **Chrome and WebView don't share any data.** »

| Version Android | Fournisseur WebView par défaut (appareils avec services Google) |
| --- | --- |
| 7 – 9 | **`com.android.chrome`** — c'est l'APK Chrome qui rend le contenu (build « Monochrome ») |
| 10 et + | **`com.google.android.webview`** — Trichrome : deux APK séparés partageant une bibliothèque commune, mis à jour indépendamment via le Play Store |

Source : `[OFF]` [webview-providers.md](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/webview-providers.md) et [legacy-os-behavior.md](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/legacy-os-behavior.md), HEAD au 20/08/2026.

WebView suit la cadence Milestone de Chrome (`[OFF]` [web-platform-compatibility.md](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/web-platform-compatibility.md) : « it's WebView's explicit goal [...] to ship new versions alongside Chrome for Android »). Mais depuis Android 10 ce sont deux applications distinctes : sur un appareil donné, **les versions peuvent diverger**. `[COM]` Aucune source Google ne chiffre cet écart sur le parc.

## 2. Ce qui est coupé par défaut dans une WebView

Source : `[OFF]` [WebSettings](https://developer.android.com/reference/android/webkit/WebSettings), MàJ 03/08/2026. Défauts documentés, verbatim.

| Réglage | Défaut | Conséquence |
| --- | --- | --- |
| `setJavaScriptEnabled` | **`false`** | Rien ne tourne sans opt-in de l'app hôte |
| `setDomStorageEnabled` | **`false`** | **`localStorage` et `sessionStorage` indisponibles** |
| `setMediaPlaybackRequiresUserGesture` | **`true`** | Autoplay bloqué sans geste (`[SRC]` mappé sur `AutoplayPolicy::kUserGestureRequired`, `aw_settings.cc`) |
| `setAllowFileAccess` | `false` si targetSdk ≥ 30 | Chargement `file://` bloqué |
| `setJavaScriptCanOpenWindowsAutomatically` | **`false`** | `window.open()` sans geste = no-op |
| `setSupportMultipleWindows` | **`false`** | `target="_blank"` **remplace la page courante** au lieu d'ouvrir ailleurs |
| `setUseWideViewPort` | non documenté, quirk actif `[SRC]` | Si l'app ne l'active pas, **`<meta viewport>` est ignoré** — le rendu 3D est mal dimensionné |
| `setMixedContentMode` | `MIXED_CONTENT_NEVER_ALLOW` (targetSdk ≥ 21) | Assets HTTP dans page HTTPS bloqués |

**Cookies tiers** — `[OFF]` [CookieManager](https://developer.android.com/reference/android/webkit/CookieManager) : « Apps targeting `LOLLIPOP` or later **default to disallowing** third party cookies. » Le cookie store est propre à l'application (`[OFF]` [cookies.md](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/cookies.md)) — invisible de Chrome et des autres apps.

**IndexedDB** — `[SRC]` `setDomStorageEnabled` ne pilote que `web_prefs->local_storage_enabled` (`aw_settings.cc`, l. 682-683) ; aucun switch ne coupe IndexedDB dans `aw_main_delegate.cc`. **IndexedDB est donc le seul stockage persistant sur lequel compter dans une WebView.** `[COM]` pour la formulation « garanti », faute de doc Android explicite.

`[SRC]` En revanche la **File System API est explicitement coupée** : `// File system API not supported (requires some new API; internal bug 6930981)` → `switches::kDisableFileSystem`.

## 3. Capacités graphiques — la bonne nouvelle

**WebGL / WebGL2 : toujours activé.** `[SRC]` `aw_settings.cc` (l. 743-746), commentaire littéral : « **Always allow webgl.** Webview always requires access to the GPU even if it only does software draws. »

**Accélération matérielle : activée par défaut.** `[OFF]` [WebView overview](https://developer.chrome.com/docs/webview) : « Hardware acceleration is enabled by default. »

**Mais l'architecture GPU est dégradée** — `[OFF]` `web-platform-compatibility.md` : « **WebView does not use a separate GPU process even when running in multi-process mode.** » et « Only **one renderer per app** is currently used ». `[SRC]` `aw_main_delegate.cc` l. 205 : `AppendSwitch(switches::kInProcessGPU)`. `[SRC]` Vulkan (`::features::kVulkan`), DrDc et HDR (`ui::kAndroidHDR`, « HDR does not support webview yet ») sont désactivés.

**WebGPU : disponible.** `[OFF]` chromestatus tient un jalon `webview` par sous-feature depuis ≈ M127 (GPUAdapter info : webview 127 ; extended range HDR : 129 ; dual source blending : 130 ; 1-component vertex formats : 133). `[SRC]` `aw_field_trials.cc` ne contient **aucune** désactivation WebGPU, là où il coupe explicitement WebXR, FedCM, WebUSB. Mêmes contraintes matérielles que Chrome Android (`[OFF]` [new-in-webgpu-121](https://developer.chrome.com/blog/new-in-webgpu-121) : Android 12+, GPU Qualcomm et ARM).

## 4. Ce qui manque à WebView — et qui fait mal ici

La liste officielle des écarts est très succincte. **La source de vérité est le code** : `[SRC]` [`aw_main_delegate.cc`](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/android_webview/lib/aw_main_delegate.cc) et [`aw_field_trials.cc`](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/android_webview/browser/aw_field_trials.cc), commentaires littéraux :

```
// Not yet supported in single-process mode.        -> kDisableSharedWorkers
// File system API not supported                    -> kDisableFileSystem
// Web Notification API and the Push API are not supported (crbug.com/434712)
                                                    -> kDisableNotifications
// WebView does not yet support screen orientation locking.
                                                    -> kDisableScreenOrientationLock
// WebView does not support MediaSession API since there's no UI for media
//   metadata and controls.                         -> kDisableMediaSessionAPI
```

Également désactivés `[SRC]` : `kWebXr` (« WebXR is not yet supported on WebView »), `kCrossOriginOpenerPolicy` (« COOP is not supported on WebView yet »), `media::kOverlayFullscreenVideo` (« WebView does not support overlay fullscreen yet for video overlays »), `kBackgroundFetch`, `kPeriodicBackgroundSync`, `kFedCm`, `kWebBluetooth`, `kWebUsb`, `kInstallElement`, `kWebAppLaunchQueue`.

### Le point le plus grave : la Fullscreen API

`[SRC]` `WebViewChromium.java` — WebView active `fullscreen_supported` **uniquement si l'app hôte a surchargé `onShowCustomView` ET `onHideCustomView`** :

```java
mWebSettings.getAwSettings().setFullscreenSupported(doesSupportFullscreen(client));
// ...
// For fullscreen support, implementations of WebChromeClient#onShowCustomView
// and WebChromeClient#onHideCustomView() are required.
```

Confirmé côté doc `[OFF]` `web-platform-compatibility.md` : « **Cooperation from the embedding app is needed to implement features such as popup windows and fullscreen, and apps may not implement these, or implement them incorrectly.** »

**`element.requestFullscreen()` peut donc être un no-op silencieux dans la WebView de TikTok ou d'Instagram, sans que le site puisse rien y faire.**

### Permissions

`[OFF]` `web-platform-compatibility.md` : « **The Web Permissions API is not implemented in WebView**, and in general any code in Chromium that relies on being able to silently check the status of permissions will not work. » → `navigator.permissions.query()` inutilisable.

`[OFF]` `WebChromeClient.onPermissionRequest` : « **If this method isn't overridden, the permission is denied.** »

### Origin Trials et flags

`[SRC]` Les Origin Trials **sont** implémentés dans WebView (`aw_browser_context.cc` instancie `origin_trials::OriginTrials` avec le même `TrialTokenValidator` que Chrome).

Mais `[OFF]` `web-platform-compatibility.md` : « **WebView is a separate "platform" for UMA/Finch purposes; experiments targeting "android" only affect Chrome for Android, not WebView.** » et « On production devices, only the flags in the developer UI can be used ». **`chrome://flags` est sans effet sur WebView.**

### Debug impossible

`[OFF]` [`setWebContentsDebuggingEnabled`](https://developer.android.com/reference/android/webkit/WebView#setWebContentsDebuggingEnabled) : activé automatiquement seulement si l'app est `android:debuggable="true"`. Les builds Play Store ne le sont pas. **On ne peut pas inspecter la WebView de TikTok via `chrome://inspect`.**

## 5. Custom Tabs — la parité totale

`[OFF]` [Overview of Android Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs) (MàJ 09/02/2026) :

> « By using a Custom Tab, your web content loads in **whatever rendering engine powers your user's preferred browser. Any API or web platform feature is available there, and is available in your Custom Tab.** »

> « Custom Tabs are **powered directly by the user's preferred browser and automatically share the state and features offered by it** [...] **Shared cookie jar and permissions model** »

> « Lifecycle management: Apps launching a Custom Tab won't be evicted by the system during the Tab's use. The importance of the Custom Tab is raised to the **foreground** level. »

Et le verdict explicite de Google sur l'alternative :

> « **WebViews don't support all features of the web platform, don't share state with the browser and add maintenance overhead.** »

`[OFF]` [browser-support](https://developer.chrome.com/docs/android/custom-tabs/browser-support) (MàJ 13/08/2026) : ce qui varie entre navigateurs, ce sont les **options d'UI** du protocole, pas les capacités web. Avertissement : « **It is currently not possible to programmatically check on an Android device, if an installed browser supports a specific Custom Tab feature.** »

## 6. Sortir d'une WebView vers le navigateur — non, ce n'est pas fiable

**`target="_blank"` ne sort jamais.** `[OFF]` `setSupportMultipleWindows` : avec le défaut `false`, les liens `target="_blank"` « will instead be **treated as top-level navigations, replacing the current page in the same WebView** ». Avec multi-windows activé mais `onCreateWindow` non implémenté (`[OFF]` défaut : « does nothing and hence returns `false` »), il ne se passe rien.

**`intent://` dépend entièrement de l'app hôte.** `[OFF]` [shouldOverrideUrlLoading](https://developer.android.com/reference/android/webkit/WebViewClient#shouldOverrideUrlLoading) : sans `WebViewClient`, le système résout l'URL. Mais **TikTok, Instagram, Facebook en ont tous un** (navigation interne, barre de titre, télémétrie). S'il retourne `false` sur un `intent://`, la WebView tente de charger l'URL et **échoue** (schéma non-HTTP). S'il retourne `true` sans lancer d'Intent, rien ne se passe.

`[COM]` `S.browser_fallback_url` est un mécanisme documenté pour **Chrome**, implémenté dans `//chrome`. Rien n'indique que WebView le parse — **non vérifié**.

> **Conclusion opérationnelle : aucun mécanisme purement côté site ne permet de sortir de manière fiable d'une WebView in-app.** Le seul levier robuste est le menu ⋮ de l'app hôte, hors de notre contrôle.

## 7. Tableau décisionnel

| Capacité | WebView in-app (défaut) | Custom Tab | Chrome |
| --- | --- | --- | --- |
| WebGL / WebGL2 | ✅ **toujours activé** `[SRC]` | ✅ | ✅ |
| Accélération matérielle | ✅ (pas de process GPU séparé) | ✅ | ✅ |
| WebGPU | ✅ (≈M127+) | ✅ | ✅ |
| `localStorage` | ❌ **coupé par défaut** | ✅ | ✅ |
| IndexedDB | ✅ | ✅ | ✅ |
| **Fullscreen API** | ❌ **sauf si l'app l'implémente** | ✅ | ✅ |
| Autoplay média | ❌ geste requis | ✅ | ✅ |
| `<meta viewport>` | ⚠️ ignoré si `setUseWideViewPort(false)` | ✅ | ✅ |
| Verrouillage d'orientation | ❌ désactivé | ✅ | ✅ |
| MediaSession | ❌ désactivé | ✅ | ✅ |
| Notifications / Push | ❌ non supporté | ✅ | ✅ |
| Permissions API | ❌ non implémentée | ✅ | ✅ |
| Cookies tiers | ❌ coupés | ✅ | ✅ |
| Partage de session avec Chrome | ❌ jamais | ✅ | ✅ |
| DevTools distant | ❌ apps Play Store | ✅ | ✅ |
| `target="_blank"` sort de l'app | ❌ jamais | n/a | n/a |
| `intent://` fiable | ❌ dépend de l'app hôte | n/a | ✅ |

## Conséquences pour ouvrance

1. **La 3D passe.** WebGL est toujours actif en WebView, l'accélération matérielle aussi. Le pari Three.js / React Three Fiber n'est pas menacé par le chemin d'ouverture in-app.
2. **Le plein écran ne passe pas de façon fiable.** C'est le risque numéro un : `requestFullscreen()` peut être un no-op muet. **Concevoir le lecteur pour être plein-écran sans l'API** — mise en page en `100dvh`, aucun élément d'UI qui suppose le mode fullscreen, aucun verrouillage d'orientation (lui aussi désactivé).
3. **Ne jamais dépendre de `localStorage`.** Coupé par défaut. Utiliser IndexedDB, ou mieux, ne rien persister côté client.
4. **Ne pas compter sur `<meta viewport>`.** Prévoir un rendu correct même si le viewport est ignoré, et mesurer les dimensions réelles au runtime plutôt que de les supposer.
5. **Pas de MediaSession, pas de notification, pas d'orientation verrouillée.** Aucune de ces API ne doit porter une fonctionnalité, seulement une amélioration.
6. **Le budget mémoire est plus serré qu'en Chrome** : un seul renderer par app, GPU in-process. À croiser avec le volet iOS quand il sera fait.
7. **On ne peut pas déboguer sur le terrain.** Les tests doivent passer par une app de test locale reproduisant les défauts `WebSettings`, pas par `chrome://inspect` sur TikTok.

## Non vérifié

- **Milestone exact de ship WebGPU dans WebView** — déduit des sous-features chromestatus (≥ M127) et de l'absence de désactivation dans `aw_field_trials.cc`. L'« Intent to Ship » sur blink-dev n'a pas été consulté.
- **`display-mode: standalone` dans WebView** — l'affirmation « vaut `browser` » est une inférence, pas une source primaire.
- **`S.browser_fallback_url` dans WebView** — probablement non parsé (code dans `//chrome`), non confirmé.
- **Moteurs embarqués custom** — rien n'a pu être établi sur le fait que TikTok, Instagram ou Facebook utilisent la WebView système plutôt qu'un Chromium embarqué. **Tous les faits ci-dessus supposent la WebView système.** À valider empiriquement (chaîne UA, présence du token `wv`).
- **Décalage de version Chrome/WebView sur le parc** — non chiffré par Google.
- `kDisableSharedWorkers` est toujours présent dans `aw_main_delegate.cc` alors que chromestatus liste « SharedWorker on Android » avec `webview: 148`. Contradiction non résolue.

## Reste à faire sur ce ticket

- **Tout le volet iOS Safari** : autoplay 2026, `playsinline`, persistance du déblocage par geste, AudioContext et mode silencieux, **nombre de décodeurs vidéo simultanés**, plafonds mémoire avant éviction d'onglet, WebGL/WebGPU sur iOS.
- **Codecs et conteneurs** : HEVC vs H.264 vs AV1 sur mobile en 2026, impact sur le poids des maîtres.
- **Cartographie par application** : quel moteur exact pour TikTok, Instagram, WhatsApp, Snapchat, et sur iOS (`SFSafariViewController` vs `WKWebView`).
- **Réseau** : 4G médiocre, `Save-Data`, coût en données d'un préchargement agressif.
