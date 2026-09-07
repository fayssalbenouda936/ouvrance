# Ce que Stripe émet, et jusqu'où il peut porter la facture d'ouvrance

**Recherche du ticket [#36](https://github.com/fayssalbenouda936/ouvrance/issues/36).** Pages consultées le **7 septembre 2026**. Extraits verbatim, chaque affirmation porte sa source.

> ⚠️ **Ce document n'est pas un avis juridique.** Il est écrit par un agent, pas par un juriste ni un expert-comptable. Trois registres sont distingués partout et il faut les lire comme tels :
> - **[DOC]** — ce que la documentation Stripe dit, verbatim, avec son lien.
> - **[TEXTE]** — ce que la loi française ou la doctrine administrative dit, verbatim, avec sa référence Légifrance ou BOFiP.
> - **[ZONE GRISE]** — ce qu'aucune source primaire consultée ne tranche. **À faire trancher avant mise en production.**
>
> **Ce document ne tranche aucune décision de conception.** Il nomme les options ; il n'en choisit aucune.

**Vocabulaire.** L'**Offrant** achète, paie et reçoit la pièce comptable. Une **Commande** existe dès le formulaire, avant tout **Paiement**. Une Commande porte une **Formule** (14,99 € ou 69,99 €), d'éventuels **Suppléments** (2 € ou 3 € l'unité) et des **Souvenirs**. Le **Cadeau** est livré quelques jours plus tard.

**Situation de départ.** ouvrance est une micro-entreprise française en **franchise en base de TVA** (art. 293 B du CGI), vend à des consommateurs français une prestation de services fournie par voie électronique, encaisse par **Stripe Checkout** avec webhook signé, et n'émet aujourd'hui **aucune pièce** : le seul document reçu par l'Offrant est le **reçu automatique Stripe**.

---

## 0. Le cadre français, en trois textes

Avant de regarder Stripe, il faut savoir à quoi on compare. Trois textes fixent la barre.

### 0.1 [TEXTE] La numérotation doit être unique, chronologique et continue

[BOFiP, BOI-TVA-DECLA-30-20-20-10 § 70](https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-10-20131018), verbatim :

> « la facture doit comporter **un numéro unique basé sur une séquence chronologique et continue** »

La doctrine admet des **séries distinctes** lorsque les conditions d'exercice de l'activité le justifient, mais chaque série doit être numérotée chronologiquement et sans interruption : **un trou dans une série est une rupture de continuité**. Le fondement réglementaire est le [7° de l'article 242 nonies A de l'annexe II au CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046086694/), qui exige « un numéro unique basé sur une séquence chronologique et continue ».

### 0.2 [TEXTE] La mention de la franchise en base, mot pour mot

[BOFiP, BOI-TVA-DECLA-30-20-20-10 § 450](https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-10-20131018) : les entreprises bénéficiant de la franchise en base doivent porter la mention

> « **TVA non applicable, art. 293 B du CGI** »

Le BOFiP ajoute une conséquence qui compte pour ouvrance : faire figurer de la TVA sur une facture alors qu'on relève de la franchise rend redevable de cette taxe **du seul fait de sa facturation**, sans ouvrir de droit à déduction au client. Autrement dit : **une pièce qui affiche une ligne « TVA 0,00 € » ou « Tax » n'est pas neutre**, elle est un risque.

Les seuils de la franchise, à [l'article 293 B du CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045035275) : pour les prestations de services, **37 500 €** de chiffre d'affaires l'année civile précédente et **41 250 €** l'année en cours.

> **[ZONE GRISE] — la renumérotation du CGI.** La recherche Légifrance signale une [ordonnance n° 2025-1247 du 17 décembre 2025](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162567/) qui abroge des dispositions de la section « Franchise en base » **à compter du 1er septembre 2026**, dans le cadre de la recodification. Le libellé exact de la mention à porter à partir de cette date (« art. 293 B du CGI » ou une nouvelle référence) **n'a pas pu être vérifié verbatim** dans la version en vigueur au 7 septembre 2026. **À vérifier avant d'imprimer la mention en dur.**

### 0.3 [TEXTE] Dix ans de conservation

[Article L123-22 du Code de commerce](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006219327), verbatim :

> « Les documents comptables et les pièces justificatives sont **conservés pendant dix ans**. »

C'est la contrainte qui commande la section 6.

---

## 1. Reçu ≠ facture

### 1.1 [DOC] Ce qu'est le reçu automatique Stripe

[Stripe — Reçus et factures payées](https://docs.stripe.com/receipts), verbatim :

> « Stripe crée des reçus **pour tous les paiements et remboursements réussis**, y compris les paiements de factures et les paiements récurrents dans le cadre d'un abonnement. Les clients peuvent consulter leurs reçus en ligne via un navigateur web, et éventuellement les télécharger sous forme de PDF. »

L'envoi automatique est un **réglage du Dashboard**, pas un défaut : « Dans le Dashboard, accédez à **Paramètres** > **Entreprise** > E-mails aux clients. Sous Paiements, activez **Paiements réussis** ou **Remboursements**. »

Le lien vient du champ `receipt_url` du Charge. [The Charge object](https://docs.stripe.com/api/charges/object), verbatim :

> `receipt_url` (string, nullable) — « This is the URL to view the receipt for this charge. The receipt is **kept up-to-date to the latest state of the charge, including any refunds**. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt. »

**Le reçu est vivant.** Il se met à jour tout seul après un remboursement. Une facture, elle, est figée à l'émission et se corrige par un avoir. C'est la première différence de nature, et elle est structurelle.

### 1.2 [DOC] Les liens expirent au bout de 30 jours

[Stripe — Reçus](https://docs.stripe.com/receipts), verbatim :

> « Les reçus n'expirent pas, mais pour des raisons de sécurité, **les liens vers les reçus expirent au bout de 30 jours**. Si un lien vers un reçu a expiré, Stripe demande au client de fournir l'adresse e-mail associée à la transaction d'origine. Stripe crée un nouveau lien et l'envoie à cette adresse e-mail. »

Conséquence directe : un `receipt_url` stocké en D1 est **mort au bout de 30 jours** pour l'Offrant qui reviendrait le chercher.

### 1.3 [DOC] Ce qui est paramétrable, et ce qui ne l'est pas

| Élément | Paramétrable sur un reçu ? | Source |
| --- | --- | --- |
| Logo, icône, couleur de marque, couleur d'accentuation | **Oui** — Paramètres > Entreprise > Image de marque, onglet « Reçus par e-mail » | [receipts](https://docs.stripe.com/receipts) |
| Dénomination sociale, adresse et e-mail du support, URL de politique de confidentialité | **Oui, et obligatoires** — « Pour des raisons de conformité, certaines coordonnées sont **toujours obligatoires** sur les reçus » | [receipts](https://docs.stripe.com/receipts) |
| Langue | **Oui** — via `preferred_locales` du Customer ou la langue par défaut du compte | [receipts](https://docs.stripe.com/receipts) |
| **Un pied de page libre / une mention légale libre** | **Non documenté.** La section « Personnaliser les reçus » ne comporte que « Image de marque », « Informations de l'entreprise » et « Localisation ». Le champ `footer` **n'existe que sur la facture**, pas sur le reçu | [receipts](https://docs.stripe.com/receipts) vs [invoicing/customize](https://docs.stripe.com/invoicing/customize) |
| **Un numéro de SIREN** | **Non documenté** comme champ. Les numéros fiscaux (`account_tax_ids`) s'affichent « sur les factures au format PDF **et les reçus par e-mail** » — mais ce sont des *tax IDs*, typés par pays, pas un SIREN | [invoicing/customize](https://docs.stripe.com/invoicing/customize) |
| Une numérotation propre à ouvrance | **Non.** Aucun champ, aucun réglage | — |

Le seul texte libre approchant est indirect : la description du paiement. Sur ce point, [Stripe — Personnaliser les factures](https://docs.stripe.com/invoicing/customize) est explicite sur le partage des responsabilités :

> « **Parce que vous en savez plus sur vos clients et votre entreprise que Stripe, assurez-vous que vos factures contiennent toutes les informations requises.** Vos factures doivent être exactes, facturer les taxes appropriées et respecter toutes les lois et réglementations en vigueur dans votre région. »

### 1.4 [DOC] La numérotation des reçus : `receipt_number`

[The Charge object](https://docs.stripe.com/api/charges/object), verbatim :

> `receipt_number` (string, nullable) — « This is the **transaction number** that appears on email receipts sent for this charge. This attribute will be `null` **until a receipt has been sent**. »

Trois choses s'en déduisent, et une seule est une réponse :

1. Stripe l'appelle un **numéro de transaction**, pas un numéro de facture.
2. Il est `null` tant qu'aucun reçu n'a été **envoyé**. Donc si l'envoi automatique des reçus est désactivé, ou si le paiement n'a jamais donné lieu à un e-mail, **il n'y a pas de numéro du tout**. Une séquence qui ne se remplit que sur envoi d'e-mail ne peut pas être une séquence chronologique continue au sens du § 0.1.
3. **[ZONE GRISE]** — la **règle** de formation de ce numéro (est-il séquentiel par compte ? par charge ? incrémental ? aléatoire ?) **n'est documentée nulle part** dans la référence API ni dans la page Reçus. Aucune source primaire ne l'énonce.

> **Conclusion de la section 1.** Le reçu Stripe est une **preuve de transaction émise par Stripe**, mise à jour en continu, dont le lien meurt en 30 jours, sans pied de page libre, sans SIREN, sans mention 293 B, et dont la numérotation n'obéit à aucune règle publiée. **Il ne peut pas tenir lieu de facture d'ouvrance**, sur au moins quatre points opposables : numérotation continue (§ 0.1), mention 293 B (§ 0.2), identification de l'émetteur, et immuabilité de la pièce.

---

## 2. Stripe Invoicing

### 2.1 [DOC] Deux systèmes de numérotation, et l'UE impose le bon

[Stripe — Personnaliser les factures](https://docs.stripe.com/invoicing/customize), verbatim :

> « Stripe génère automatiquement des numéros de facture pour le suivi et le rapprochement des factures. Les numéros de facture ont un préfixe et un suffixe, comme `586A2E-0139` ou `MYSHOP-1203`. (Le numéro de facture complet est toujours unique dans votre compte pour les deux systèmes.) Stripe prend en charge deux systèmes de numérotation de factures :
> - **Séquentiellement pour chaque client (au niveau du client)** : utilise un préfixe unique pour chaque client et numérote les factures séquentiellement à l'échelle du client.
> - **Séquentiellement à l'échelle de votre compte (au niveau du compte)** : utilise le même préfixe pour chaque client et numérote les factures séquentiellement à l'échelle de votre compte. »

Et, verbatim :

> « Stripe choisit un comportement par défaut en fonction du pays où votre compte Stripe est basé. **Les pays membres de l'Union européenne et le Royaume-Uni nécessitent en général un séquençage au niveau du compte.** Tous les autres pays ont par défaut un séquençage au niveau du client car cela n'indique pas le nombre total de factures. Lorsque vous basculez entre les systèmes ou que vous mettez à jour les préfixes, **seules les futures factures utilisent les nouveaux paramètres**. Cela n'affecte pas les factures existantes. »

Suit un avertissement explicite, verbatim :

> « Les exigences en matière de facture varient selon la juridiction. Consultez un professionnel pour obtenir des informations sur votre cas d'usage spécifique. **Il est de votre responsabilité de vérifier que les factures que vous émettez répondent aux exigences fiscales locales.** »

| Réglage | Valeur | Source |
| --- | --- | --- |
| Préfixe de compte | 1 à 12 lettres majuscules ou chiffres, modifiable dans Paramètres > Factures (API par défaut ≥ `2020-03-02`) | [invoicing/customize](https://docs.stripe.com/invoicing/customize) |
| Numéro initial | « Par défaut, les numéros de facture commencent à `0001` » ; champ **Séquence de la prochaine facture** | idem |
| Contrainte de reprise | « Vous pouvez uniquement définir le prochain numéro de facture sur un **numéro plus grand** que tout numéro utilisé sur une facture » | idem |
| Plafond | « Le numéro de facture autorisé maximum est **1 000 000 000** » | idem |
| Préfixe par client | `invoice_prefix` sur le Customer ; départ via `next_invoice_sequence` | idem |

**Point important pour une reprise de séquence** : on ne peut faire **qu'avancer** le compteur, jamais le reculer. Une erreur de réglage est définitive.

### 2.2 [DOC] Le numéro est attribué à la **finalisation**, pas à la création

C'est la réponse à la question des brouillons supprimés, et elle est adossée à deux faits documentés.

**Fait 1** — [The Invoice object](https://docs.stripe.com/api/invoices/object) : dans l'exemple canonique d'une facture `"status": "draft"`, le champ est `"number": null`. La description du champ, verbatim :

> `number` (string, nullable) — « A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer's unique invoice_prefix if it is specified. »

**Fait 2** — [Stripe — Changements et finalisation des états](https://docs.stripe.com/invoicing/integration/workflow-transitions), verbatim, sur ce que fait la finalisation :

> « La finalisation d'une facture :
> - Permet le paiement de la facture.
> - **Garantit la présence d'un numéro de facture.**
> - Cela rend certaines propriétés immuables sur la facture.
> - Crée un Payment Intent incomplet pour la facture.
> - Génère une URL unique permettant au client de payer la facture et un lien pour télécharger la facture au format PDF. »

Le cycle de vie, [Stripe — Fonctionnement de la facturation](https://docs.stripe.com/invoicing/overview), verbatim :

> « Vous pouvez supprimer une facture `draft`. **Vous ne pouvez pas récupérer une facture supprimée.** »

Et la transition documentée est `draft` → `DELETE /v1/invoices/:id` → webhook `invoice.deleted` → « (Supprimé) ».

> **Réponse : un brouillon supprimé ne consomme pas de numéro**, parce qu'un brouillon **n'a pas** de numéro — il est `null` jusqu'à la finalisation, et une facture supprimée n'est jamais finalisée. La séquence ne saute donc pas.
>
> **[ZONE GRISE]** — aucune page Stripe ne l'écrit *en toutes lettres* sous la forme « supprimer un brouillon ne consomme pas de numéro ». C'est une déduction de deux faits documentés (`number: null` sur un `draft` + « la finalisation garantit la présence d'un numéro »), pas une citation. À confirmer empiriquement en mode test avant de s'y fier.

**Le corollaire compte autant** : une facture **finalisée** ne se supprime pas, elle s'annule. Verbatim, [invoicing/overview](https://docs.stripe.com/invoicing/overview) :

> « En théorie, l'annulation d'une facture équivaut à sa suppression. Cependant, lorsque vous annulez une facture, **une trace en est conservée, ce qui vous permet de la rechercher ensuite grâce à son numéro**. Les factures annulées sont considérées comme nulles à des fins de reporting et ne peuvent donc pas être réglées. »

Une facture `void` **garde son numéro**. La séquence reste continue. C'est exactement le comportement qu'exige le § 0.1.

Stripe renvoie d'ailleurs explicitement au droit local, verbatim :

> « Consultez les réglementations locales pour déterminer si et comment une facture peut être modifiée, annulée ou invalidée dans la juridiction où vous exercez votre activité. Vous pouvez être amené à émettre une autre facture ou un avoir à la place. **Stripe vous recommande de consulter votre conseiller juridique pour obtenir des conseils spécifiques à votre entreprise.** »

### 2.3 [DOC] Les champs qui peuvent porter la mention 293 B

| Champ | Ce que la doc en dit, verbatim | Où il s'affiche | Modifiable après finalisation ? |
| --- | --- | --- | --- |
| `footer` | « Les factures PDF peuvent inclure un bloc de texte de bas de page facultatif. **Le champ Bas de page est souvent utilisé pour le texte obligatoire contractuel ou juridique.** Un cas d'usage fréquent consiste à afficher les informations d'enregistrement de l'entreprise, comme le numéro d'enregistrement d'entreprise britannique (CRN). » | PDF de la facture | **Non** — « Une fois que la facture est finalisée, vous ne pouvez plus mettre à jour le champ de pied de page » |
| `custom_fields` | « Les champs personnalisés vous permettent de fournir **jusqu'à quatre paires clé-valeur** qui s'affichent dans **l'en-tête** de la facture. » Exemples cités : « Numéros de bon de commande / Numéros de sous-traitant / **Conformité fiscale** » | En-tête du PDF | **Non** — « Une fois la facture finalisée, vous ne pouvez plus mettre à jour les champs personnalisés » |
| `description` (mémo) | « Les mémos sont inclus dans les factures au format PDF, les e-mails de facture et la page de facture hébergée. » Réglable par défaut au niveau du compte | PDF, e-mail, page hébergée | Généralement non — « Pour la plupart des factures, cela inclut également le champ `description` » |
| `account_tax_ids` | « Ajoutez des numéros d'identification fiscale (tax IDs) pour les afficher sur les **factures au format PDF et les reçus par e-mail**. » Attention : « Une fois que vous avez ajouté un numéro fiscal, **vous ne pouvez plus modifier le numéro ou le type**. » | PDF + reçus | Non |
| Informations publiques | « Les factures comprennent **toutes les informations publiques** enregistrées dans les informations publiques sur l'entreprise, notamment votre adresse e-mail et l'adresse de votre site Web. Par défaut, nous indiquons l'adresse de votre entreprise » | PDF, e-mails | Réglage de compte |

Source unique de ce tableau : [Stripe — Personnaliser les factures](https://docs.stripe.com/invoicing/customize).

> **Le `footer` est le porteur naturel de « TVA non applicable, art. 293 B du CGI ».** C'est le champ que Stripe désigne lui-même comme celui du « texte obligatoire contractuel ou juridique », avec l'exemple d'un numéro d'enregistrement d'entreprise. Un `custom_field` intitulé « Conformité fiscale » ou « SIREN » est l'autre option nommée. **On ne choisit ni l'un ni l'autre ici.**
>
> **[ZONE GRISE]** — aucune source Stripe ne dit qu'un `footer` ou un `custom_field` **satisfait** une obligation de mention légale française. Stripe fournit un emplacement ; il ne se prononce pas sur la validité de ce qu'on y met, et le renvoi de responsabilité du § 2.1 est explicite.

### 2.4 [DOC] Émettre une facture après un Checkout déjà encaissé

C'est le cas d'ouvrance : le Paiement est encaissé par Checkout, et la pièce doit suivre.

**Voie 1 — `invoice_creation` sur la Checkout Session.** [Stripe — Reçus et factures payées](https://docs.stripe.com/receipts), verbatim :

> « Vous pouvez générer des reçus pour les factures payées, qui contiennent **plus de détails que les reçus standards**. Pour les abonnements, Stripe génère les factures automatiquement, mais **vous devez les activer pour les paiements ponctuels**. »

Le paramètre, [Create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create) : `invoice_creation` (object, optional) — « **Generate a post-purchase Invoice for one-time payments.** » Le sous-objet `invoice_data` porte, dans l'exemple de réponse de l'API : `account_tax_ids`, `custom_fields`, `description`, `footer`, `issuer`, `metadata`, `rendering_options`. L'exemple documenté sur la page Reçus le montre en clair :

```
-d "invoice_creation[enabled]=true"
-d "invoice_creation[invoice_data][description]=Invoice for Product X"
-d "invoice_creation[invoice_data][account_tax_ids][0]=DE123456789"
-d "invoice_creation[invoice_data][custom_fields][0][name]=Purchase Order"
-d "invoice_creation[invoice_data][footer]=B2B Inc."
```

Ce qui suit le paiement, verbatim :

> « Une fois le paiement effectué, Stripe envoie un récapitulatif de la facture à l'adresse e-mail indiquée par le client. Ce récapitulatif comprend des liens pour télécharger **la facture et le reçu du paiement** au format PDF. »

Avec une réserve d'exploitation, verbatim :

> « Les reçus de facture ne sont envoyés **qu'une fois le paiement effectué**, et non à la fin de la session de paiement. Les moyens de paiement différés ou asynchrones peuvent donc prendre plus de temps à déclencher les reçus. »

L'événement à écouter est `invoice.paid` — « Vous pouvez écouter l'événement `invoice.paid` si vous avez besoin d'accéder aux reçus de facture par voie programmatique. »

**Voie 2 — une facture indépendante marquée payée hors Stripe.** [Stripe — Fonctionnement de la facturation](https://docs.stripe.com/invoicing/overview), verbatim :

> « **Factures externes à Stripe.** Si un client paie une facture en dehors de Stripe, vous pouvez définir manuellement son état sur `paid` via le Dashboard ou l'API. […] Pour marquer manuellement une facture en cours comme payée dans l'API, utilisez le paramètre `paid_out_of_band` lorsque vous soumettez une requête au endpoint Pay. »

Avec cette conséquence sur les webhooks, verbatim : une facture peut basculer sur `paid` sans PaymentIntent associé lorsqu'« elle est marquée comme `paid_out_of_band` » — « Dans un tel cas, vous recevez l'événement `invoice.paid`, mais **pas** l'événement `invoice.payment_succeeded`. »

Le champ correspondant sur l'objet, [The Invoice object](https://docs.stripe.com/api/invoices/object) : `amount_paid_off_stripe` — « Amount, in the smallest currency unit, that was paid on the invoice **outside of Stripe**. »

> **Deux options existent, nommées, documentées, et elles ne sont pas équivalentes** : `invoice_creation` lie la facture au Paiement Stripe et fait envoyer le PDF par Stripe ; `paid_out_of_band` crée une facture qu'ouvrance contrôle de bout en bout mais qui présente le Paiement comme extérieur à Stripe, ce qui est **factuellement faux** ici puisque Stripe a bien encaissé. **Le choix n'est pas tranché dans ce document.**

### 2.5 [DOC] Le PDF et sa durée de vie

[The Invoice object](https://docs.stripe.com/api/invoices/object), verbatim :

> `invoice_pdf` (string, nullable) — « The link to download the PDF for the invoice. **If the invoice has not been finalized yet, this will be null.** »
>
> `hosted_invoice_url` (string, nullable) — « The URL for the hosted invoice page, which allows customers to view and pay an invoice. **If the invoice has not been finalized yet, this will be null.** »

Sur la persistance de la page hébergée après annulation, [invoicing/overview](https://docs.stripe.com/invoicing/overview) :

> « Après l'annulation d'une facture, **la page de facture hébergée reste accessible** et affiche un message indiquant que la facture a été annulée. »

> **[ZONE GRISE] — la durée de vie du PDF.** Aucune page consultée n'énonce de durée d'expiration pour `invoice_pdf` ou `hosted_invoice_url`. La seule expiration documentée dans tout le corpus est celle des **liens de reçus, à 30 jours** ([receipts](https://docs.stripe.com/receipts)) — elle est écrite pour les reçus, pas pour les factures, et on ne peut ni l'étendre ni conclure à une absence d'expiration. **Aucune source primaire ne garantit qu'un `invoice_pdf` sera encore téléchargeable dans dix ans.** Voir section 6.

### 2.6 [DOC] Le prix

Invoicing est un produit facturé **en plus** des frais de paiement.

[Stripe — Tarifs Invoicing](https://stripe.com/invoicing/pricing), verbatim :

| Offre | Tarif |
| --- | --- |
| Invoicing **Starter** | « **0,4 % par facture payée** » |
| Invoicing **Plus** | « **0,5 % par facture payée** » |

Sans frais fixes ni frais d'installation, les frais Stripe Payments s'appliquant séparément.

**Mais le cas d'ouvrance relève d'un barème distinct.** [Stripe — Reçus](https://docs.stripe.com/receipts) prévient, verbatim :

> « La création de factures pour les paiements ponctuels via l'API Checkout Sessions **n'est pas une fonctionnalité d'Invoicing et est facturée séparément.** »

Et l'article de support qu'elle vise, [Pricing for post-payment invoices for one time purchases via Checkout and Payment Links](https://support.stripe.com/questions/pricing-for-post-payment-invoices-for-one-time-purchases-via-checkout-and-payment-links), verbatim :

> « **0.4% of the transaction total, up to a maximum of $2 USD (or local currency equivalent) per invoice.** »

Appliqué aux prix d'ouvrance — simple arithmétique sur le taux cité, pas une citation :

| Commande | 0,4 % | Plafond atteint ? |
| --- | --- | --- |
| Formule 14,99 € | ≈ 0,06 € | non |
| Formule 69,99 € | ≈ 0,28 € | non |
| Formule 69,99 € + 5 Suppléments à 3 € | ≈ 0,34 € | non |

> **Le coût marginal d'une facture Stripe sur ce catalogue est de l'ordre de 6 à 35 centimes**, très loin du plafond de 2 $. Le prix n'est pas l'argument décisif ; l'émetteur (section 4) l'est.

---

## 3. Avoirs et remboursements

### 3.1 [DOC] Le `Refund` ne produit aucune pièce comptable

[Stripe — Rembourser et annuler des paiements](https://docs.stripe.com/refunds), verbatim :

> « Vous pouvez émettre plusieurs remboursements pour un paiement, mais **le montant total du remboursement ne peut être supérieur au montant du paiement initial**. »

Sur ce que le client reçoit, verbatim :

> « Si toutes les conditions suivantes sont réunies, nous envoyons un e-mail à votre client pour l'informer du remboursement :
> - Le paiement d'origine a été créé sur un objet Customer dans votre compte Stripe.
> - Le client dispose d'une adresse e-mail enregistrée.
> - Vous avez activé l'option **Envoyer un e-mail aux clients en cas d'émission d'un remboursement**. »

C'est un **e-mail de notification**, plus la mise à jour du reçu (§ 1.1 : « The receipt is kept up-to-date to the latest state of the charge, **including any refunds** »). Il n'y a **ni numéro d'avoir, ni PDF d'avoir, ni pièce datée et figée**.

Deux pièges d'exploitation documentés, verbatim :

> « Les remboursements émis **peu après** le paiement d'origine se présentent sous la forme d'une **annulation** et non d'un remboursement. Dans ce cas, le paiement d'origine **disparaît tout simplement du relevé du client**, et aucun crédit n'est émis. »

> « Les frais de traitement Stripe liés à la transaction initiale **ne sont pas remboursés**. »

Le premier compte pour ouvrance : un remboursement de Supplément décidé le jour même ne laissera **aucune trace visible** côté client.

### 3.2 [DOC] Le `CreditNote`, lui, est une vraie pièce — mais adossée à une facture

[The Credit Note object](https://docs.stripe.com/api/credit_notes/object), verbatim :

> `number` (string) — « A unique number that identifies this particular credit note and **appears on the PDF of the credit note and its associated invoice**. »
>
> `pdf` (string) — « The link to download the PDF of the credit note. »
>
> `invoice` (string, expandable) — « ID of the invoice. »
>
> `memo` (string, nullable) — « **Customer-facing text that appears on the credit note PDF.** »
>
> `out_of_band_amount` (integer, nullable) — « Amount that was credited **outside of Stripe**. »
>
> `effective_at` (timestamp, nullable) — « The date when this credit note is in effect. […] When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF. »
>
> `status` (enum) — « one of `issued` or `void` »
>
> `type` (enum) — « one of `pre_payment` or `post_payment`. A `pre_payment` credit note means it was issued when the invoice was open. A `post_payment` credit note means it was issued when the invoice was paid. »

Le numéro d'exemple donné par Stripe est `"C9E0C52C-0036-CN-01"` — **il dérive du numéro de la facture d'origine**, suffixé `-CN-01`. L'avoir n'a donc pas une séquence indépendante : il hérite de celle de la facture.

Un avoir **exige** une facture. [Create a credit note](https://docs.stripe.com/api/credit_notes/create), verbatim :

> `invoice` (string, **required**) — « ID of the invoice. »

> **Réponse directe : non, un `CreditNote` ne peut pas exister sans facture d'origine.** Le paramètre est requis. Sans Stripe Invoicing, il n'y a **aucun objet avoir** dans le compte Stripe d'ouvrance — seulement des `Refund`, qui ne sont pas des pièces comptables (§ 3.1).

### 3.3 [DOC] Le remboursement partiel : ce que l'avoir sait faire

[Create a credit note](https://docs.stripe.com/api/credit_notes/create), verbatim :

> « A credit note will first reduce the invoice's `amount_remaining` (and `amount_due`), but not below zero. This amount is indicated by the credit note's `pre_payment_amount`. The excess amount is indicated by `post_payment_amount`, and it can result in any combination of the following:
> - **Refunds**: create a new refund (using `refund_amount`) or link existing refunds (using `refunds`).
> - **Customer balance credit**: credit the customer's balance (using `credit_amount`) which will be automatically applied to their next invoice when it's finalized.
> - **Outside of Stripe credit**: record the amount that is or will be credited outside of Stripe (using `out_of_band_amount`).
>
> The sum of refunds, customer balance credits, and outside of Stripe credits must equal the `post_payment_amount`. »

Et, verbatim :

> « **You may issue multiple credit notes for an invoice.** »

Trois façons d'imputer le crédit, [Stripe — Émettre des avoirs](https://docs.stripe.com/invoicing/dashboard/credit-notes), verbatim :

> « - Réduction d'un montant fixe sur un poste de facture.
> - Réduction sur une quantité d'un poste de facture. […]
> - Appliquez une réduction au montant total de la facture en ajoutant **un poste de réduction personnalisé** avec une description, une quantité et un prix unitaire. »

Avec une recommandation forte, verbatim :

> « Nous vous recommandons dans la mesure du possible d'appliquer des réductions **aux postes de facture**, car chaque avoir est associé à un poste de facture. L'ajout d'un poste de réduction personnalisé peut **compliquer le reporting et le suivi**, car l'avoir n'est pas associé à un poste de facture réel. »

Appliqué aux deux cas d'usage d'ouvrance :

| Cas d'usage | Ce que Stripe permet | Réserve documentée |
| --- | --- | --- |
| **Supplément refusé, remboursé à l'unité** | Avoir sur le **poste** correspondant, par montant ou par quantité — le cas le plus propre, tel que Stripe le recommande | Chaque Supplément doit exister comme **poste distinct** de la facture. Une facture à une seule ligne « Commande » obligerait au « poste de réduction personnalisé » que Stripe déconseille |
| **Remboursement au prorata sur un dénominateur de deux ans** | Montant arbitraire via `amount` + `lines`, ou poste personnalisé | Contrainte de mélange : « si vous effectuez une remise sur la quantité d'un poste, un avoir à venir ne [peut] effectuer une remise sur ce poste que **par quantité, et non par montant** » — le premier avoir contraint la forme des suivants |

Contrainte de plafond, [Stripe — Émettre des avoirs](https://docs.stripe.com/invoicing/dashboard/credit-notes), verbatim :

> « La somme de tous les avoirs émis pour une facture **ne peut pas dépasser le montant total de la facture**. Pour une facture à l'état `paid`, la somme des montants du remboursement, du crédit et des paiements en dehors de Stripe doit être **égale au total de l'avoir**. »

Et l'articulation avec les remboursements faits *hors* du flux avoir, [Create a credit note](https://docs.stripe.com/api/credit_notes/create), verbatim :

> « For invoices that also have refunds created through the Refund API, the credit note API **subtracts those refund amounts from the maximum creditable amount**. […] If you use both, ensure the combined total does not exceed the invoice's paid amount. »

Enfin, l'annulation d'un avoir est très restreinte, verbatim :

> « Vous pouvez annuler un avoir **uniquement s'il figure sur une facture en cours**. »

Un avoir sur une facture `paid` — le cas d'ouvrance, toujours — est donc **définitif**.

> **Conclusion de la section 3.** Sans Invoicing, un remboursement ouvrance produit un e-mail et un reçu réécrit : **aucune pièce**. Avec Invoicing, un remboursement partiel produit un `CreditNote` **numéroté, daté, avec PDF et mémo**, y compris au prorata — à la condition que la facture d'origine existe et, pour le cas des Suppléments, que ses postes soient assez fins.

---

## 4. Qui est l'émetteur, juridiquement

C'est la question qui commande toutes les autres.

### 4.1 [DOC] Ce que Stripe dit de son propre rôle

Le champ le plus parlant est sur l'objet lui-même. [The Invoice object](https://docs.stripe.com/api/invoices/object), verbatim :

> `issuer` (object) — « **The connected account that issues the invoice.** The invoice is presented with the branding and support information of the specified account. »

Et sa valeur par défaut, dans l'exemple canonique de Stripe : `"issuer": { "type": "self" }`. `self`, c'est **le compte marchand** — ouvrance. Stripe se modélise lui-même comme **l'outil**, pas comme l'émetteur.

Le renvoi de responsabilité est ensuite répété à trois endroits différents de la documentation :

[Stripe — Personnaliser les factures](https://docs.stripe.com/invoicing/customize) :

> « Parce que vous en savez plus sur vos clients et votre entreprise que Stripe, assurez-vous que vos factures contiennent toutes les informations requises. **Vos factures doivent être exactes, facturer les taxes appropriées et respecter toutes les lois et réglementations en vigueur dans votre région.** »

> « Les exigences en matière de facture varient selon la juridiction. Consultez un professionnel pour obtenir des informations sur votre cas d'usage spécifique. **Il est de votre responsabilité de vérifier que les factures que vous émettez répondent aux exigences fiscales locales.** »

[Stripe — Changements et finalisation des états](https://docs.stripe.com/invoicing/integration/workflow-transitions) :

> « **Il vous incombe de vous assurer que les factures que vous créez sont conformes à toutes les réglementations en vigueur.** »

[Stripe Services Agreement](https://stripe.com/legal/ssa), § 7.3(b), verbatim :

> « User has sole responsibility and liability for: (i) determining which, if any, Taxes or fees apply to the sale of its products and services… (ii) **assessing, collecting, reporting, and remitting Taxes for its business to the appropriate tax and revenue authorities.** »

> **[ZONE GRISE] — le SSA ne contient pas la clause qu'on cherchait.** La lecture du [Stripe Services Agreement](https://stripe.com/legal/ssa) n'a **pas** fait apparaître de clause disant expressément « Stripe n'est pas l'émetteur de la facture du marchand », ni de clause « merchant of record » / « seller of record ». Ce qu'on y trouve est le renvoi fiscal du § 7.3(b) et la clause de conservation du § 4.4 (voir section 6). **L'absence d'une clause n'est pas une preuve** : elle peut tenir à la version consultée ou à la profondeur de lecture. Ce qui est établi, c'est le faisceau : `issuer: self`, plus trois renvois de responsabilité dans la doc produit.

### 4.2 [TEXTE] Ce que le droit français appelle cette situation : le mandat de facturation

[Article 289 du CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413), I-2 : les factures peuvent être

> « **matériellement émises par le client ou par un tiers lorsque l'assujetti leur donne mandat à cet effet** »

et chaque facture est alors « établie au nom et pour le compte de l'assujetti ».

La doctrine est plus précise que le texte. [BOFiP, BOI-TVA-DECLA-30-20-10-30](https://bofip.impots.gouv.fr/bofip/13244-PGP.html/identifiant%3DBOI-TVA-DECLA-30-20-10-30-20220629), verbatim :

| Point | Verbatim BOFiP | § |
| --- | --- | --- |
| Qui donne mandat | « **Le fournisseur du bien ou service doit donner mandat au tiers ou client concerné** » | § 90 |
| Un écrit est-il exigé ? | « **La conclusion d'un mandat de facturation n'est soumise à aucun formalisme en particulier** » — mandat écrit **ou tacite**, mais les parties doivent pouvoir en démontrer l'existence sur demande de l'administration ; l'écrit est recommandé pour la sécurité juridique | § 120 |
| Exception | Pour un mandataire **hors UE**, « le mandat ainsi conclu **doit impérativement prendre la forme d'un contrat écrit** » | § 260 |
| Acceptation | « **Toute facture émise au nom et pour le compte du fournisseur doit faire l'objet d'une acceptation par ce dernier** » | § 150 |
| Responsabilité | Le mandant « **conserve l'entière responsabilité de ses obligations en matière de facturation et de ses conséquences au regard de la TVA** » | § 170 |
| Trésor | Le mandant reste tenu « de verser au Trésor la taxe mentionnée sur les factures établies en son nom » | § 230 |

> **[ZONE GRISE] — Stripe Payments Europe est-il « hors UE » ?** Le § 260 impose un **contrat écrit** lorsque le mandataire est établi hors de l'Union. L'entité contractante d'ouvrance chez Stripe (Stripe Payments Europe Ltd., Irlande, ou une autre) **n'a pas été vérifiée dans cette recherche**, et le mandat n'est de toute façon pas au dossier. **À faire trancher.**

### 4.3 La conclusion, encadrée

> **Une facture produite par Stripe Invoicing est une facture d'ouvrance, matériellement établie par un outil.** Stripe se désigne lui-même comme l'outil (`issuer: self`) et renvoie trois fois la responsabilité au marchand. Le droit français connaît parfaitement cette configuration : c'est l'article 289, I-2 du CGI et la sous-traitance de facturation.
>
> **Stripe Invoicing peut donc tenir lieu de facture d'ouvrance**, sous réserve des conditions que la doctrine pose :
> 1. **Le mandat doit exister et être démontrable** (BOFiP § 120), **écrit** si le mandataire est hors UE (§ 260) — point non vérifié, voir § 4.2.
> 2. **ouvrance reste seule responsable** de la conformité de chaque facture (BOFiP § 170) — ce que Stripe écrit d'ailleurs dans ses propres termes.
> 3. **La pièce doit porter tout ce que le droit français exige** : numérotation continue (§ 0.1), mention 293 B (§ 0.2), identification du vendeur. Stripe fournit les emplacements (`footer`, `custom_fields`, informations publiques) ; **il ne remplit pas ces emplacements à la place d'ouvrance et ne garantit pas leur suffisance**.
> 4. **La conservation dix ans reste due par ouvrance** (§ 0.3, et section 6).
>
> **[ZONE GRISE]** — aucune source primaire consultée ne dit qu'un compte Stripe Invoicing configuré correctement **est** conforme au droit français de la facturation. Stripe dit exactement l'inverse : « il est de votre responsabilité de vérifier ». **Le point 1 et le point 3 sont à faire valider par un expert-comptable avant émission de la première pièce.**

---

## 5. Stripe Tax et la franchise en base

### 5.1 [DOC] Ce que Stripe Tax fait quand il n'y a pas d'immatriculation

[Stripe — Montants de taxe nuls et autoliquidation](https://docs.stripe.com/tax/zero-tax), verbatim :

> « **Non immatriculé** — `not_collecting` — Pour collecter une taxe dans une juridiction, **vous devez au préalable vous immatriculer à cette fin**. Vous pouvez préciser où vous êtes immatriculés pour cela à la page Paramètres fiscaux. »

Et, verbatim :

> « Si vous ne souhaitez pas collecter de taxe sur un produit donné, indiquez à Stripe Tax de le traiter comme non taxable en lui attribuant **le code fiscal Non taxable (`txcd_00000000`)**. »

Avec un avertissement de lecture, verbatim :

> « `not_collecting` **est ambigu** : cela signifie soit l'absence d'immatriculation active dans la juridiction du client, **soit** un code de taxe de produit non taxable (`txcd_00000000`) sur le produit. »

Il n'existe donc **pas** de réglage nommé « franchise en base » ni « exempt / not registered » côté vendeur : il y a **l'absence d'immatriculation** (état par défaut) et **un code produit non taxable**. Le statut `exempt` documenté (`Customer.tax_exempt = exempt`) porte sur **le client**, pas sur le vendeur — « Certains clients sont exonérés du paiement de la taxe indirecte dans certaines juridictions ».

Rappel du § 0.2 : afficher une ligne de taxe à 0 sur une facture en franchise n'est pas anodin en droit français.

> **Conclusion.** Pour une micro-entreprise en franchise en base qui vend à des consommateurs français, **Stripe Tax n'apporte rien à l'émission de la facture** : il n'y a aucune taxe à calculer, aucune immatriculation à déclarer, et le résultat par défaut (`not_collecting`, montant nul) est déjà celui d'un compte où Tax n'est pas activé. La seule fonction potentiellement utile est le **suivi des seuils** — [Stripe Tax](https://docs.stripe.com/tax) : « Suit vos ventes par rapport aux seuils d'enregistrement fiscal locaux et vous envoie des alertes lorsque vous risquez d'avoir des obligations fiscales » — mais les seuils qu'il surveille sont ceux de l'immatriculation TVA par juridiction, **pas** les 37 500 / 41 250 € de l'article 293 B. **[ZONE GRISE]** : aucune source consultée ne dit que Stripe Tax surveille le seuil français de franchise en base.

### 5.2 Le guichet OSS : hors sujet ici, en deux phrases

Une vente de service fourni par voie électronique par une entreprise **française** à un consommateur **français** est une opération purement interne : le lieu d'imposition est la France, et il n'y a ni OSS ni seuil intra-UE à considérer. Le guichet OSS et le seuil de 10 000 € cité par [Stripe — Tax in the European Union](https://docs.stripe.com/tax/supported-countries/european-union) ne concernent que les ventes **transfrontalières** vers des consommateurs d'autres États membres — **ce n'est pas le sujet du ticket**, et le seul point à surveiller le jour où ouvrance vendrait hors de France est que ce dossier redevient ouvert.

---

## 6. Archivage : dix ans, et Stripe n'en promet aucun

### 6.1 [DOC] Ce que Stripe s'engage à conserver

[Stripe Services Agreement § 4.4](https://stripe.com/legal/ssa), verbatim :

> « **Stripe is not obligated to retain data that it receives from or through User after the Term**, except as (a) required by Law; (b) reasonably required for Stripe to perform any post-termination obligations; (c) this Agreement otherwise states; or (d) the parties otherwise agree in writing. »

[Stripe — Data retention policy](https://support.stripe.com/questions/data-retention-policy), verbatim :

> « [Stripe is] required to comply with many regulations, including anti-terrorism and anti-money laundering laws. **Some of these regulations and laws require Stripe to retain transactional records for a prescribed period of time.** »

**Aucune durée n'y est chiffrée.** La page renvoie à la politique de confidentialité et au Privacy Center.

### 6.2 [DOC] Ce que l'export permet

| Moyen | Ce que la doc en dit, verbatim | Limite |
| --- | --- | --- |
| **API `List`** | [List all invoices](https://docs.stripe.com/api/invoices/list) : « The invoices are returned sorted by creation date, with the most recently created invoices appearing first. » `limit` — « **Limit can range between 1 and 100, and the default is 10.** » ; curseurs `starting_after` / `ending_before` | Pagination à 100 par page ; **exhaustif par curseur**, mais ne récupère que les **objets JSON**, pas les PDF |
| **Sigma** | [Fonctionnement de Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard) : « Sigma fournit un environnement SQL interactif dans le Dashboard Stripe pour interroger vos données transactionnelles. […] **Toutes les données sont en lecture seule** » | Tables `invoices`, `credit_notes`, `refunds`, `charges` disponibles ([fraîcheur des données](https://docs.stripe.com/stripe-data/available-data), 3 h). **Abonnement payant** ; annulable, et l'accès cesse à la fin du cycle |
| **Fraîcheur** | [Sigma — fraîcheur des données](https://docs.stripe.com/stripe-data/available-data) : « Sigma rend la plupart des données de transactions Stripe disponibles pour interrogation dans **un délai de trois heures**. » | Fraîcheur ≠ profondeur d'historique |

> **[ZONE GRISE] — la profondeur de l'historique.** Aucune page consultée n'indique **jusqu'où remonte** l'historique interrogeable dans Sigma, ni combien de temps un `invoice_pdf` reste téléchargeable. Les pages Sigma documentent la **fraîcheur** (à quelle vitesse une donnée arrive), jamais la **rétention** (combien de temps elle reste).

### 6.3 La conclusion, encadrée

> **Non, s'en remettre à Stripe pour la conservation décennale n'est pas acceptable.** Trois raisons, toutes sourcées :
>
> 1. **Stripe écrit qu'il n'y est pas tenu.** SSA § 4.4 : « not obligated to retain data […] after the Term ». Le jour où le compte ouvrance ferme, l'obligation de Stripe s'éteint ; celle d'ouvrance court encore dix ans ([L123-22](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006219327)).
> 2. **Aucune durée n'est promise nulle part.** La page de rétention parle d'obligations réglementaires *pesant sur Stripe* (LCB-FT), qui ne sont ni les obligations comptables d'ouvrance, ni un engagement envers elle.
> 3. **L'accès est conditionné à l'abonnement.** Sigma est payant et son accès cesse à la résiliation ; les liens de reçus expirent à 30 jours ; la durée de vie des `invoice_pdf` n'est pas documentée.
>
> **Ce qui reste à faire côté ouvrance, quelle que soit l'option retenue en section 2** : rapatrier et stocker, chez ouvrance, la pièce **et** son PDF, dès l'émission — pas au moment du contrôle. Les moyens documentés existent (webhook `invoice.paid` puis téléchargement de `invoice_pdf` ; `List` paginé en filet de sécurité ; Sigma pour le rapprochement). **Le choix du moyen n'est pas tranché ici.**

---

## 7. Stripe et la réforme française de la facturation électronique

### 7.1 [TEXTE] Le calendrier officiel

[impots.gouv.fr — Facturation électronique et plateformes agréées](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees) et le [guide pratique de démarrage au 1er septembre 2026](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf) :

- **1er septembre 2026** — obligation de **réception** de factures électroniques généralisée à toutes les entreprises assujetties, et obligation d'**émission** pour les grandes entreprises et les ETI. Le passage par une **plateforme agréée** (PA, anciennement PDP) est requis pour transmettre et recevoir, et pour transmettre les données de transaction et de paiement à l'administration.
- **1er septembre 2027** — obligation d'**émission** pour les PME et les **microentreprises**.
- L'**e-reporting** suit le même calendrier.

Cohérent avec [l'article 242 nonies A de l'annexe II au CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046086694/), dont les dispositions s'appliquent « à compter du 1er septembre 2027 pour les factures émises par les assujettis appartenant aux catégories des microentreprises et des petites et moyennes entreprises ».

**Une précision qui compte pour ouvrance** : la réforme e-invoicing vise le **B2B**. ouvrance vend en **B2C** à des consommateurs français. La branche qui la concerne au premier chef est donc l'**e-reporting** (transmission des données de transaction), pas l'émission de factures structurées entre assujettis. **[ZONE GRISE]** : le périmètre exact de l'e-reporting applicable à une micro-entreprise B2C en franchise en base **n'a pas été vérifié verbatim** dans cette recherche. **À faire trancher.**

### 7.2 [DOC] Ce que Stripe déclare, au 7 septembre 2026

C'est écrit noir sur blanc, et c'est net. [Stripe — Facturation électronique](https://docs.stripe.com/invoicing/e-invoicing), verbatim :

> « **Stripe Invoicing crée des enregistrements de facture et expose les données de facture via notre API et nos webhooks, mais ne génère ni ne transmet de fichiers de facture électronique conformes à la loi par lui-même.** Pour vous conformer aux mandats de facturation électronique, vous pouvez utiliser des fournisseurs tiers du Stripe App Marketplace ou créer une intégration personnalisée à l'aide des webhooks Stripe. »

Et la raison qu'il en donne, verbatim :

> « Étant donné que les formats de facturation électronique, les réseaux de transmission et les règles de conformité diffèrent d'un pays à l'autre et changent fréquemment, **Stripe s'appuie sur des fournisseurs tiers spécialisés** pour gérer la génération, la validation et la livraison. »

Deux voies sont documentées, aucune n'est native :

| Voie | Verbatim |
| --- | --- |
| **App Marketplace** | « Le partenaire de facturation électronique **privilégié** de Stripe est **Billit**, mais plusieurs fournisseurs sont disponibles sur le Stripe App Marketplace. L'utilisation d'une application Stripe permet une configuration no-code : l'application lit vos données de facture Stripe et gère la conversion de format et la transmission **en votre nom**. » |
| **Webhook maison** | « Plus flexible pour les flux de travail personnalisés, les relations de fournisseur de facturation électronique existantes ou **les pays non couverts par Billit**. » Le flux documenté : écouter `invoice.created` (« Vous pouvez également utiliser `invoice.finalized`, mais comme les factures finalisées ne peuvent pas être modifiées, vous ne pourrez pas modifier la facture directement si l'autorité gouvernementale rejette votre envoi ») → récupérer l'`Invoice` → transformer au format attendu → « Stockez la confirmation du fournisseur, l'ID du document et l'état de la transmission **pour vos dossiers**. » |

> **Réponse directe.** Au **7 septembre 2026**, **il n'existe aucune page Stripe officielle annonçant un support natif de la réforme française** : pas de page « France e-invoicing », pas de statut de Plateforme Agréée / PDP pour Stripe, pas de génération de Factur-X. La page produit dit le contraire en toutes lettres : Stripe « **ne génère ni ne transmet de fichiers de facture électronique conformes à la loi par lui-même** ».
>
> **[ZONE GRISE] — le statut de Billit.** Plusieurs sources tierces (blogs de prestataires, non retenues comme sources primaires ici) présentent Billit comme immatriculée Plateforme Agréée par l'administration fiscale française. **Cette immatriculation n'a pas été vérifiée** sur la liste officielle de la DGFiP dans cette recherche. Stripe se contente d'écrire que Billit est son « partenaire privilégié » et qu'il « prend en charge la facturation électronique dans plusieurs pays » — **sans nommer la France**. **À vérifier sur la liste officielle avant toute décision.**

---

## Ce que Stripe peut porter, et ce qu'il ne peut pas

Trois colonnes. La deuxième répond à la question du ticket ; la troisième dit ce qui reste, sans dire comment le faire.

| Obligation | Stripe le porte ? | Ce qu'il reste à faire côté ouvrance |
| --- | --- | --- |
| **Numérotation unique, chronologique et continue** ([BOFiP § 70](https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-10-20131018)) | **Reçu : non** — `receipt_number` est un « transaction number », `null` tant qu'aucun reçu n'est envoyé, règle de formation non documentée.<br>**Invoicing : oui** — séquençage au niveau du compte (défaut UE), préfixe réglable, numéro attribué à la **finalisation**, brouillon supprimé sans numéro, facture `void` gardant le sien | Choisir et **figer** le système de numérotation avant la première facture (le compteur ne peut qu'avancer). Vérifier empiriquement en mode test que les brouillons supprimés ne trouent pas la séquence. Décider si la séquence Stripe **est** la séquence d'ouvrance ou si ouvrance en tient une propre |
| **Mention « TVA non applicable, art. 293 B du CGI »** ([BOFiP § 450](https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-10-20131018)) | **Reçu : non** — aucun champ de texte libre documenté.<br>**Invoicing : un emplacement, pas la mention** — `footer` (« texte obligatoire contractuel ou juridique ») ou l'un des quatre `custom_fields` (« Conformité fiscale ») | Rédiger la mention, la placer, et **vérifier son libellé en vigueur** après la recodification du 1er septembre 2026 (§ 0.1). Ne pas laisser apparaître de ligne de taxe à 0 |
| **SIREN / identification du vendeur** | **Partiellement** — les informations publiques du compte (dénomination, adresse, e-mail, site) figurent sur les reçus **et** les factures ; `account_tax_ids` s'affiche sur les deux, mais est typé « tax ID » par pays, pas SIREN, et **non modifiable** une fois posé | Vérifier ce que le PDF affiche réellement. Si aucun champ typé ne convient, le SIREN passe par `footer` ou `custom_fields` — donc **Invoicing seulement**, jamais sur un reçu |
| **Émetteur = ouvrance** ([CGI art. 289, I-2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413)) | **Oui, techniquement** — `issuer: { type: "self" }`, et Stripe renvoie trois fois la responsabilité au marchand. Mais **Stripe ne se déclare pas mandataire** : le SSA lu ne contient pas de clause en ce sens | Établir et conserver la trace du **mandat de facturation** (BOFiP § 120 ; **écrit obligatoire** si le mandataire est hors UE, § 260). Vérifier l'entité Stripe contractante. Assumer que la responsabilité de conformité reste entière (BOFiP § 170) |
| **Avoir sur remboursement total ou partiel** | **Sans Invoicing : non** — un `Refund` ne produit qu'un e-mail et un reçu réécrit ; un remboursement immédiat devient une « annulation » qui ne laisse **aucune trace** chez le client.<br>**Avec Invoicing : oui** — `CreditNote` numéroté, PDF, `memo`, `effective_at`, partiel, multiple. Mais `invoice` est **requis** : pas d'avoir sans facture | Décider si les **Suppléments** sont des postes distincts de la facture (sinon l'avoir passe par un « poste personnalisé » que Stripe déconseille). Anticiper l'irréversibilité : un avoir sur facture `paid` ne s'annule pas. Ne pas mélanger Refund API et avoirs sans suivre le plafond commun |
| **Conservation dix ans** ([C. com. L123-22](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006219327)) | **Non** — SSA § 4.4 : « not obligated to retain data […] after the Term » ; aucune durée chiffrée nulle part ; liens de reçus morts à 30 jours ; durée de vie des `invoice_pdf` non documentée ; Sigma payant et résiliable | Rapatrier **la pièce et son PDF** chez ouvrance dès l'émission, pas au contrôle. Moyens documentés disponibles : webhook `invoice.paid` + `invoice_pdf`, `List` paginé (100/page), Sigma pour le rapprochement |
| **Facturation électronique / e-reporting France** ([impots.gouv.fr](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees)) | **Non** — « Stripe Invoicing […] **ne génère ni ne transmet de fichiers de facture électronique conformes à la loi par lui-même** ». Aucune page officielle Stripe « France e-invoicing », aucun statut de Plateforme Agréée | Échéance **1er septembre 2027** pour l'émission par une microentreprise ; réception due depuis le 1er septembre 2026. Voies documentées : app du Marketplace (Billit, **statut PA France non vérifié**) ou intégration webhook vers une PA. Déterminer d'abord le périmètre e-reporting réellement applicable à une vente **B2C** en franchise |

---

## Ce qui reste ouvert

Sept points qu'aucune source primaire consultée ne tranche, rassemblés pour ne pas les perdre :

1. **Le libellé de la mention 293 B** après la recodification du 1er septembre 2026 (§ 0.1).
2. **La règle de formation de `receipt_number`** — nulle part documentée (§ 1.4).
3. **La confirmation empirique** que la suppression d'un brouillon ne troue pas la séquence (§ 2.2).
4. **La durée de vie d'un `invoice_pdf`** et la profondeur d'historique de Sigma (§ 2.5, § 6.2).
5. ~~**L'entité Stripe contractante** d'ouvrance, qui commande l'exigence d'un mandat écrit (§ 4.2).~~ **Refermé le 7 septembre 2026.** Le [Stripe Services Agreement](https://stripe.com/legal/ssa), section 12, tableau « Europe, Middle East and Africa », désigne **`Stripe Payments Europe, Limited`** (Irlande) pour un marchand français. Le mandataire est donc **dans l'Union** : le § 260 du BOFiP, qui impose un contrat écrit hors UE, **ne s'applique pas**. Le mandat peut rester tacite, mais il doit rester démontrable (§ 120).
6. **Le périmètre e-reporting** applicable à une micro-entreprise B2C en franchise (§ 7.1).
7. ~~**Le statut de Plateforme Agréée France de Billit**, à vérifier sur la liste officielle DGFiP (§ 7.2).~~ **Refermé le 7 septembre 2026.** La liste officielle DGFiP a été téléchargée et dépouillée : **BILLIT y est immatriculée depuis le 19/12/2025**, parmi 149 opérateurs ayant réussi les tests (16 autres en attente de test d'interopérabilité). **Stripe est absent des deux listes**, ce qui confirme le § 7.2. Y figurent aussi Tiime (18/12/2025), Indy (09/01/2026), Abby (29/01/2026), Qonto (18/12/2025) et Pennylane (11/12/2025). [Liste officielle](https://www.impots.gouv.fr/liste-des-plateformes-de-dematerialisation-partenaires-pdp-immatriculees-sous-reserve).

Les points 1, 5, 6 et 7 relèvent d'un expert-comptable ou d'un avocat fiscaliste. Les points 2, 3 et 4 se règlent par une manipulation en mode test.
