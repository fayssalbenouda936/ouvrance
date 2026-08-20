# Chaîne de sous-traitance — audit RGPD sur sources primaires

**Recherche partielle du ticket [#4](https://github.com/fayssalbenouda936/ouvrance/issues/4).** Toutes les pages consultées le **20 août 2026**. Registre DPF interrogé via l'API publique du site officiel (`dpfapi.azurewebsites.net/api/participants`, backend de dataprivacyframework.gov/list).

Ce document couvre **les sous-traitants de la plomberie** (hors fal.ai, traité à part). Le volet RGPD / doctrine CNIL / droit à l'image français reste à faire.

## 1. Tableau récapitulatif

| Fournisseur | Rôle RGPD | DPA public | Signature requise | Localisation | DPF vérifié au registre | Liste sous-traitants |
| --- | --- | --- | --- | --- | --- | --- |
| **Cloudflare** (R2, Workers) | Sous-traitant | Oui — v6.4, eff. 03/04/2026 | Non, incorporé par référence | Global ; R2 `jurisdiction=eu` = **stockage** UE garanti ; cache et exécution non couverts | **Active** (EU-US + Swiss + UK) | [lien](https://www.cloudflare.com/gdpr/subprocessors/cloudflare-services/) |
| **Stripe** | **Double rôle** : sous-traitant **et responsable autonome** | Oui — MàJ 18/11/2025 | Non | Transfert explicite vers **Stripe, LLC (USA)** ; contrat avec **Stripe Payments Europe (Irlande)** | **Active** (cert. 11/05/2026 → 11/05/2027) | [lien](https://stripe.com/legal/service-providers) |
| **Brevo** | Sous-traitant | Oui — Appendix 3 des CGU, 01/10/2025 | Non | **UE** : OVH (France) + GCP (Belgique) | Filiale US **Active** depuis 26/02/2026 (support seul) | Annexe 2 des CGU |
| **Resend** | Sous-traitant | Oui — MàJ 31/12/2025 | Non | **États-Unis**, y compris avec région d'envoi `eu-west-1` | **Active - Re-certification under Review** (pas de Swiss) | [lien](https://resend.com/legal/subprocessors) — **22 sous-traitants, tous aux USA** |
| **Formspree** | Se présente comme sous-traitant, **sans contrat publié** | **Non — 404** | Sans objet | **AWS États-Unis** | **NON — « Inactive - Withdrawal » depuis le 26/04/2022** | **Aucune** |
| **GitHub** | Sous-traitant | Oui — eff. oct. 2025 | Non | USA + mondial | **Active** | [lien](https://github.com/subprocessors) |

---

## 2. Cloudflare — que garantit vraiment `jurisdiction = "eu"` ?

Source : [data-location](https://developers.cloudflare.com/r2/reference/data-location/) (MàJ 19/08/2026).

> « **Jurisdictional Restrictions guarantee objects in a bucket are stored within a specific jurisdiction.** »
> « Use Jurisdictional Restrictions when you need to ensure data is **stored and processed** within a jurisdiction to meet data residency requirements, including local regulations such as the GDPR »
> « Once an R2 bucket is created, the jurisdiction cannot be changed. »

Endpoint S3 : `https://<ACCOUNT_ID>.eu.r2.cloudflarestorage.com`. Binding Workers : `jurisdiction = "eu"`.

**Une seule limitation est listée** sur cette page : Logpush n'interagit pas avec les buckets à juridiction.

**Réponse honnête : oui, les objets au repos sont garantis stockés dans l'UE — mais la page ne dit rien du cache, des métadonnées, des logs ni du lieu d'exécution du code.** Ces trous sont comblés ailleurs, et ils comptent :

1. **Cache CDN hors UE.** [public-buckets](https://developers.cloudflare.com/r2/buckets/public-buckets/) (16/06/2026) : un domaine personnalisé « allows you to use **Cloudflare Cache** ». Le cache est mondial : des copies des objets peuvent résider hors UE.
2. **Exécution du code hors UE.** [data-localization/workers](https://developers.cloudflare.com/data-localization/how-to/workers/) (23/07/2026), verbatim : « Regional Services restricts where Workers are executed [...] However, **Workers code and secrets are deployed globally to all Cloudflare data centers.** [...] Regional Services does not extend to outgoing **subrequests** ». Sans Regional Services, un Worker s'exécute au data center le plus proche du visiteur.
3. **Métadonnées, logs, analytics** relèvent du **Customer Metadata Boundary** — [data-localization](https://developers.cloudflare.com/data-localization/) (05/05/2026) qualifie toute la suite d'« **Enterprise-only paid add-on** ». Un compte self-serve n'y a pas accès.
4. **Chiffrement** : « All objects stored in R2, **including their metadata**, are encrypted at rest » (AES-256 GCM), clés gérées par Cloudflare.

> **Conclusion opérationnelle** : `jurisdiction=eu` est une vraie garantie de résidence **du stockage**, à documenter comme telle dans le registre des traitements. Ce n'est **pas** une garantie de non-traitement hors UE. Pour un flux de photos et de vocaux, **garder le bucket privé** (URL présignées ou Worker, jamais de bucket public en cache) réduit fortement l'exposition.

**DPA** : [v6.4](https://www.cloudflare.com/cloudflare-customer-dpa/), auto-accepté via les CG self-serve (6.1 : « hereby incorporated by reference »). CCT Décision **2021/914**, Module Two ou Three, clause d'amarrage activée. DPF : clause 6.4, « Cloudflare will notify Customer if its Data Privacy Framework certification lapses ». Sous-traitants : préavis **30 jours**, objection sous **10 jours** ; liste MàJ 01/10/2025 (Slack, Zendesk, Salesforce, Google, Oracle, AWS, CoreWeave, Nebius, **Anthropic, OpenAI, X.AI, Groq**). Rétention : suppression ou restitution au choix du client ; **aucune durée fixe pour les objets R2 — c'est vous qui pilotez le cycle de vie.**

---

## 3. Stripe — attention au double rôle

[DPA](https://stripe.com/legal/dpa), MàJ **18/11/2025**. Auto-accepté (« subject to and forms part of the Agreement »).

**Entité contractante pour un vendeur français** : « If User's Stripe Account is located in North America or South America, User enters this DPA with Stripe, LLC. **If User's Stripe Account is located elsewhere, User enters this DPA with Stripe Payments Europe, Limited** » → **Irlande**.

**Responsable de traitement autonome pour la lutte anti-fraude : OUI, explicitement.** Section « Stripe as a Data Controller » : Stripe « has the **sole and exclusive authority to determine the purposes and means** of Processing Personal Data it receives from or through User ». Finalités listées en tant que responsable : « **monitor, prevent and detect fraudulent transactions** [...] **comply with Law, including applicable anti-money laundering screening and know-your-customer obligations** [...] **analyze, improve and develop Stripe's products and services** ».

> **Conséquence pratique** : pour ces finalités, Stripe n'agit **pas** sur nos instructions. La politique de confidentialité doit le dire : « Stripe agit comme responsable de traitement indépendant pour la prévention de la fraude ».

**Localisation** : « User acknowledges that in order for Stripe to provide the Services, **User transfers Personal Data to Stripe, LLC in the United States**. » **Aucune option de résidence UE.** CCT 2021/914 Modules 1 **et** 2 (le Module 1 confirme le double rôle). DPF vérifié Active.

**Sous-traitants** : notification 30 jours, objection sous 30 jours — mais « Stripe will not be obligated to provide User the Services for which Stripe uses that Sub-processor ». **Rétention** : suppression au choix, sauf conservation « required or authorized by DP Law » — les obligations LCB-FT imposent plusieurs années côté responsable autonome.

---

## 4. Brevo — le seul hébergement réellement européen

Entité : **Sendinblue SAS**, RCS Paris 498 019 298, 9-17 rue Salneuve 75017 Paris. « Only the English language version of these Terms is binding. »

**Le DPA n'a pas d'URL propre** (`/legal/dpa` = 404) : c'est l'**Appendix 3 des [Terms of Service](https://www.brevo.com/legal/termsofuse/)**, version **1er octobre 2025**. « the parties agree that **We act as Processor and You act as Controller** [...] In some cases where You act as Processor for an end-user, We will act as subprocessor. »

**Hébergement UE** (Annexe 2) : **OVH**, France, **serveurs France** ; **Google Cloud Platform**, entité France, **serveurs Belgique**. S'y ajoutent Cloudflare (CDN/WAF, avec mention de la Data Localization Suite), Zendesk (support, EU/USA), Omni (dashboards, EU).

**Transferts** : « We may rely on the **EU-US Data Privacy Framework** [...] as long as this framework remains valid. » La filiale **Brevo, Inc.** (raison sociale au registre : « Seninblue, Inc. », Austin TX) est **Active** depuis le 26/02/2026, objet déclaré : **support client uniquement** — « This processing does not involve any hosting of personal data by Brevo, Inc. in the US. »

**Rétention** : « **You** [...] and not Brevo, are responsible for managing the retention periods. » Suppression sur demande **sous 3 mois** après résiliation ; suppression automatique du compte après **6 mois** d'inactivité.

---

## 5. Resend — pas de résidence UE, et le contenu des emails est lisible

[DPA](https://resend.com/legal/dpa), MàJ **31/12/2025**. Entité : **Plus Five Five, Inc.** Auto-accepté. CCT **2021/914** Module Two, annexées.

**Le point important** — [regions](https://resend.com/docs/dashboard/domains/regions), verbatim :

> « **Region selection controls where your emails are routed and sent from. It does not control where customer data is stored.** All account data, including email metadata, logs, and API records, **is stored in the United States regardless of the sending region you select.** Choosing `eu-west-1` means your emails are dispatched from Ireland, but your Resend account data still resides in the US. »

**Il n'existe donc pas de résidence UE chez Resend.**

**DPF** : entrée « Resend » (PLUS FIVE FIVE) au statut **« Active - Re-certification under Review »** (EU-US et UK ; **pas de certification suisse**). Statut valide, mais recertification en cours d'instruction — les CCT du DPA couvrent le transfert de toute façon.

**Sous-traitants** : [liste](https://resend.com/legal/subprocessors) MàJ 15/07/2026 — **22 sous-traitants, tous « USA »** : AWS, Vercel, Supabase, PlanetScale, Snowflake, Tinybird, Datadog, Cloudflare, Svix, Inngest, Estuary, Elastic, Metabase, Retool, Liveblocks, Attio, Plain, Salesforce/Slack, Google, Stripe, **Anthropic (« Artificial Intelligence »)**, **RunPod (« Self hosted LLM's »)**. Préavis **14 jours**.

**Rétention** : suppression des données client **sous 90 jours** après résiliation du compte. Sauvegardes **30 jours**, « globally replicated ». Lien de partage public d'un email : **48 heures**.

**Le contenu HTML des emails est stocké et consultable par défaut** dans le tableau de bord (Preview, Plain Text, HTML, export CSV/JSON). Sa désactivation est un **service payant conditionné** : « Resend can **turn off message content storage** for teams with additional compliance requirements » sous 3 conditions (Pro/Scale depuis ≥ 1 mois, domaine actif, > 3 000 emails envoyés avec < 5 % de bounce) et « **requires a $50/mo add-on** ».

> **Conséquence** : prénoms, message, montant, email et téléphone de l'offrant restent lisibles en clair dans un tableau de bord hébergé aux États-Unis, **pour une durée non documentée publiquement**.

---

## 6. Formspree — le maillon le plus faible de la chaîne

- **DPA public : NON.** `/legal/dpa` et `/legal/data-processing-agreement` renvoient **404**. Les CGU ne mentionnent ni DPA, ni sous-traitants, ni CCT. La politique de confidentialité date du **24 avril 2022** et contient **zéro occurrence** de « Standard Contractual Clauses », « Privacy Shield » ou « Data Privacy Framework ».
- **DPF : NON — retrait confirmé.** Registre officiel, fiche **Formspree, Inc.** (San Antonio, TX) : EU-US et Swiss-US au statut **« Inactive - Withdrawal »**, fin d'usage autorisé le 22/04/2022, **période d'inactivité ouverte depuis le 26/04/2022, sans date de fin**. Aucune certification UK.
- **CCT** : seule affirmation trouvée, sur la page sécurité : « We rely on **Standard Contractual Clauses (SCCs)** as a data processor. » **Aucun document CCT publié, signable ou annexé.** Une affirmation marketing ne vaut pas clauses conclues : **le transfert vers Formspree n'a pas de base documentée au titre du chapitre V du RGPD.**
- **Localisation** : « Our services are hosted with **Amazon Web Services in the United States**. »
- **Rétention** : les soumissions **sont** stockées et exportables. **Aucune durée documentée** — seulement « for as long as your account is active » (texte de 2022).
- **Clause bloquante**, verbatim : « **You agree not to use the Formspree Service to collect sensitive personal data.** »

> **Recommandation directe** : Formspree en repli d'un flux contenant des données personnelles identifiantes est le point le plus fragile de la chaîne — **pas de DPA (art. 28 §3 non satisfait, manquement en soi)**, pas de DPF, pas de CCT produites, rétention indéfinie aux États-Unis. Un repli alternatif (écriture dans R2 UE, Cloudflare Queues, ou un second fournisseur email déjà sous contrat) supprimerait ce risque sans travail significatif.

---

## 7. GitHub

[DPA](https://github.com/customer-terms/github-data-protection-agreement) effectif octobre 2025, CCT 2021/914 Module Two ou Three, for compétent **Pays-Bas**. DPF **Active**. [Sous-traitants](https://github.com/subprocessors).

**Pertinence : nulle tant qu'aucune donnée personnelle n'atterrit dans le dépôt.** Le risque réel est opérationnel — fixtures de test contenant de vrais emails, dumps de logs, captures d'écran du tableau de bord Stripe ou Resend committées. À couvrir par un `.gitignore` strict et une revue avant commit, pas par du droit.

---

## 8. Non vérifié / limites

1. **Durée de conservation du contenu des emails chez Resend** — aucune durée publiée. Seules certitudes : 90 jours après résiliation, sauvegardes 30 jours, partage public 48 h. À demander par écrit à privacy@resend.com.
2. **Existence d'un DPA Formspree sur demande** — non trouvé publiquement, non demandé au support. Rien n'est auto-accepté aujourd'hui.
3. **Localisation exacte des métadonnées R2** (noms d'objets, tailles, logs d'accès) pour un compte sans Data Localization Suite — non précisé par la documentation. Seule voie documentée pour les garder en UE : le Customer Metadata Boundary, réservé Enterprise.
4. **Tarif de la Data Localization Suite** — « Enterprise-only paid add-on », aucun prix public.
5. **Résidence UE chez Stripe** — aucune option trouvée ; l'existence d'une offre Enterprise n'est pas exclue, non vérifiée.
6. **Statut DPF de Resend** — « Active - Re-certification under Review » au 20/08/2026, susceptible de bouger. À re-vérifier périodiquement.
7. **fal.ai** — traité dans le document sur les conditions des modèles.
