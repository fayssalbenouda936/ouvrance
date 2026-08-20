# Ce qu'iOS Safari et Android Chrome autorisent vraiment

**Recherche du ticket [#3](https://github.com/fayssalbenouda936/ouvrance/issues/3).** Vérifié le **20/08/2026** sur sources primaires : code WebKit et Chromium, documentation Apple et Google, spécifications W3C/WHATWG.

**Convention de fiabilité** : `[OFF]` = documentation officielle éditeur · `[SRC]` = code source du moteur (officiel, non documentaire) · `[COM]` = inférence, non confirmé sur source primaire.

**Plan.** Partie A : Android WebView, Custom Tabs et Chrome. Partie B : iOS Safari. Partie C : codecs, cartographie par application, réseau. Puis les conséquences pour ouvrance.

---

# Partie A — Android WebView, Custom Tabs et Chrome

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

---

# Partie B — iOS Safari

Sauf mention contraire, le code cité est celui de `WebKit/WebKit` branche `main`, lue le **20/08/2026**. WebKit est le moteur de Safari : c'est la source de vérité la plus proche du comportement réel, la documentation Apple sur le sujet étant à la fois maigre et très ancienne.

## 8. Autoplay et geste utilisateur sur iOS

### 8.1 Les règles de base

`[OFF]` [New `<video>` Policies for iOS](https://webkit.org/blog/6784/new-video-policies-for-ios/), WebKit, **25/07/2016** — verbatim :

> « On iPhone, `<video playsinline>` elements will now be allowed to play inline, and will not automatically enter fullscreen mode when playback begins. »

> « `<video muted>` elements will also be allowed to autoplay without a user gesture. »

> « `<video>` elements will be allowed to `autoplay` without a user gesture if their source media contains no audio tracks. »

> « When we say that an action must have happened "as a result of a user gesture", we mean that the JavaScript which resulted in the call to `video.play()`, for example, must have directly resulted from a handler for a `touchend`, `click`, `doubleclick`, or `keydown` event. »

**Cette page a dix ans.** Elle reste la seule page normative publiée par Apple sur le sujet ; on la complète donc par le code, qui est à jour.

⚠️ `[OFF]` L'ancien guide Apple [iOS-Specific Considerations](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/Device-SpecificConsiderations/Device-SpecificConsiderations.html) (**dernière révision 13/12/2012**) affirme encore « all devices running iOS are limited to playback of a single audio or video stream at any time » et « preload and autoplay are disabled ». **Ces deux affirmations sont périmées** — contredites par le billet de 2016 et par le code actuel. Elle n'est citée ici que pour qu'on cesse de la retrouver dans les résultats de recherche et de la croire.

### 8.2 `playsinline` — la règle exacte

`[SRC]` `MediaElementSession::requiresFullscreenForVideoPlayback()`, `Source/WebCore/html/MediaElementSession.cpp` (l. 1097-1143). La logique, dans l'ordre :

1. Un `<audio>` n'est jamais concerné.
2. Si `allowsInlineMediaPlayback` est faux (réglage d'hôte, pertinent en WebView), **le plein écran est imposé, point**.
3. Si `inlineMediaPlaybackRequiresPlaysInlineAttribute` est faux, l'inline est libre.
4. Sinon : `return !element->hasAttributeWithoutSynchronization(HTMLNames::playsinlineAttr);`

**Le piège pour les navigateurs in-app** — même fonction, bloc `#if PLATFORM(IOS_FAMILY)` :

```cpp
if (!linkedOnOrAfterSDKWithBehavior(SDKAlignedBehavior::UnprefixedPlaysInlineAttribute))
    return !element->hasAttributeWithoutSynchronization(HTMLNames::webkit_playsinlineAttr);
```

`[SRC]` Une application liée contre un SDK antérieur à l'introduction de l'attribut non préfixé **n'honore que `webkit-playsinline`**. La parade est gratuite : **écrire les deux attributs**, `playsinline` et `webkit-playsinline`.

`[SRC]` Un quirk par site existe aussi (`shouldIgnorePlaysInlineRequirementQuirk()`), et Apple Books est traité à part — deux rappels que le comportement n'est pas uniforme.

### 8.3 Ce qu'un geste débloque exactement

`[SRC]` Les restrictions sont des drapeaux de `MediaElementSession::BehaviorRestrictions`, posés à la construction de l'élément (`HTMLMediaElement::initializeMediaSession()`, `HTMLMediaElement.cpp` l. 710-772) :

| Restriction | Posée quand | Effet |
| --- | --- | --- |
| `RequireUserGestureForVideoRateChange` | réglage plateforme (actif sur iOS) | tout `<video>` a besoin d'un geste |
| `RequireUserGestureForAudioRateChange` | idem | mais **contournée si `muted()` ou `volume()==0`** |
| `RequireUserGestureForLoad` | si `requiresUserGestureToLoadVideo()` | même charger l'octet 0 demande un geste |
| `AutoPreloadingNotPermitted` | si `!mediaDataLoadsAutomatically()` | `preload` désobéi |
| `InvisibleAutoplayNotPermitted` | réglage | pas d'autoplay hors écran |
| `RequireUserGestureForFullscreen` | toujours | |
| **`RequireUserGestureForVideoDueToLowPowerMode`** | `page->isLowPowerModeEnabled()` | |
| **`RequireUserGestureForVideoDueToAggressiveThermalMitigation`** | `page->isAggressiveThermalMitigationEnabled()` | |

`[SRC]` `MediaElementSession::playbackStateChangePermitted()` (l. 465-556) applique la règle du muet littéralement :

```cpp
if (m_restrictions & RequireUserGestureForAudioRateChange && (!element->isVideo() || element->hasAudio())
    && !element->muted() && element->volume() && !document->processingUserGestureForMedia())
    return makeUnexpectedDenial(...);
```

**Le fait le plus important de cette section, et il n'est documenté nulle part côté Apple :**

```cpp
if (m_restrictions & RequireUserGestureForVideoDueToLowPowerMode && element->isVideo()
    && !document->processingUserGestureForMedia())
    return makeUnexpectedDenial(..., "Video low power mode restriction"_s);

if (m_restrictions & RequireUserGestureForVideoDueToAggressiveThermalMitigation && element->isVideo()
    && !document->processingUserGestureForMedia())
    return makeUnexpectedDenial(..., "Video aggressive thermal mitigation"_s);
```

Ces deux tests portent sur `element->isVideo()` **sans exception pour `muted`**. `[SRC]` Conclusion : **en mode économie d'énergie, ou quand l'appareil est en mitigation thermique, même une vidéo muette et sans piste audio n'autoplay pas.** Un iPhone à 15 % de batterie, ou qui vient de faire tourner du WebGL pendant deux minutes, casse l'autoplay muet.

`[SRC]` WebKit expose d'ailleurs cet état en interne (`HTMLMediaElement.cpp` l. 8432) :

```cpp
return isVideo() && autoplay() && (mediaSession().hasBehaviorRestriction(MediaElementSession::RequireUserGestureForVideoDueToLowPowerMode)
    || mediaSession().hasBehaviorRestriction(MediaElementSession::RequireUserGestureForVideoDueToAggressiveThermalMitigation));
```

`[COM]` Il n'existe **aucune API web** permettant de savoir si l'appareil est en mode économie d'énergie ou en mitigation thermique. On ne peut que constater l'échec de `play()` — donc **toujours traiter la promesse renvoyée par `play()`** et prévoir un écran « Toucher pour commencer ».

### 8.4 Combien de temps le déblocage persiste — la réponse

Deux mécanismes distincts, qu'il ne faut pas confondre.

**(a) « Être dans un geste » — trois fenêtres temporelles.** `[SRC]` `Document::mediaUserGestureReason()`, `Source/WebCore/dom/Document.cpp` (l. 9636-9656) :

```cpp
if (UserGestureIndicator::processingUserGestureForMedia())          return MediaGestureReason::ActiveToken;
if (m_domWindow && m_domWindow->hasTransientActivation())           return MediaGestureReason::TransientActivation;
if (m_userActivatedMediaFinishedPlayingTimestamp + maxIntervalForUserGestureForwardingAfterMediaFinishesPlaying >= MonotonicTime::now())
                                                                     return MediaGestureReason::MediaFinishedGrace;
```

| Fenêtre | Durée | Constante `[SRC]` |
| --- | --- | --- |
| Jeton de geste actif, transporté à travers une chaîne `fetch` | **10 s** | `maxIntervalForUserGestureForwardingForFetch { 10 }` — `dom/UserGestureIndicator.cpp` l. 114 |
| Activation transitoire (`navigator.userActivation.isActive`) | **5 s** | `defaultTransientActivationDuration { 5_s }` — `page/LocalDOMWindow.cpp` l. 200 |
| Grâce après qu'un média lancé par l'utilisateur s'est **terminé** | **1 s** | `maxIntervalForUserGestureForwardingAfterMediaFinishesPlaying { 1_s }` — `dom/Document.cpp` l. 499 |

La fenêtre de 1 s est celle qui décide de l'enchaînement cinématique → gameplay → cinématique : **quand une vidéo lancée par l'utilisateur atteint sa fin, il reste une seconde pour démarrer la suivante sans nouveau geste**. Au-delà, il faut un nouveau tap.

**(b) Le déblocage définitif, et il est *par élément*.** `[SRC]` `HTMLMediaElement::removeBehaviorRestrictionsAfterFirstUserGesture()` (l. 9184-9209) efface d'un coup, **sans minuterie ni expiration** :

`RequireUserGestureForLoad`, `AutoPreloadingNotPermitted`, `RequireUserGestureForVideoRateChange`, `RequireUserGestureForAudioRateChange`, `RequireUserGestureForFullscreen`, `RequireUserGestureForVideoDueToLowPowerMode`, `RequireUserGestureForVideoDueToAggressiveThermalMitigation`, `InvisibleAutoplayNotPermitted`, `RequireUserGestureToControlControlsManager`.

`[SRC]` Elle est appelée depuis `play()`, la variante à promesse de `play()`, `prepareForLoad()`, la pose de l'attribut `autoplay` — chaque fois sous condition `if (processingUserGestureForMedia())`.

> **Le déblocage n'est ni par onglet ni par origine : il est porté par l'objet `MediaElementSession`, donc par l'élément `<video>` lui-même.** Un `<video>` créé plus tard repart avec toutes ses restrictions. Le déblocage dure aussi longtemps que l'élément vit — indéfiniment, tant qu'on ne le détruit pas.

`[SRC]` La seule propagation au document est `mainFrameDocument->noteUserInteractionWithMediaElement()`, qui n'est consommée que derrière un quirk par site (`quirks().needsPerDocumentAutoplayBehavior()`) — donc **pas un comportement général sur lequel s'appuyer**.

**Conséquence d'architecture directe** : au premier tap, appeler `play()` (quitte à `pause()` immédiatement après) sur **tous** les éléments `<video>` du parcours — intro, gameplay, fin — pour les débloquer à vie. Ne jamais détruire ces éléments ; les réutiliser en changeant leur source. Cette stratégie entre en tension frontale avec la limite de décodeurs simultanés (§ 10).

## 9. AudioContext, mode silencieux, retour d'arrière-plan

### 9.1 Déblocage de l'AudioContext — une règle différente de celle des `<video>`

`[SRC]` `Source/WebCore/Modules/webaudio/AudioContext.cpp`, l. 93-101 :

```cpp
static bool shouldDocumentAllowWebAudioToAutoPlay(const Document& document)
{
    if (document.isCapturing()) return true;
    RefPtr mainDocument = document.mainFrameDocument();
    if (document.quirks().shouldAutoplayWebAudioForArbitraryUserGesture() && mainDocument && mainDocument->hasHadUserInteraction())
        return true;
    RefPtr window = document.window();
    return window && window->hasTransientActivation();
}
```

Appelée par `AudioContext::willBeginPlayback()` (l. 499-516), qui retire ensuite définitivement `RequireUserGestureForAudioStartRestriction`.

> **Le Web Audio ne connaît que l'activation transitoire : une fenêtre de 5 s.** Il n'hérite **pas** de la grâce de 1 s après fin de média, ni du transport de jeton à 10 s à travers `fetch`. Un `audioContext.resume()` lancé plus de 5 s après le dernier tap échoue.

`[COM]` Corollaire pratique : `resume()` doit être appelé dans le même geste que le premier `play()`. Le retarder « au moment où on en aura besoin » est un bug d'architecture, pas une optimisation.

### 9.2 Retour d'arrière-plan — l'état `interrupted`

`[SRC]` WebKit ajoute à `AudioContext` un état hors spécification, `State::Interrupted` (`AudioContext.cpp` l. 350-355 et 571-572) :

```cpp
bool interrupted = context.m_mediaSession->state() == PlatformMediaSession::State::Interrupted;
context.setState(interrupted ? State::Interrupted : State::Running);
```

`[SRC]` `AudioContext::shouldOverrideBackgroundPlaybackRestriction()` (l. 781-800) : le passage en arrière-plan (`InterruptionType::EnteringBackground`) n'interrompt pas le contexte si sa destination n'est pas connectée, ou si le document tient déjà une session audio de type lecture (`hasPlayBackAudioSession`).

`[COM]` Donc `audioContext.state` peut valoir `"interrupted"` — une valeur que la spécification W3C ne définit pas. **Tout code qui teste `state === "suspended"` pour décider s'il faut reprendre est cassé sur iOS.** Il faut tester `state !== "running"`, et rebrancher la reprise sur un geste puisque `resume()` hors activation transitoire échouera.

### 9.3 Mode silencieux — `<video>` muet contre AudioContext

C'est ici que se joue la différence, et elle est **entièrement déterminée par la catégorie de session audio que WebKit choisit pour la page**.

`[SRC]` `MediaSessionManagerCocoa::updateSessionState()`, `Source/WebCore/platform/audio/cocoa/MediaSessionManagerCocoa.mm` (l. 176-197) :

```cpp
else if (hasAudibleVideoMediaType)          category = AudioSession::CategoryType::MediaPlayback;
else if (hasAudibleAudioOrVideoMediaType)   category = AudioSession::CategoryType::MediaPlayback;
else if (webAudioCount)                     category = AudioSession::CategoryType::AmbientSound;
```

`[SRC]` `AudioSessionIOS::setCategory()`, `Source/WebCore/platform/audio/ios/AudioSessionIOS.mm` (l. 214-249), la traduction vers AVFoundation :

```cpp
case CategoryType::AmbientSound:  categoryString = AVAudioSessionCategoryAmbient;  break;
case CategoryType::MediaPlayback: categoryString = AVAudioSessionCategoryPlayback; break;
```

`[OFF]` Apple, [`AVAudioSession.Category.ambient`](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct/ambient) : « When you use this category, audio from other apps mixes with your audio. **Screen locking and the Silent switch (on iPhone, the Ring/Silent switch) silence your audio.** »

`[OFF]` Apple, [`AVAudioSession.Category.playback`](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct/playback) : « **your app audio continues with the Silent switch set to silent or when the screen locks.** »

| Ce que la page joue | Catégorie retenue | Coupé par le bouton silence ? |
| --- | --- | --- |
| `<video>` **avec piste audio, non muet** | `Playback` | **Non** |
| `<video muted>` **seul** | ni l'un ni l'autre — le muet ne compte pas comme audible | rien à couper |
| **AudioContext seul** | `Ambient` | **Oui — totalement silencieux** |
| AudioContext **+** un `<video>`/`<audio>` audible qui joue | `Playback` | **Non** |

> **Une expérience dont tout le son passe par le Web Audio est muette pour tout utilisateur dont le téléphone est sur silencieux.** Un `<video muted>` ne sauve pas la mise : muet, il ne fait pas passer la session en `Playback`.
>
> **Le seul levier identifié : faire jouer en permanence un élément `<audio>` ou `<video>` réellement audible** (au besoin une piste quasi silencieuse mais **non** muette et à `volume` non nul), ce qui force la catégorie `Playback` pour toute la page, Web Audio compris. `[COM]` Ce montage est déduit du code ci-dessus, pas d'une recommandation Apple ; **à vérifier sur appareil réel avant d'en dépendre**.

`[COM]` Alternative plus propre quand elle suffit : **router tout le son par un unique `<audio>` audible** et ne garder le Web Audio que pour ce qui doit être synthétisé ou spatialisé.

## 10. Décodeurs vidéo simultanés, préchargement, plafonds mémoire

C'est la contrainte qui décide de la stratégie de préchargement. **Elle est mal documentée : Apple ne publie aucun chiffre.** Voici ce qui est établissable, et ce qui ne l'est pas.

### 10.1 Ce qu'aucune source primaire ne donne

`[COM]` **Il n'existe aucun nombre officiel de décodeurs vidéo simultanés sur iOS.** Recherche menée dans le code WebKit (`grep` sur `maxActiveContexts`, `maximumMediaElements`, `concurrent video decoders`, `decoderBudget`, `hardware decoder limit`) : **aucune constante de ce type n'existe côté WebKit**. La limite n'est pas dans le moteur — elle est appliquée par VideoToolbox / le matériel, en dessous.

`[SRC]` La preuve que la limite existe et qu'elle est gérée comme une condition d'exécution normale : `Source/WebCore/platform/graphics/cocoa/WebCoreDecompressionSession.mm` rejette explicitement avec `kVTVideoDecoderNotAvailableNowErr` — le code d'erreur VideoToolbox qui signifie « décodeur indisponible **pour le moment** ».

`[COM]` La seule quantification trouvée est un rapport d'utilisateur, **pas une source Apple** : WebKit Bugzilla [bug 193449, « Multiple playing videos pool needs to be managed by browser »](https://bugs.webkit.org/show_bug.cgi?id=193449), ouvert le **15/01/2019**, sévérité *Critical*, **toujours `NEW` — dernière modification 31/01/2022** :

> « iOS by design can only play `<x>` concurrent videos as decoding is done on hardware. » — « for iPhone 6, it is 32 » — « **If a video is "paused" it still occupies the hardware decoder** » — « on `<x>`+1 video play, the call to `play()` method fails ».

Un commentaire ultérieur (24/11/2019) note que le cas de test **faisait planter** iOS 13.3 beta.

> **À retenir, en étant honnête sur le degré de confiance :** le chiffre « 32 » vient d'un rapporteur de bug en 2019 sur un iPhone 6 ; il ne doit **pas** servir de budget. Ce qui est solide, c'est la **forme** de la contrainte : la ressource est le décodeur matériel, elle est finie, **une vidéo en pause la retient toujours**, et le dépassement se manifeste par un `play()` qui échoue — pas par une dégradation douce. Et le bug est ouvert depuis 2019 : WebKit **ne gère pas** de pool ni d'éviction pour vous.

### 10.2 Ce qui, en revanche, est certain : précharger une vidéo cachée ne marche pas

`[SRC]` `MediaElementSession::preferredBufferingPolicy()`, `MediaElementSession.cpp` (l. 633-663) :

```cpp
if (isSuspended())          return MediaPlayer::BufferingPolicy::MakeResourcesPurgeable;
if (bufferingSuspended())   return MediaPlayer::BufferingPolicy::LimitReadAhead;
if (isPlaying)              return MediaPlayer::BufferingPolicy::Default;
// ...
if (m_elementIsHiddenUntilVisibleInViewport || m_elementIsHiddenBecauseItWasRemovedFromDOM || element->elementIsHidden())
    return MediaPlayer::BufferingPolicy::MakeResourcesPurgeable;
```

> **Un `<video>` qui n'est pas en train de jouer et qui est caché — `display:none`, hors du viewport, retiré du DOM — voit ses ressources marquées *purgeables*.** C'est exactement la configuration dans laquelle on précharge naïvement la cinématique de fin pendant le gameplay. **Le préchargement n'est alors pas garanti** : le système peut reprendre la mémoire à tout moment.

`[SRC]` Sous pression mémoire, la reprise est active et non plus seulement autorisée. `Source/WebCore/page/MemoryRelease.cpp` (l. 168-171) :

```cpp
for (auto& mediaElement : HTMLMediaElement::allMediaElements())
    Ref { mediaElement.get() }->purgeBufferedDataIfPossible();
```

`[SRC]` `HTMLMediaElement::purgeBufferedDataIfPossible()` (l. 10011-10035) passe alors à `BufferingPolicy::PurgeResources` **pour tout élément en pause** (ou piloté par MSE). Un élément qui **joue** est épargné.

`[SRC]` Le mappage vers AVFoundation est explicite dans les `static_assert` de `MediaPlayerPrivateAVFoundationObjC::setBufferingPolicy()` (l. 3699-3727) :

| `BufferingPolicy` WebKit | `AVPlayerResourceConservationLevel` |
| --- | --- |
| `Default` | `None` |
| `LimitReadAhead` | `ReduceReadAhead` |
| `MakeResourcesPurgeable` | `ReuseActivePlayerResources` |
| `PurgeResources` | `RecycleBuffer` |

Et la propriété pilotée est `m_avPlayer.get().resourceConservationLevelWhilePaused` — **« while paused »**. `[COM]` Cela recoupe le rapport du bug 193449 : c'est bien l'état *en pause* qui est le levier de libération des ressources, et WebKit ne l'actionne que si l'élément est **caché ou suspendu**.

**Conséquence opérationnelle** : pour qu'une vidéo reste réellement préchargée, elle doit être **visible** (même à 1×1 px derrière un calque, `opacity` non nulle et pas de `display:none`) ou **en train de jouer**. `[COM]` Ce montage se déduit du code ; il n'est pas documenté par Apple et doit être mesuré sur appareil.

### 10.3 Plafond dur du buffer MSE

`[SRC]` `SettingsBase::defaultMaximumSourceBufferSize()`, `Source/WebCore/page/cocoa/SettingsBaseCocoa.mm` (l. 80-91), commentaire littéral :

```cpp
#if PLATFORM(IOS_FAMILY)
    // iOS Devices have lower memory limits, enforced by jetsam rates, and a very limited
    // ability to swap. Allow SourceBuffers to store up to 105MB each, roughly a third of
    // the limit on macOS, and approximately equivalent to the limit on Firefox.
    return 110376422;
#endif
    return 318767104;
```

**105 Mo par `SourceBuffer` sur iOS, contre 304 Mo ailleurs.** Si l'on passe par Media Source Extensions, c'est le plafond dur de ce qu'on peut tenir en mémoire par piste.

### 10.4 Plafonds mémoire avant éviction d'onglet

`[SRC]` Sur iOS, la « RAM » vue par WebKit **n'est pas la RAM de l'appareil** : c'est la limite jetsam du processus. `Source/WTF/wtf/RAMSize.cpp` :

```cpp
size_t ramSize() { static size_t ramSize = availableMemory(); return ramSize; }
// et, plus bas, une fonction nommée sans ambiguïté :
size_t ramSizeDisregardingJetsamLimit()
```

`[SRC]` `Source/WTF/wtf/AvailableMemory.cpp` (l. 88-98 et 140-151) :

```cpp
static size_t jetsamLimit()
{
    memorystatus_memlimit_properties_t properties;
    if (memorystatus_control(MEMORYSTATUS_CMD_GET_MEMLIMIT_PROPERTIES, getpid(), 0, &properties, sizeof(properties)))
        return 840 * MB;                       // repli quand la requête noyau échoue
    if (properties.memlimit_active < 0) return std::numeric_limits<size_t>::max();
    return static_cast<size_t>(properties.memlimit_active) * MB;
}
// ...
sizeAccordingToKernel = std::min(sizeAccordingToKernel, jetsamLimit());   // arrondi au multiple de 128 Mo supérieur
```

**Le plafond est le `memlimit_active` que le noyau attribue au processus WebContent**, pas la RAM installée. `[SRC]` Le repli codé en dur, **840 Mo**, donne l'ordre de grandeur qu'Apple juge plausible. `[COM]` La valeur réelle varie par appareil et par version d'iOS et **n'est pas publiée** ; on ne peut pas la lire depuis le web.

`[SRC]` Les seuils de réaction, `Source/WTF/wtf/MemoryPressureHandler.cpp` (l. 46-55, 139-175, 377-384) — **plus stricts sur iOS que partout ailleurs** :

| Seuil | iOS | autres plateformes |
| --- | --- | --- |
| `Conservative` | **0,50 × base** | 0,33 × base |
| `Strict` | **0,65 × base** | 0,50 × base |

avec `baseThreshold = min(3 GB, ramSize())` et une scrutation toutes les **30 s** (`s_pollInterval = 30_s`).

`[SRC]` Au-delà, `MemoryPressureHandler` tente de réduire l'empreinte puis, en cas d'échec, tue le processus — trace littérale : `"Unable to shrink memory footprint of process (%zu MB) below the kill thresold (%zu MB). Killed"`. `[COM]` C'est ce qui se manifeste dans Safari par le rechargement silencieux de l'onglet, ou par « A problem repeatedly occurred ».

> **Budget de travail proposé, à valider sur appareil** `[COM]` : viser **≤ 50 % du plafond** pour rester sous le seuil `Conservative`, soit de l'ordre de **400 Mo d'empreinte totale** si l'on retient 840 Mo comme plafond de travail — textures WebGL, buffers vidéo, JS et DOM compris. Ce chiffre est une inférence à partir des constantes ci-dessus, **pas une garantie Apple**.

## 11. WebGL et WebGPU sur iOS Safari

### 11.1 Disponibilité

**WebGL 1 et WebGL 2** : disponibles de longue date sur iOS Safari. `[COM]` Aucune note de version récente n'a été relue pour redater WebGL 2 ; l'affirmation repose sur l'usage courant, pas sur une source primaire.

**WebGPU : disponible.** `[OFF]` [News from WWDC25: WebGPU in Safari](https://webkit.org/blog/16993/news-from-wwdc25-webgpu-in-safari/), WebKit, **09/06/2025** : « WebKit for Safari 26 beta adds support for WebGPU » sur **macOS, iOS, iPadOS et visionOS**. Safari 26 étant diffusé depuis, **WebGPU est disponible sur iOS Safari en août 2026**.

`[COM]` Ce billet **ne dit rien** des limites de mémoire texture, ni du comportement sur matériel ancien, ni d'un plancher de version d'appareil. Aucune source primaire n'a été trouvée sur ces points côté iOS. **À mesurer, pas à supposer.**

### 11.2 La limite qui existe vraiment : le nombre de contextes

`[SRC]` `Source/WebCore/html/canvas/WebGLRenderingContextBase.cpp` (l. 190-191) :

```cpp
static constexpr size_t maxActiveContexts = 16;
static constexpr size_t maxActiveWorkerContexts = 4;
```

`[SRC]` `addActiveContext()` (l. 326-340) : au-delà, WebKit **détruit le contexte le plus ancien** (`recycleContext()`), avec ce message console verbatim :

> « There are too many active WebGL contexts on this page, the oldest context will be lost. »

`[SRC]` Et le point qui fait mal — `recycleContext()` utilise `SyntheticLostContext`, avec ce commentaire :

```cpp
// Using SyntheticLostContext means the developer won't be able to force the restoration
// of the context by calling preventDefault() in a "webglcontextlost" event handler.
```

> **Un contexte perdu par éviction ne peut pas être récupéré par `preventDefault()` dans `webglcontextlost`.** Il faut recréer le contexte et **retéléverser toutes les textures**.

`[SRC]` Cette limite est **la même sur toutes les plateformes** — ce n'est pas une restriction iOS. La restriction iOS, elle, est mémoire (§ 10.4) et thermique (§ 8.3).

### 11.3 Textures sur appareil bas de gamme

`[COM]` **Aucun chiffre primaire trouvé** : ni Apple ni WebKit ne publient de plafond de mémoire texture par appareil, et `MAX_TEXTURE_SIZE` est une valeur d'exécution, pas une constante documentée. Ce qu'on peut affirmer :

- `[SRC]` La perte de contexte WebGL est un chemin de code normal et prévu (`RealLostContext` par le pilote, `SyntheticLostContext` par éviction). **Gérer `webglcontextlost` / `webglcontextrestored` n'est pas un raffinement, c'est une obligation.**
- `[SRC]` WebKit retente la restauration au maximum une fois par seconde (`secondsBetweenRestoreAttempts { 1_s }`).
- `[SRC]` Le budget mémoire textures est prélevé sur la même enveloppe jetsam que tout le reste (§ 10.4) : **une texture de plus, c'est un buffer vidéo de moins.**
- `[SRC]` Et sous mitigation thermique, ce n'est plus le rendu qui casse en premier mais **l'autoplay vidéo** (§ 8.3).

`[COM]` La seule mesure fiable est empirique, sur les appareils de la cible. Aucune API web ne renseigne le niveau de gamme : `WEBGL_debug_renderer_info` est restreint sur iOS, et `deviceMemory` / `hardwareConcurrency` ne sont pas exposés de façon utile par Safari. **Ce trou est réel et doit être comblé par de la mesure terrain.**

---

# Partie C — codecs, navigateurs in-app, réseau

## 12. Codecs et conteneurs

### 12.1 Ce qui est lisible partout, sans condition

**H.264 (AVC) en MP4, profil Main ou High, audio AAC.** `[COM]` Aucune source primaire n'a été relue pour le redater — c'est le socle depuis quinze ans, décodé matériellement sur tout iPhone et tout Android livré avec les services Google. **C'est le seul format sur lequel on peut s'engager sans conditionnel.**

### 12.2 HEVC (H.265)

| Plateforme | État | Source |
| --- | --- | --- |
| iOS Safari | Pris en charge, décodage matériel | `[OFF]` implicite dans les notes Safari 17.4 (« Fixed an HEVC decoder issue when translating annexb data ») |
| Chrome / WebView Android | **Décodage matériel activé depuis M107** | `[OFF]` chromestatus, « Enable HEVC hardware decoding », *Enabled by default*, **M107 desktop, Android et WebView** — « Enables support for decoding HEVC video on platforms where hardware [...] for decoding HEVC is available » |

> **Le HEVC est le meilleur compromis en 2026 : ~30-50 % de poids en moins qu'H.264 à qualité égale, décodage matériel des deux côtés.** `[COM]` Mais sur Android il dépend de la présence d'un décodeur matériel sur l'appareil — chromestatus le dit littéralement (« on platforms where hardware [...] is available »). **Il faut donc un repli H.264.**

### 12.3 AV1 — le piège

`[OFF]` chromestatus, « AV1 Decoder » : *Enabled by default* depuis **Chrome 70**, mais **desktop uniquement** — Windows, macOS, Linux, ChromeOS. **Android : non pris en charge.** Même chose pour l'encodeur (M90, desktop). AVIF sur Android est explicitement « gated on a DFM for the AV1 decoder ». Seul WebRTC a AV1 sur Android (M111).

`[OFF]` Côté Apple, [notes de Safari 17](https://developer.apple.com/documentation/safari-release-notes/safari-17-release-notes) (septembre 2023) : « **Added support for AV1 codec support to the MediaCapabilities API for devices with hardware support.** » — c'est-à-dire uniquement les appareils dotés d'un décodeur AV1 matériel.

> **Verdict : AV1 n'est pas un format de livraison sur mobile en 2026.** Il est absent de Chrome Android pour `<video>` selon chromestatus, et sur iOS il est réservé au matériel récent. `[COM]` Il est possible que le décodage matériel AV1 fonctionne sur certains Android via les décodeurs de plateforme sans que chromestatus le reflète — **cela n'a pas pu être vérifié sur source primaire, et ne doit pas être supposé.**

### 12.4 VP9 / WebM

`[OFF]` Notes de [Safari 17.4](https://developer.apple.com/documentation/safari-release-notes/safari-17_4-release-notes) (mars 2024) : « **Added support for VP8/VP9 and WebM on iOS and iPadOS.** (64825245) » et « Added support for the Vorbis audio codec on iOS, iPadOS, and in visionOS. »

`[COM]` VP9 est donc lisible des deux côtés depuis iOS 17.4, mais **le décodage matériel sur iOS n'est pas garanti** — Apple ne le dit nulle part, et un décodage logiciel de VP9 sur un long plan est exactement ce qui déclenche la mitigation thermique du § 8.3. À écarter pour les cinématiques.

### 12.5 Le choix de priorité fait par le moteur

`[OFF]` Notes de Safari 17.4 : « **Added prioritizing video sources with power efficient hardware-decoded codecs before software-decoded codecs.** (120679553) »

`[COM]` Autrement dit : **lister plusieurs `<source>` fonctionne**, et Safari 17.4+ choisit le codec décodé matériellement plutôt que le premier de la liste. Combiné à `MediaCapabilities.decodingInfo()` (`powerEfficient`), c'est le mécanisme correct de sélection.

### 12.6 Impact sur le poids des maîtres

`[COM]` Aucune source primaire ne chiffre le gain HEVC/H.264 ; les ordres de grandeur usuels (30-50 %) sont des résultats d'encodage, pas des affirmations d'éditeur. **Ce qui est sourcé, ce sont les contraintes qui encadrent ce poids :**

- `[SRC]` **105 Mo par `SourceBuffer` MSE sur iOS** (§ 10.3) — plafond dur si l'on passe par MSE.
- `[SRC]` **`MediaDataLoadsAutomatically` vaut `false` sur iOS** (§ 14.1) — le préchargement n'a pas lieu avant le geste, quel que soit `preload`.
- `[SRC]` **Une vidéo cachée voit ses ressources marquées purgeables** (§ 10.2) — un maître lourd préchargé peut être jeté.

> **Recommandation de livraison** `[COM]` : deux maîtres seulement — **HEVC/MP4** en premier `<source>`, **H.264/MP4** en repli — et pas d'AV1, pas de VP9. Le troisième encodage coûte plus cher qu'il ne rapporte.

## 13. Cartographie par application — quel moteur sert vraiment le lien

### 13.1 iOS : c'est toujours WebKit, et c'est une règle contractuelle

`[OFF]` [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), guideline **2.5.6**, verbatim, page consultée le 20/08/2026 :

> « Apps that browse the web must use the appropriate WebKit framework and WebKit JavaScript. **You may apply for an entitlement to use an alternative web browser engine in your app.** Learn more about these entitlements for the **EU and Japan**. »

> **L'hypothèse « ces apps utilisent le moteur système et non un Chromium embarqué » est VALIDÉE sur iOS, par une règle contractuelle publiée.** Un navigateur in-app dans TikTok, Instagram, WhatsApp ou Snapchat rend en WebKit. Aucun de ces éditeurs n'est un navigateur web ; l'exception d'entitlement UE/Japon vise les moteurs de navigateurs alternatifs et ne s'applique pas à eux.
>
> **Nuance 2026 à surveiller** : la dérogation UE/Japon existe désormais dans les guidelines. Elle ouvre la porte, à terme, à des moteurs non-WebKit sur iOS. `[COM]` Rien n'indique qu'une de ces quatre applications l'ait demandée.

**Reste à savoir lequel des deux conteneurs WebKit** — et la différence est énorme.

`[OFF]` [`SFSafariViewController`](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) : « Interactions with the web interface aren't visible to your app, and **you can't access AutoFill data, browsing history, or website data.** » ; « The web interface supports Safari features such as Reader, AutoFill, Fraudulent Website Warning, and content blocking. » ; « You can't customize or interact with the web content » — si l'app veut le faire, elle **doit** utiliser `WKWebView`.

> **`SFSafariViewController` ≈ Safari.** Mêmes capacités, mêmes cookies, l'app hôte ne voit rien. C'est l'équivalent iOS des Custom Tabs Android (§ 5).
>
> **`WKWebView` est un conteneur configuré par l'app hôte**, et ses défauts sont hostiles (§ 13.2).

`[COM]` **Critère de discrimination, applicable sans source :** une application qui **injecte du JavaScript** dans la page, qui **surveille les saisies**, qui affiche une **barre d'outils personnalisée** avec ses propres actions, ou qui **réécrit les liens**, est nécessairement en `WKWebView` — la documentation Apple ci-dessus l'établit, puisque `SFSafariViewController` interdit tout accès au contenu.

`[COM]` **Quelle application utilise quoi, nommément : non établi sur source primaire.** Aucune de ces quatre entreprises ne documente son conteneur, et l'introspection à distance est impossible. **Ce trou n'est pas comblé** ; il doit l'être par mesure sur appareil (§ 13.3).

### 13.2 Les défauts hostiles de `WKWebView` — l'équivalent iOS du tableau `WebSettings`

`[SRC]` `Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml`, valeurs par défaut de la cible `WebKit` (c'est-à-dire `WKWebView`), branche `main` au 20/08/2026 :

| Préférence | Défaut iOS | Défaut ailleurs | Conséquence |
| --- | --- | --- | --- |
| **`AllowsInlineMediaPlayback`** | **`false`** | `true` | **toute vidéo part dans le lecteur plein écran natif** |
| **`MediaDataLoadsAutomatically`** | **`false`** | `true` | **aucun préchargement média avant un geste** |
| `RequiresUserGestureForAudioPlayback` | **`true`** | `false` | geste requis pour tout son |
| `RequiresUserGestureForVideoPlayback` | `false` | `false` | vidéo muette autorisée — *sauf* mode éco / thermique (§ 8.3) |
| `RequiresUserGestureToLoadVideo` | `true` (cible `WebCore`) | `false` | charger l'octet 0 demande un geste |

`[OFF]` Apple confirme le premier point mot pour mot — [`WKWebViewConfiguration.allowsInlineMediaPlayback`](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/allowsinlinemediaplayback) :

> « **The default value of this property is `false` for iPhone and `true` for iPad.** » et « When adding a video element to an HTML document on iPhone, you must also include the `playsinline` attribute. » — avec la note : « Apps created before iOS 10.0 must use the `webkit-playsinline` attribute. »

> **C'est le miroir exact du problème Android du § 4, mais inversé.**
> Sur Android, l'échec est que **`requestFullscreen()` ne fait rien**.
> Sur iOS, l'échec est que **la vidéo passe en plein écran natif qu'on le veuille ou non**, si l'application hôte n'a pas mis `allowsInlineMediaPlayback = true`.
>
> Dans les deux cas **le site ne peut rien** : on ne peut ni forcer le plein écran sur Android, ni l'empêcher sur iOS. Et le lecteur natif iOS **détruit toute composition** : plus d'overlay, plus de 3D par-dessus, plus d'UI.

`[SRC]` La conséquence de `MediaDataLoadsAutomatically = false` est directe : `MediaElementSession` reçoit `AutoPreloadingNotPermitted` (§ 8.3), donc **`preload="auto"` est ignoré**. C'est la version moderne et sourcée de l'affirmation périmée de 2012 (§ 8.1) : ce n'est pas « le cellulaire » qui coupe le préchargement, c'est un défaut de plateforme.

### 13.3 Android : comment vérifier soi-même, faute de source

`[COM]` **L'hypothèse « WebView système, pas de Chromium embarqué » n'a PAS pu être validée sur source primaire pour Android.** Aucun de ces quatre éditeurs ne publie son architecture, et il n'existe pas d'équivalent Android à la guideline 2.5.6 qui l'imposerait. **Tout le § 2 à § 4 reste conditionné à cette hypothèse.**

Ce qui est vérifiable, en revanche, c'est **la signature**. `[SRC]` `chromium/chromium`, `android_webview/browser/aw_content_browser_client.cc`, fonction `GetUserAgent()`, branche `main` :

```cpp
std::string GetUserAgent() {
  // "Version/4.0" had been hardcoded in the legacy WebView.
  std::string product = "Version/4.0 " + GetProduct();
  ...
  // The "Linux; Android 10; K; wv" string matches the
  // expected format for a reduced WebView User-Agent.
  constexpr char kUnifiedPlatformOsInfoWebview[] = "Linux; Android 10; K; wv";
```

Deux marqueurs, tous deux absents de Chrome pour Android :

1. le jeton **`wv`** dans la section plateforme du User-Agent ;
2. le préfixe **`Version/4.0 `** devant `Chrome/…`.

> **Protocole de validation, à exécuter avant de figer l'architecture** `[COM]` : publier une page de sonde, ouvrir le lien depuis chacune des quatre applications, sur iOS et sur Android, et journaliser `navigator.userAgent`, le résultat de `document.documentElement.requestFullscreen()`, la présence de `window.localStorage`, la valeur de `audioContext.state` après un tap, et le comportement d'un `<video playsinline>` — plein écran ou non. **Une demi-journée de travail qui remplace huit hypothèses.**

## 14. Réseau

### 14.1 Le préchargement n'a pas lieu sur iOS avant un geste

`[SRC]` `UnifiedWebPreferences.yaml` :

```yaml
MediaDataLoadsAutomatically:
  defaultValue:
    WebKit:
      "PLATFORM(IOS_FAMILY)": false
      default: true
```

`[SRC]` Ce réglage pose `MediaElementSession::AutoPreloadingNotPermitted`, levée seulement par `removeBehaviorRestrictionsAfterFirstUserGesture()` (§ 8.4).

`[COM]` Le fichier donne le défaut pour l'API embarquée (`WKWebView`). **Safari lui-même peut surcharger ce réglage ; le fichier ne permet pas de le dire.** À vérifier sur appareil. Ce qui est certain, c'est que **dans tout navigateur in-app iOS, rien n'est préchargé avant le premier tap.**

### 14.2 `Save-Data` : utilisable sur Android, inexistant sur iOS

`[OFF]` chromestatus : « HTTP Client Hints: Save-Data », *Enabled by default* depuis **Chrome 49**, toutes plateformes ; formalisé en client hint avec la permissions policy `CH-Save-Data` en **Chrome 102**.

`[SRC]` Côté WebKit, une recherche sur `Save-Data` dans `WebKit/WebKit` ne renvoie **que des fichiers de test importés de web-platform-tests** — aucune implémentation. **Safari n'envoie pas `Save-Data`.**

`[OFF]` Et ce n'est pas un oubli. [WebKit Tracking Prevention](https://webkit.org/tracking-prevention/) liste les API « we have decided to not yet implement due to fingerprinting, security, and other concerns », parmi lesquelles :

- **Network Information API** → `navigator.connection`, `effectiveType`, `downlink`, `rtt` : **indisponibles sur Safari**
- **Device Memory API** → `navigator.deviceMemory` : **indisponible**
- Battery Status API, Web Bluetooth, Web MIDI, WebHID, Serial, Web USB, Web NFC, User Idle Detection

`[OFF]` La demande explicite d'une détection grossière du mode économie d'énergie — [WebKit/standards-positions#353](https://github.com/WebKit/standards-positions/issues/353), ouverte le **13/07/2020**, proposant précisément « detecting (in JS or in an HTTP header such as `Save-Data: On`) whether the user agent's device is currently in power saving mode » — a été **fermée avec le label `invalid` le 07/07/2026**, soit six semaines avant cette recherche.

`[OFF]` `prefers-reduced-data` (chromestatus) est au stade **« Start prototyping »**, avec « No signal » de Firefox et Safari. **Ce n'est pas une option.**

> **Sur iOS, on ne sait rien du réseau ni de l'appareil.** Ni le type de connexion, ni le débit, ni la RAM, ni le mode économie d'énergie. **Toute adaptation doit être mesurée par le site lui-même** — chronométrer le premier segment téléchargé et adapter ensuite — ou être décidée à l'avance de façon conservatrice.

### 14.3 Autoplay Chrome Android, pour mémoire

`[OFF]` [Autoplay policy in Chrome](https://developer.chrome.com/blog/autoplay), **dernière mise à jour affichée : 13/09/2017** — obsolète en apparence, mais toujours la page normative de Chrome :

> « Muted autoplay is always allowed. Autoplay with sound is allowed if: The user has interacted with the domain (click, tap, etc.). **On desktop**, the user's Media Engagement Index threshold has been crossed [...] The user has added the site to their home screen on mobile or installed the PWA on desktop. »

**Le Media Engagement Index est desktop uniquement.** Sur Android, l'autoplay sonore exige une interaction avec le domaine — ou une PWA installée. Et la recommandation de la page reste juste : « Don't assume a video will play, and don't show a pause button when the video is not actually playing. »

`[SRC]` En WebView, c'est plus strict encore : `setMediaPlaybackRequiresUserGesture` vaut `true` par défaut (§ 2), donc **même l'autoplay muet est bloqué** tant que l'app hôte n'a pas fait l'opt-in.

### 14.4 Ce qu'un préchargement agressif coûte

`[COM]` Aucune source primaire ne chiffre le coût en données d'une stratégie de préchargement — c'est une propriété du contenu, pas de la plateforme. Ce que les sources établissent, c'est **pourquoi le préchargement agressif est structurellement perdant sur mobile** :

1. `[SRC]` Sur iOS il **n'a pas lieu** avant le premier geste (§ 14.1).
2. `[SRC]` Une fois lancé, s'il vise un élément **caché**, ses ressources sont **purgeables** (§ 10.2) — on paie les octets sans garantie de les garder.
3. `[SRC]` Sous pression mémoire, WebKit **purge activement** tous les éléments en pause (§ 10.2) — on paie les octets et on les perd.
4. `[SRC]` Chaque `<video>` prêt retient un décodeur matériel, même en pause (§ 10.1) — et le `play()` de trop échoue.
5. `[OFF]` Sur iOS **on ne peut pas savoir** qu'on est en 4G médiocre (§ 14.2) — donc on ne peut pas décider de s'abstenir.

> **Conclusion : la seule stratégie de préchargement défendable est séquentielle et juste-à-temps** — précharger la ressource *suivante*, une seule, pendant que la courante joue, et jamais les trois d'un coup.

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
