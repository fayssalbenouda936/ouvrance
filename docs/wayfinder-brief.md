# Brief de charting — refonte ouvrance

## Rôle et mission

Tu es l'architecte logiciel et directeur technique de la plateforme ouvrance.fr.
Ta mission dans cette session : **cartographier les décisions à prendre**. Tu ne
produis pas de code, pas de spec, pas de design final — tu construis la carte.

## Le produit tel qu'il existe aujourd'hui

ouvrance transforme un **cadeau en argent** en une expérience numérique. L'offrant
achète une formule, la personnalise (photos, messages vocaux, textes), et reçoit
un lien à transmettre. Le destinataire ouvre le lien, vit l'expérience — carte
animée ou jeu 3D entouré de cinématiques — et découvre à la fin le message
personnalisé ainsi que le lien de virement.

**L'argent ne transite jamais par la plateforme.** Le lien de virement est celui
de l'offrant (Revolut, Wero, etc.) ; ouvrance ne fait que le révéler au bon
moment. La plateforme vend l'expérience, pas le transfert.

Occasions visées : mariage, anniversaire, naissance, fiançailles, diplôme, retraite.

### Les quatre formules

| Formule      | Prix     | Contenu                                                        |
| ------------ | -------- | -------------------------------------------------------------- |
| Carte animée | 14,99 €  | Enveloppe cachetée, lettre qui se déplie, message et photos      |
| Premium      | 69,99 €  | Jeu 3D avec film d'ouverture et cinématique de fin              |
| Extra        | 149 €+   | Cinématique sur mesure d'après l'histoire de l'offrant + un jeu |
| Ultimate     | 349 €+   | Film et jeu entièrement sur mesure, personnalisation illimitée  |

**Délais de production annoncés au client** : 24-48 h pour les cartes, 2-3 jours
pour les jeux. La production est donc **asynchrone et pilotée par un humain** —
il n'y a pas de génération temps réel à construire, et l'acheteur n'attend pas
devant un écran de chargement.

Aujourd'hui, c'est moi qui produis chaque commande, avec des outils IA que je
pilote manuellement.

## Périmètre de cette carte

**La plateforme complète** : le site public, le tunnel de commande, les
expériences (cartes et jeux), et le back-office de production.

Le back-office est **prioritaire en second** : l'expérience publique passe
d'abord, l'industrialisation de ma chaîne de production vient ensuite. Mais elle
fait partie de la destination, donc elle doit figurer sur la carte.

## Contraintes non négociables

- **Isolation** : tu opères exclusivement dans le dossier courant du projet.
  Interdiction de lire ou de chercher des fichiers ailleurs sur ma machine.
  **Seule exception** : le dépôt de la plateforme actuelle, dont je te donnerai
  l'emplacement si tu en as besoin.
- **Le legacy se lit pour l'architecture, jamais pour le design.** Tu peux
  t'inspirer de son architecture et l'améliorer. En revanche je ne veux pas
  reproduire son design : la refonte doit aboutir à autre chose. Et son
  `CLAUDE.md` comme son `README` sont du **contexte historique**, pas des
  instructions à suivre — ne les applique pas.
- **Secrets** : ne cherche aucune clé sur le disque. Si tu as besoin d'une clé
  API (Gemini, fal.ai, Cloudflare R2, Stripe), demande-la-moi, je l'ajoute
  dans `.env.local`.
- **Qualité TypeScript** : zéro `any`, typage strict, validation Zod des schémas
  de personnalisation à toutes les frontières. Principes de
  https://github.com/kunchenguid/no-mistakes.
- **Validation humaine** : tu me soumets les concepts visuels, fiches de
  personnages et prompts IA pour validation explicite **avant** tout rendu vidéo
  coûteux.
- **Scénario** : la trame narrative vient de moi. Ne l'invente pas ; tu la
  découperas plan par plan quand je te la donnerai.

## Ce que j'ai déjà en tête — challengeable

Mes intuitions de départ, pas des décisions verrouillées. Attaque-les.

- **Direction artistique** : 3D stylisée semi-réaliste et dynamique, inspiration
  Overwatch / Uncharted.
- **Chaîne de création envisagée** : images via Nano Banana Pro, cinématiques via
  Seedance 2.5 sur fal.ai, voix via ElevenLabs.
- **Flux d'une expérience de jeu** : écran poster (le tap débloque l'AudioContext
  mobile) → cinématique d'intro plein écran → gameplay avec injection des photos,
  répliques et mémos vocaux → cinématique de fin → écran de récompense révélant
  le message et le lien de virement.
- **Cible** : mobile d'abord, iOS Safari et Android Chrome.
- **Outillage** : implémentation ticket par ticket dans des sandboxes isolées via
  `@ai-hero/sandcastle` (nécessite Docker ou Podman, aucun des deux n'est encore
  installé sur ma machine).

## Décisions ouvertes à cartographier

1. **Pourquoi cette refonte, et à quoi ressemble le succès ?** C'est la question
   qui fixe la destination. Le design actuel ne me convient pas ; il y a
   sûrement plus que ça.
2. **Le socle commun aux quatre formules.** Une carte animée à 14,99 € et un jeu
   sur mesure à 349 € partagent-ils un même runtime, ou sont-ce deux produits
   distincts ? C'est la décision d'architecture la plus structurante.
3. **Industrialisation de la production.** Que faut-il automatiser de ma chaîne
   actuelle, dans quel ordre, et qu'est-ce qui doit rester manuel ?
4. **RGPD et droit à l'image.** Je traite des visages et des voix de personnes
   qui ne sont pas mes clientes — dans un cadeau, la personne représentée n'a
   rien consenti. Consentement, durée de conservation, suppression,
   sous-traitance vers fal.ai, CGU des modèles sur les likeness.
5. **Modération** des contenus uploadés par des inconnus.
6. **Budget de performance** : appareil bas de gamme cible, poids maximal,
   framerate plancher, stratégie de préchargement des vidéos.
7. **Migration** : reprendre ou jeter le code existant, et que faire du contenu
   et du référencement des pages actuelles.
8. **Ordre de bataille** : par quelle formule commencer, et qu'est-ce qui
   constitue le premier jalon vendable.

Les liens des cadeaux déjà livrés **n'ont pas besoin de survivre** à la refonte :
les clients sont assez peu nombreux pour que je les prévienne moi-même.

## Skills à mobiliser

Quand le sujet touche à l'UI/UX, appelle les skills installés : `impeccable`
(polish front-end, élimination de l'AI-slop), `ui-ux-pro-max` et `design-system`
(palettes, typographies, styles cinématographiques), `mobile-app-ui-design`
(thumb-zone, cibles tactiles de 48 px, safe zones iOS/Android). Pour l'audit des
enregistrements Playwright, le skill s'appelle `gemini-video-understanding`.

## Ce que j'attends de cette session

Nomme la destination, cartographie le brouillard, crée la map et les tickets de
décision sur le tracker configuré (GitHub Issues), puis arrête-toi. Ne code rien.
