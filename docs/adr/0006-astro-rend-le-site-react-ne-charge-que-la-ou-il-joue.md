# Astro rend le site, React ne charge que là où il joue

Le site refondu est une **application Astro unique**, déployée en **Worker Cloudflare** avec assets statiques, sur R2 en juridiction `eu`. React n'est chargé qu'en îlots, sur les trois routes où quelque chose se joue : le formulaire de commande, le lecteur de cadeau, l'atelier. Les panneaux de vente n'exécutent rien.

La frontière serveur a trois primitives et une règle.

- **Actions Astro** — tout ce que le navigateur appelle sous contrat typé, entrée validée par un schéma Zod.
- **Endpoints bruts** — les deux cas qu'une Action ne peut pas porter : le webhook Stripe, qui vérifie sa signature sur le corps non parsé, et le service des dérivés, qui streame avec `Range`.
- **Cron Trigger** — la purge des commandes non payées à 24 h.

La règle : **aucune écriture d'état de paiement ne vient du navigateur.**

## Pourquoi

**Parce que la page qui vend est celle qui ne doit rien exécuter.** Le visiteur arrive de TikTok sur un panneau dont le fond est un teaser vidéo, et le destinataire ouvre un lien depuis une messagerie : ce sont deux démarrages à froid sur mobile, et ce sont eux qui décident de la conversion. Un framework React de bout en bout fait payer son runtime sur cette page-là. Le bénéfice qu'on serait allé y chercher — une frontière serveur typée — les Actions Astro le donnent, en validant leur entrée par un schéma : la ligne « Zod aux frontières » cesse d'être une discipline pour devenir une propriété du framework.

**Parce que React Three Fiber n'impose React que sur une route.** Le moteur 3D est une dépendance du lecteur, pas du site. Un îlot `client:only` est déjà un bundle séparé ; en faire une seconde application coûterait deux builds et deux déploiements pour un gain nul.

**Parce que les Pages Functions vivaient à côté de l'application, hors de son système de types.** Ce n'est pas une objection théorique : c'est très exactement pourquoi `/api/paiement` a pu marquer une commande payée sur un simple POST du navigateur, en parallèle d'un webhook Stripe par ailleurs correctement signé. La vérité du paiement avait deux sources, dont une anonyme. Un Worker ramène le serveur dans le code de l'application, typé et testable.

**Parce que la purge à 24 h exige un cron et non un webhook.** La contrainte vient de l'étude RGPD ; les Cron Triggers d'un Worker la portent nativement.

## Conséquences

- **Cloudflare et R2 sont conservés**, la juridiction `eu` avec eux. Le build cible **Workers** et non Pages : le répertoire `functions/` disparaît.
- **`/api/paiement` est supprimé sans remplaçant.** La page `/merci` lit un état, elle ne l'écrit jamais.
- **Le Payment Link cède la place à une Checkout Session créée côté serveur** : le supplément rend le montant calculé, `expires_at` adosse la purge au plafond Stripe, `client_reference_id` rattache la session à la Commande dès sa création. L'ancien lien à 49,99 € meurt avec le mécanisme.
- **L'atelier passe derrière Cloudflare Access.** `CLE_ATELIER` — un secret partagé voyageant dans la barre d'adresse, devant une console qui voit les photos et les messages de tous les clients — disparaît. Aucune ligne d'authentification à écrire.
- **Brevo est le seul chemin d'email.** Le domaine `send.ouvrance.fr` y est déjà authentifié ; Resend et Formspree sont retirés, le second faute de DPA. Le repli en cascade était une fausse robustesse : la Commande est persistée avant l'envoi, donc l'échec d'un email ne perd rien.
- **Dépôt unique, une seule application, aucun workspace pnpm.** La couture qui compte — le noyau ignore le schéma de personnalisation — est tenue par le registre et par une règle de lint qui interdit au noyau d'importer une expérience, vérifiée en intégration continue. Promouvoir un dossier en package reste possible le jour où ça fait mal.
- **La porte de qualité est bloquante en intégration continue** — `typecheck`, `lint`, `test`, `build` — et Playwright n'y est pas : son usage est l'audit visuel, pas la garde de fusion.
- **Les secrets vivent dans `wrangler secret` en production et `.dev.vars` en local** — la convention Workers, et non le `.env.local` que supposaient les notes.
- **La bascule sur ouvrance.fr est atomique.** Le Worker se construit sur un domaine de préversion et ne prend le domaine que lorsqu'il sait déjà vendre la carte animée. Aucune cohabitation, aucune règle de routage à écrire puis à jeter.
