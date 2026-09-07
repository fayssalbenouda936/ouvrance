# Volet facturation — obligation d'émettre, mentions, numérotation, facture électronique, conservation

**Recherche du ticket [#36](https://github.com/fayssalbenouda936/ouvrance/issues/36).** Pages consultées le **7 septembre 2026**. Extraits verbatim, chaque affirmation porte sa source.

Ce document traite une seule question : **que le droit français impose-t-il réellement à ouvrance en matière de facturation ?** Il part du doute posé au ticket — l'idée reçue « en B2C on ne facture pas, une note suffit » — et va lire les textes.

> ⚠️ **Ce document n'est pas un avis juridique.** Il est écrit par un agent, pas par un expert-comptable ni par un avocat. Trois registres sont distingués partout et il faut les lire comme tels :
> - **[TEXTE]** — ce que la loi, le décret ou l'arrêté dit, verbatim, avec sa référence.
> - **[ADMIN]** — la doctrine BOFiP, une FAQ de la DGFiP, une fiche service-public. **Opposable en pratique** (le BOFiP l'est au sens de l'art. L80 A du LPF), mais ce n'est pas la loi.
> - **[ZONE GRISE]** — ce qu'aucune source primaire ne tranche. **À faire trancher par un expert-comptable ou un avocat.**

**Vocabulaire.** Les termes du domaine sont ceux de [`CONTEXT.md`](../../CONTEXT.md) : l'**Offrant** passe la **Commande** et paie, le **Destinataire** ouvre le lien, la **Formule** fixe le prix et le quota, le **Supplément** est un **Souvenir** au-delà du quota, la **Validation** est la porte humaine et la **Livraison** l'envoi du lien. **Une Commande existe dès le formulaire, avant tout paiement** — ce point est décisif pour la section 4.

**Chiffres du dossier**, tenus pour acquis et non vérifiés ici : EI Fayssal BENOUDA, SIREN **980207898**, SIRET siège 98020789800050, APE 63.11Z, créée le 17/12/2025. Micro-entreprise en **franchise en base de TVA** (art. 293 B du CGI). Formule carte animée **14,99 €**, Supplément **2 €**, plafond **28,99 €**. Formule jeu premium **69,99 €**, Supplément **3 €**, plafond **84,99 €**. Aucune facture émise à ce jour ; seul le reçu automatique Stripe.

---

## 1. L'obligation de facturer entre un professionnel et un particulier

### 1.1 [TEXTE] L'article 289 du CGI ne vise pas le particulier

[Légifrance, art. 289 du CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413), version en vigueur depuis le 31 décembre 2023, I-1, verbatim :

> « **Tout assujetti doit s'assurer qu'une facture est émise**, par lui-même, ou en son nom et pour son compte, par son client ou par un tiers :
>
> a. Pour les livraisons de biens ou les prestations de services qu'il effectue **pour un autre assujetti, ou pour une personne morale non assujettie**, et qui ne sont pas exonérées en application des articles 261 à 261 E ;
>
> b. Pour les livraisons de biens mentionnées à l'article 258 A et pour les livraisons de bien exonérées en application des I et III de l'article 262 ter et du II de l'article 298 sexies […] ;
>
> c. Pour les acomptes qui lui sont versés avant que l'une des opérations visées aux a et b ne soit effectuée […] ;
>
> d. Pour les livraisons aux enchères publiques de biens d'occasion, d'œuvres d'art, d'objets de collection ou d'antiquité. »

La liste est fermée. Le a vise « un autre **assujetti** » ou une « **personne morale** non assujettie ». Un consommateur français — personne **physique** non assujettie — n'est **ni l'un ni l'autre**. Les b, c et d ne concernent aucune opération d'ouvrance.

Et le I-3, premier alinéa, qui commande tout le calendrier d'émission :

> « **La facture est, en principe, émise dès la réalisation de la livraison ou de la prestation de services.** »

### 1.2 [ADMIN] Le BOFiP le dit en toutes lettres

[BOI-TVA-DECLA-30-20-10-10](https://bofip.impots.gouv.fr/bofip/13242-PGP.html/identifiant=BOI-TVA-DECLA-30-20-10-10-20211222), « Opérations donnant lieu à facturation », version du 22/12/2021, **§ 20**, verbatim :

> « Sous réserve de la remarque figurant ci-dessous et pour certaines catégories d'opérations visées au II § 30 à 80, au IV § 100 à 110 et au VI § 140, **l'obligation fiscale de délivrance de facture ne concerne pas les assujettis qui livrent des biens ou rendent des services à des particuliers.** »

Le même § 20 pose l'exception, qui ne concerne pas ouvrance :

> « Il existe une obligation particulière de facturation en matière de **travaux immobiliers** réalisés en faveur de particuliers. En effet, l'article 290 quinquies du CGI impose aux prestataires de services de délivrer une note pour toute prestation comportant l'exécution de travaux immobiliers, assortie ou non de vente, fournie à des particuliers. »

Le BOFiP ajoute que le fournisseur qui **doute** de la qualité d'assujetti de son client a intérêt à facturer quand même.

### 1.3 [TEXTE] L'article L441-9 du Code de commerce est bien B2B — et seulement B2B

[Légifrance, art. L441-9 du Code de commerce](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414397/), version en vigueur du 26 avril 2019 au 1er janvier 2027, I premier alinéa, verbatim :

> « **Tout achat de produits ou toute prestation de service pour une activité professionnelle fait l'objet d'une facturation.** »

Le champ est dans la lettre : « **pour une activité professionnelle** ». C'est l'achat du *client* qui doit être professionnel. Un Offrant qui achète un Cadeau pour un proche n'achète pas pour une activité professionnelle : l'article ne s'applique pas.

Ce qui suit dans le même article (noms et adresses des parties, adresse de facturation si différente, date de l'opération, quantité, dénomination précise, prix unitaire HT, réductions, date de règlement, conditions d'escompte, taux de pénalités de retard, indemnité forfaitaire de recouvrement) ne s'impose donc pas non plus à ouvrance tant que ses clients sont des consommateurs. **L'amende administrative de 75 000 € (personne physique) / 375 000 € (personne morale)** que prévoit le II du même article sanctionne les manquements à ce régime B2B, pas les ventes B2C.

> **Attention à la date.** Légifrance donne à cette version un terme au **1er janvier 2027**. Une version postérieure existe ; ce document ne l'a pas lue. **[ZONE GRISE]** — à revérifier avant janvier 2027.

### 1.4 [TEXTE] La note obligatoire pour les prestations de services : le seuil de 25 € est toujours en vigueur

Le fondement légal est l'[article L112-1 du Code de la consommation](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032227331), version en vigueur depuis le 1er juillet 2016, verbatim :

> « Tout vendeur de produit **ou tout prestataire de services** informe le consommateur, par voie de marquage, d'étiquetage, d'affichage ou par tout autre procédé approprié, sur les prix **et les conditions particulières de la vente et de l'exécution des services**, selon des modalités fixées **par arrêtés du ministre chargé de l'économie**, après consultation du Conseil national de la consommation. »

L'arrêté d'application est l'[arrêté n° 83-50/A du 3 octobre 1983 relatif à la publicité des prix de tous les services](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000494187/). **Légifrance donne l'état du texte au 7 septembre 2026 : « En vigueur ».** Sa dernière modification date du 9 septembre 2010 (arrêté du 15 juillet 2010, qui a converti le seuil en euros).

[**Article 1er**](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459194), verbatim :

> « **Toute prestation de service doit faire l'objet, dès qu'elle a été rendue et en tout état de cause avant paiement du prix, de la délivrance d'une note lorsque le prix de la prestation est supérieur ou égal à 25 € (TVA comprise).** »
>
> Pour les prestations dont le prix est inférieur à 25 € TTC, **la délivrance d'une note est facultative, mais elle doit être remise au client s'il la demande.**

[**Article 2**](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459002), verbatim :

> « Les conditions dans lesquelles la délivrance d'une note est obligatoire ou facultative doivent être rappelées à la clientèle **par un affichage lisible au lieu où s'exécute le paiement du prix**. »

[**Article 3**](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459003) — les mentions de la note :

> « La date de rédaction de la note ; le nom et **l'adresse du prestataire** ; le nom du client, sauf opposition de celui-ci ; la date et le lieu d'exécution de la prestation ; le **décompte détaillé, en quantité et prix, de chaque prestation et produit fourni** ; **la somme totale à payer hors taxes et toutes taxes comprises**. »
>
> Le décompte détaillé devient facultatif lorsqu'un devis descriptif et détaillé a été préalablement établi, accepté par le client et conforme aux travaux effectués.

[**Article 4**](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459004) :

> « **La note doit être établie en double exemplaire. L'original est remis au client, le double doit être conservé par le prestataire** [pendant deux ans, classé par ordre de date de rédaction]. »

[**Article 5**](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459005) — le champ :

> « Le présent arrêté **s'applique à tous les services**, sauf dispositions particulières à certains d'entre eux, et sans préjudice des autres réglementations concernant la publicité des prix. »

[**Article 6**](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459006/2026-03-25) porte la durée de conservation des notes à **deux ans**. Légifrance donne cet article « En vigueur » au 25 mars 2026.

**Le seuil de 25 € est-il toujours celui de 2026 ?** Oui. Deux vérifications convergentes :
1. Légifrance affiche l'arrêté « **En vigueur au 07/09/2026** » avec l'article 1er inchangé depuis le 9 septembre 2010.
2. La [question écrite n° 07523 du sénateur Antoine Lefèvre, publiée le 5 février 2026](https://www.senat.fr/questions/base/2026/qSEQ260207523.html), interroge le gouvernement sur l'articulation entre « l'arrêté du 3 octobre 1983 imposant la remise d'une note avant paiement pour toute prestation supérieure à 25 € TTC » et l'interdiction d'impression des tickets issue de la loi AGEC. Le seuil y est présenté comme le droit en vigueur en février 2026. **La question est encore « en attente de réponse du Ministère »** au moment de la consultation : aucune évolution acquise, mais un signal que le texte est sur la table.

### 1.5 Application aux prix d'ouvrance

Le seuil se lit sur le **prix TTC de la prestation**. En franchise en base, aucune TVA n'est facturée : le TTC est le prix payé.

| Panier | Prix payé | Note (arrêté 83-50/A) |
| --- | --- | --- |
| Carte animée seule | 14,99 € | **Facultative** — mais obligatoire **si l'Offrant la demande** |
| Carte animée + 1 à 5 Suppléments | 16,99 € → 24,99 € | **Facultative** — sur demande |
| Carte animée + 6 Suppléments | **26,99 €** | **Obligatoire** |
| Carte animée + 7 Suppléments (plafond) | **28,99 €** | **Obligatoire** |
| Jeu premium seul | **69,99 €** | **Obligatoire** |
| Jeu premium + Suppléments | 72,99 € → 84,99 € | **Obligatoire** |

Le basculement se fait donc **au 6ᵉ Supplément** sur la Formule carte animée. Sur la Formule jeu premium, la note est obligatoire dans tous les cas.

### 1.6 [ZONE GRISE] Trois angles morts de l'arrêté de 1983 en vente à distance

L'arrêté a été écrit pour le coiffeur et le garagiste. Trois de ses termes n'ont pas d'équivalent évident en ligne, et **aucune source primaire ni doctrinale consultée ne les transpose** :

1. **« avant paiement du prix ».** L'arrêté suppose une prestation rendue *puis* payée. Chez ouvrance, l'Offrant paie par Stripe **avant** la Livraison. Faut-il alors délivrer la note au moment du paiement (le prix est connu, la prestation ne l'est pas encore) ou au moment de la Livraison (la prestation est rendue, mais le paiement est passé) ? Le texte ne permet pas de trancher.
2. **« affichage lisible au lieu où s'exécute le paiement du prix » (art. 2).** Il n'y a pas de lieu physique. Un équivalent en ligne — une mention sur la page de paiement — est plausible mais **non sourcé**.
3. **« la note doit être établie en double exemplaire » (art. 4).** Rédigé pour le carnet à souche. Ce que « double exemplaire » veut dire pour un PDF n'est écrit nulle part.

**À faire trancher par un expert-comptable.** Le risque est celui d'une amende contraventionnelle de publicité des prix, pas un redressement fiscal.

> **Conclusion de la section 1 — ce que ça change pour ouvrance.**
>
> **L'idée reçue est fausse à moitié, et la moitié fausse est la plus coûteuse.**
>
> - **Vrai** : l'article 289 du CGI **n'impose pas** de facture pour une vente à un consommateur personne physique, et le BOFiP le confirme mot pour mot (§ 20). L'article L441-9 du Code de commerce **ne s'applique pas** non plus : son champ est l'achat « pour une activité professionnelle ».
> - **Faux** : « une note suffit » sous-entend que la note serait un pis-aller optionnel. Ce n'est pas le cas. **Au-dessus de 25 € TTC, la note est obligatoire** — de plein droit, sans demande du client — et l'arrêté fixe ses mentions, sa remise en double exemplaire et sa conservation deux ans. **Le jeu premium à 69,99 € y est toujours ; la carte animée y bascule au 6ᵉ Supplément.**
> - **Sous 25 €, la note reste obligatoire dès que l'Offrant la demande.** « Facultatif » ne veut pas dire « refusable ».
> - Le reçu automatique Stripe ne satisfait aucune de ces exigences telles qu'elles sont écrites : voir la grille du § 2.4.

---

## 2. Vente à distance de contenu numérique : deux obligations qui ne se recouvrent pas

### 2.1 [TEXTE] Article L221-13 — la confirmation du contrat sur support durable

[Légifrance, art. L221-13 du Code de la consommation](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563210), version en vigueur depuis le 28 mai 2022 (ord. n° 2021-1734 du 22 décembre 2021, art. 6), verbatim :

> « Le professionnel fournit au consommateur, **sur support durable**, dans un délai raisonnable, après la conclusion du contrat et **au plus tard au moment de la livraison du bien ou avant le début de l'exécution du service ou du contrat de fourniture de contenu numérique fourni sans support matériel ou de services numériques, la confirmation du contrat comprenant toutes les informations prévues à l'article L. 221-5**, sauf si le professionnel les lui a déjà fournies, sur un support durable, avant la conclusion du contrat. Le contrat est accompagné du **formulaire type de rétractation** mentionné au 7° du même article.
>
> Le cas échéant, le professionnel fournit au consommateur, dans les mêmes conditions et **avant l'expiration du délai de rétractation, la confirmation de son accord exprès pour la fourniture d'un contenu numérique non présenté sur un support matériel et de la reconnaissance de la perte de son droit de rétractation.** »

Ce que ce texte impose, et qui n'est pas une facture : **toutes les informations de l'article L221-5** (identité et coordonnées du professionnel, caractéristiques essentielles du service, prix, date ou délai d'exécution, modalités de paiement, existence et modalités du droit de rétractation, garanties, etc.), **plus le formulaire type de rétractation**, **plus** — quand l'exécution anticipée a été demandée — la confirmation de l'accord exprès et de la reconnaissance de la perte du droit.

### 2.2 [TEXTE] Article L221-25 — l'exécution avant la fin du délai de rétractation

[Légifrance, art. L221-25 du Code de la consommation](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000044563179), version en vigueur depuis le 28 mai 2022, premier alinéa, verbatim :

> « **Si le consommateur souhaite que l'exécution d'une prestation de services ou d'un contrat mentionné au premier alinéa de l'article L. 221-4 commence avant la fin du délai de rétractation prévu à l'article L. 221-18 et si le contrat soumet le consommateur à une obligation de payer, le professionnel recueille sa demande expresse par tout moyen pour les contrats conclus à distance** et sur papier ou sur support durable pour les contrats conclus hors établissement. »

Les alinéas suivants : le professionnel demande au consommateur de **reconnaître** qu'il ne disposera plus du droit de rétractation après exécution complète du contrat ; le consommateur qui se rétracte en cours d'exécution verse un montant proportionné au service fourni jusqu'à sa demande ; et **aucune somme n'est due** si la demande expresse n'a pas été recueillie conformément au premier alinéa ou si le professionnel n'a pas respecté ses obligations d'information.

Le pendant, pour le **contenu numérique sans support matériel**, est l'[article L221-26](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563174) : le consommateur ne doit **aucune somme** si le professionnel n'a pas obtenu son accord exprès préalable **et** la preuve qu'il a reconnu perdre son droit de rétractation.

### 2.3 Un email de confirmation vaut-il facture ?

**Non — et la question porte mal.** Ce sont deux obligations différentes, de codes différents, avec des contenus différents et des sanctions différentes. Elles peuvent **coexister sur un même document**, mais l'une ne dispense jamais de l'autre.

| | **Confirmation L221-13** | **Note (arrêté 83-50/A)** | **Facture (289 CGI)** |
| --- | --- | --- | --- |
| **Source** | Code de la consommation | Code de la consommation + arrêté | CGI |
| **Déclenchée par** | Tout contrat à distance B2C | Prestation ≥ 25 € TTC, ou sur demande | Client assujetti / personne morale non assujettie |
| **Due à ouvrance ?** | **Oui, toujours** | **Oui** au-dessus de 25 € ; sur demande en dessous | **Non** tant que le client est un particulier |
| **Support** | **Support durable** exigé | Non précisé ; « double exemplaire » (art. 4) | Papier ou électronique (289 V à VII) |
| **Moment** | Au plus tard **avant le début de l'exécution** | Dès la prestation rendue et **avant paiement** | Dès la réalisation de la prestation (289 I-3) |
| **Contenu** | Toutes les infos L221-5 + formulaire de rétractation | 6 mentions de l'art. 3 | 18 mentions du 242 nonies A |
| **Sanction du manquement** | Nullité du droit de percevoir (L221-25 al. 3, L221-26) | Publicité des prix | Amende fiscale (art. 1737 CGI) |

Deux différences suffisent à interdire la confusion : la confirmation L221-13 **n'exige aucun décompte quantité/prix par ligne** (l'art. 3 de l'arrêté, si) ; et l'arrêté **n'exige aucun formulaire de rétractation** (L221-13, si).

### 2.4 Le reçu Stripe, mesuré contre les trois grilles

**[ZONE GRISE]** — cette ligne-ci est un raisonnement, pas une source. Le contenu exact du reçu Stripe d'ouvrance n'a pas été lu dans le cadre de cette recherche. Ce qui suit est la grille à lui appliquer, pas un verdict :

| Exigence | Où elle est écrite | Un reçu de paiement générique la couvre-t-il ? |
| --- | --- | --- |
| Nom **et adresse du prestataire** | Arrêté art. 3 ; 242 nonies A 1° | À vérifier — dépend de ce qui est configuré côté Stripe |
| Date **et lieu d'exécution de la prestation** | Arrêté art. 3 | Non : un reçu porte la date du **paiement**, pas de l'exécution |
| Décompte détaillé **en quantité et prix de chaque prestation** | Arrêté art. 3 | À vérifier — la Formule et chaque Supplément doivent apparaître |
| Somme totale **HT et TTC** | Arrêté art. 3 | Partiellement — en franchise en base HT = TTC, mais les deux lignes sont exigées |
| Toutes les informations **L221-5** | L221-13 | Non |
| **Formulaire type de rétractation** | L221-13 | Non |
| **Accord exprès** + reconnaissance de la perte du droit | L221-13 al. 2, L221-25, L221-26 | Non |
| Mention **TVA non applicable, art. 293 B du CGI** | BOI-TVA-DECLA-40-10-20 § 50 (voir 3.3) | Non, sauf configuration |

> **Conclusion de la section 2 — ce que ça change pour ouvrance.**
>
> - **La confirmation de l'article L221-13 est due sur chaque Commande payée, quel que soit le prix.** Elle n'a pas de seuil. Elle est due **avant le début de l'exécution**, donc **avant la Validation et la production**, pas au moment de la Livraison.
> - Elle **ne vaut pas note** et **ne vaut pas facture** : les contenus exigés ne se recouvrent que partiellement.
> - La sanction du manquement à L221-25 / L221-26 n'est pas une amende : c'est que **le consommateur ne doit aucune somme**. Sur un produit prépayé, cela signifie un **remboursement intégral exigible** alors que le Cadeau a déjà été produit et livré.
> - Un reçu Stripe seul ne coche, au mieux, qu'une partie de la première colonne. **Il n'a jamais été conçu pour couvrir L221-13.**

---

## 3. Les mentions obligatoires, si facture il y a

Cette section s'applique **dès qu'ouvrance choisit d'émettre une facture** (facturation volontaire), et **s'imposera** le jour où un Offrant sera un professionnel agissant pour son activité.

### 3.1 [TEXTE] L'article 242 nonies A de l'annexe II au CGI, verbatim

[Légifrance, art. 242 nonies A de l'annexe II au CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050811276), version en vigueur depuis le **1er janvier 2025** (décret n° 2024-1195 du 21 décembre 2024, art. 1). **Le I**, verbatim :

> « **1°** Le nom complet, **le numéro d'identification mentionné au premier alinéa de l'article R. 123-221 du code de commerce et l'adresse** de l'assujetti et de son client ;
>
> **2°** Le numéro individuel d'identification attribué à l'assujetti en application de l'article 286 ter du code précité et sous lequel il a effectué la livraison de biens ou la prestation de services ;
>
> **3°** Les numéros d'identification à la taxe sur la valeur ajoutée du vendeur et de l'acquéreur pour les livraisons désignées au I de l'article 262 ter du code précité ;
>
> **4°** Le numéro d'identification à la taxe sur la valeur ajoutée du prestataire ainsi que celui fourni par le preneur pour les prestations pour lesquelles le preneur est redevable de la taxe ;
>
> **5°** Lorsque le redevable de la taxe est un représentant fiscal au sens de l'article 289 A du code précité, le numéro individuel d'identification attribué à ce représentant fiscal […] ;
>
> **5° bis** Lorsque la livraison de biens ou la prestation de services est effectuée par le membre d'un assujetti unique constitué en application de l'article 256 C du code général des impôts, la mention " Membre d'un assujetti unique " […] ;
>
> **6°** Sa date d'émission ;
>
> **7° Un numéro unique basé sur une séquence chronologique et continue ; la numérotation peut être établie dans ces conditions par séries distinctes lorsque les conditions d'exercice de l'activité de l'assujetti le justifient ; l'assujetti doit faire des séries distinctes un usage conforme à leur justification initiale ;**
>
> **7° bis** L'adresse de livraison des biens si elle est différente de l'adresse du client ;
>
> **8°** Pour chacun des biens livrés ou des services rendus, **la quantité, la dénomination précise, le prix unitaire hors taxes et le taux de taxe sur la valeur ajoutée légalement applicable ou, le cas échéant, le bénéfice d'une exonération** ;
>
> **8° bis** L'information selon laquelle les opérations donnant lieu à facture sont constituées exclusivement de livraisons de biens ou exclusivement de prestations de services ou sont constituées de ces deux catégories d'opérations ;
>
> **9°** Tous rabais, remises, ristournes ou escomptes acquis et chiffrables lors de l'opération et directement liés à cette opération ;
>
> **10°** La date à laquelle est effectuée, ou achevée, la livraison de biens ou la prestation de services ou la date à laquelle est versé l'acompte visé au c du 1 du I de l'article 289 du code précité, **dans la mesure où une telle date est déterminée et qu'elle est différente de la date d'émission de la facture** ;
>
> **11°** Le montant de la taxe à payer et, par taux d'imposition, le total hors taxe et la taxe correspondante mentionnés distinctement ;
>
> **11° bis** Lorsque le prestataire a opté pour le paiement de la taxe d'après les débits, la mention : " Option pour le paiement de la taxe d'après les débits " ;
>
> **12° En cas d'exonération, la référence à la disposition pertinente du code général des impôts ou à la disposition correspondante de la directive 2006/112/CE** du Conseil du 28 novembre 2006 […] ou à toute autre mention indiquant que l'opération bénéficie d'une mesure d'exonération ;
>
> **13°** Lorsque l'acquéreur ou le preneur est redevable de la taxe, la mention : " Autoliquidation " ;
>
> **14°** Lorsque l'acquéreur ou le preneur émet la facture au nom et pour le compte de l'assujetti, la mention : " Autofacturation " ;
>
> **15°** […] " Régime particulier-Agences de voyages " ; **16°** […] " Régime particulier-Biens d'occasion " […] ; **17°** […] moyen de transport neuf […] ; **18°** […] enchères publiques […]. »

Et **le II**, qui allège la liste pour ouvrance :

> « Les factures dont le montant est inférieur ou égal à 150 € hors taxe **ainsi que celles établies par les assujettis bénéficiant du régime de franchise en base prévu aux articles 293 B et 293 B ter du code général des impôts** […] **peuvent ne pas comporter les mentions énoncées aux 2° et 12° du I du présent article.** »

Le 2° (numéro individuel d'identification à la TVA) et le 12° (référence à la disposition d'exonération) tombent donc **deux fois** : par le montant (≤ 150 € HT — c'est le cas de toutes les Formules d'ouvrance) et par le régime (franchise en base).

### 3.2 [ADMIN] Quatre mentions nouvelles sont obligatoires depuis le 1er septembre 2026

[FAQ DGFiP « Je découvre la facturation électronique », version du 01/09/2026](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf), question **3.4**, verbatim :

> « Les mentions obligatoires prévues par le Code de commerce et le Code général des impôts restent identiques. **Quatre nouvelles mentions sont cependant rendues obligatoires à des fins de gestion des données.** Le décret n° 2022-1299 du 7 octobre 2022 […] modifie l'article 242 nonies A de l'annexe II au Code général des impôts pour rendre obligatoires ces nouvelles mentions **à compter du 1er septembre 2026**.
>
> Il s'agit des mentions suivantes :
> - **le SIREN du client** ;
> - **la catégorie de l'opération** : livraison de biens, prestation de service ou double […] ;
> - **l'option de paiement de la TVA sur les débits**, le cas échéant ;
> - **l'adresse de livraison des biens**, si elle est différente de l'adresse de facturation, le cas échéant. »

Ces quatre mentions correspondent aux 1° (partie « numéro d'identification » du client), 8° bis, 11° bis et 7° bis du texte cité en 3.1. **Deux d'entre elles sont inconditionnelles** : le SIREN du client et la catégorie de l'opération. La catégorie pour ouvrance est **PS** (prestation de services) ; le SIREN du client n'existe que si le client est une entreprise.

### 3.3 [ADMIN] La mention « TVA non applicable, article 293 B du CGI »

Ce n'est **pas** l'article 242 nonies A qui l'impose — le II l'en dispense même. C'est la doctrine, dans un document du BOFiP mis à jour **le 1er juillet 2026** : [BOI-TVA-DECLA-40-10-20](https://bofip.impots.gouv.fr/bofip/1079-PGP.html/identifiant=BOI-TVA-DECLA-40-10-20-20260701), « Franchise en base — Conséquences de la franchise », **§ 50**, verbatim :

> « **Les bénéficiaires de la franchise doivent indiquer sur les factures, la note d'honoraires ou sur tout autre document en tenant lieu, la mention : « TVA non applicable, article 293 B du CGI »** [ou « TVA non applicable, article 293 B bis du CGI » ou une référence à l'article 284 de la directive 2006/112/CE du Conseil du 28 novembre 2006 modifiée]. »

Deux points qui méritent d'être relevés :
- La mention est exigée **« sur tout autre document en tenant lieu »**. Une **note** au sens de l'arrêté de 1983 en tient lieu. La mention y est donc due aussi.
- C'est une exigence **[ADMIN]**, pas **[TEXTE]**. Elle est opposable en pratique (le BOFiP l'est) mais elle n'est pas dans la loi. **[ZONE GRISE]** : quelle sanction exactement frappe son omission ? Aucune source primaire consultée ne le dit. Les blogs qui annoncent un « redressement immédiat » ne citent aucun texte — ils ne valent rien ici.

### 3.4 [TEXTE] Le SIREN — d'où il vient exactement

Le 1° du 242 nonies A ne dit pas « SIREN » : il dit « **le numéro d'identification mentionné au premier alinéa de l'article R. 123-221 du code de commerce** ». C'est le renvoi qui fait le SIREN. Pour ouvrance : **980207898**.

Attention à ne pas confondre : le **SIREN** (9 chiffres, l'unité légale) est ce qu'exige le 1° et ce que la FAQ DGFiP appelle « SIREN du client » ; le **SIRET** (14 chiffres, l'établissement) n'est exigé nulle part par ce texte.

### 3.5 [TEXTE] Une facture peut-elle porter une adresse d'émetteur tronquée ?

C'est la question posée par le dossier : les mentions légales actuelles portent **« 93600 Aulnay-sous-Bois », sans nom de rue**, par choix délibéré (domicile personnel).

**Ce que le texte exige.** Le 1° du I de l'article 242 nonies A, verbatim : « Le nom complet, le numéro d'identification […] **et l'adresse** de l'assujetti et de son client ». Le texte dit « **l'adresse** », au singulier défini, sans autre qualification.

**Ce que la doctrine ajoute.** [BOI-TVA-DECLA-30-20-20-10](https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-10-20121231), « Mentions obligatoires générales », **§ 10** :

> Les factures doivent indiquer « le nom du vendeur ou du prestataire et celui du client (ou leur raison sociale) ainsi que **leurs adresses respectives (ou le lieu de leur siège social)** ».

Le BOFiP admet donc **le siège social** en lieu et place de l'adresse — mais un siège social est **une adresse complète**, pas une commune. La substitution porte sur *laquelle* des adresses de l'entreprise on porte, pas sur *combien* on en écrit.

**Deux autres textes exigent la même chose, indépendamment du CGI :**
- **La note** de l'arrêté de 1983, [article 3](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459003) : « le nom et **l'adresse du prestataire** ». Ce texte-là s'impose **dès aujourd'hui** à ouvrance, dès 25 € TTC — sans attendre la moindre facture.
- **Le site marchand** : [article 19 de la LCEN (loi n° 2004-575 du 21 juin 2004)](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032236011), qui impose « un accès facile, direct et permanent » notamment à **l'adresse où le professionnel est établi**. **Contradiction de sources à signaler** : plusieurs commentateurs annoncent l'abrogation de cet article au 1er septembre 2026 (transfert au Code de la consommation dans le cadre de l'adaptation au DSA). **Légifrance, source primaire, affiche au 7 septembre 2026 : « En vigueur du 01/07/2016 au 01/01/2027 ».** Légifrance prime : l'article est encore applicable aujourd'hui, avec une abrogation différée. **[ZONE GRISE]** — l'article de reprise dans le Code de la consommation n'a pas été identifié dans cette recherche ; l'obligation d'indiquer l'adresse d'établissement n'est pas supprimée, elle change de support.

**Une adresse de domiciliation ou une boîte postale est-elle admise ?** **[ZONE GRISE].** Aucune des sources consultées — ni l'article 242 nonies A, ni le BOFiP § 10, ni l'arrêté de 1983 — ne mentionne la boîte postale, la domiciliation commerciale ou la société de domiciliation. Le BOFiP § 20 (rescrit 2006/13) traite d'un cas voisin — facturer à l'adresse d'un établissement principal ou secondaire du **client** — et n'en dit rien pour l'émetteur. **Rien n'interdit** une adresse de domiciliation, qui est une adresse réelle et déclarée ; **rien ne l'autorise explicitement non plus** dans les textes lus. À faire trancher.

Ce qu'on peut dire sans zone grise : **une commune et un code postal ne sont pas « l'adresse ».** Une adresse sans voie ne permet ni de localiser l'établissement, ni de lui adresser un courrier, ni de vérifier quoi que ce soit — c'est précisément la fonction que le 1° et l'article 3 de l'arrêté lui donnent.

### 3.6 [TEXTE] L'entrepreneur individuel doit accoler « EI » à son nom

[Légifrance, art. L526-22 du Code de commerce](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049048964), premier alinéa, version en vigueur depuis le 28 janvier 2024 :

> « **L'entrepreneur individuel est une personne physique qui exerce en son nom propre une ou plusieurs activités professionnelles indépendantes.** »

L'obligation de dénomination est au niveau réglementaire. [Légifrance, art. R526-27 du Code de commerce](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045697814), créé par le **décret n° 2022-725 du 28 avril 2022, art. 2**, en vigueur depuis le 15 mai 2022, verbatim et intégralement :

> « Pour l'exercice de l'activité professionnelle mentionnée au premier alinéa de l'article L. 526-22, et sans préjudice des articles D. 123-235 et D. 123-236, **l'entrepreneur individuel utilise une dénomination incorporant son nom ou nom d'usage précédé ou suivi immédiatement des mots : « entrepreneur individuel » ou des initiales : « EI ».**
>
> **La dénomination figure sur les documents et correspondances à usage professionnel de l'intéressé.**
>
> Chaque compte bancaire dédié à son activité professionnelle ouvert par l'entrepreneur individuel doit contenir la dénomination dans son intitulé.
>
> Au sens et pour l'application de l'article L. 526-23, à défaut d'immatriculation, la première utilisation de la dénomination vaut date déclarée de début d'activité pour identifier le premier acte exercé en qualité d'entrepreneur individuel. »

Trois choses se lisent dans la lettre :
- La mention accompagne **le nom de la personne physique**, pas le nom commercial. « ouvrance » seul ne satisfait pas le texte ; « EI Fayssal BENOUDA » ou « Fayssal BENOUDA EI » le satisfait. Un nom commercial peut s'y ajouter (« sans préjudice des articles D. 123-235 et D. 123-236 »), il ne peut pas s'y substituer.
- Le champ est « **les documents et correspondances à usage professionnel** » — donc les factures **et** les notes, sans distinction.
- Elle s'applique **aussi à l'intitulé du compte bancaire dédié**.

### 3.7 La facture minimale d'ouvrance, mention par mention

| Mention | Source | Due ? | Valeur pour ouvrance |
| --- | --- | --- | --- |
| Nom complet de l'émetteur + « EI » | 242 nonies A 1° ; R526-27 | **Oui** | « Fayssal BENOUDA EI » (+ nom commercial ouvrance) |
| Numéro d'identification (SIREN) | 242 nonies A 1° (renvoi R. 123-221) | **Oui** | 980207898 |
| **Adresse de l'émetteur** | 242 nonies A 1° ; arrêté art. 3 | **Oui** | **Adresse complète — voir 3.5** |
| Nom et adresse du client | 242 nonies A 1° | **Oui** | Nom de l'Offrant (« sauf opposition » sur la note, art. 3) |
| SIREN du client | 242 nonies A 1° depuis le 01/09/2026 | Si le client est une entreprise | — |
| Date d'émission | 242 nonies A 6° | **Oui** | — |
| Numéro unique, séquence chronologique continue | 242 nonies A 7° | **Oui** | Voir section 4 |
| Catégorie de l'opération (LB / PS / LBPS) | 242 nonies A 8° bis depuis le 01/09/2026 | **Oui** | **PS** |
| Quantité, dénomination précise, prix unitaire HT | 242 nonies A 8° ; arrêté art. 3 | **Oui** | Formule + chaque Supplément, ligne par ligne |
| Date d'exécution si ≠ date d'émission | 242 nonies A 10° ; arrêté art. 3 | **Oui** si différente | Date de Livraison |
| Total HT **et** TTC | Arrêté art. 3 | **Oui** (sur la note) | Identiques en franchise en base |
| N° de TVA intracommunautaire | 242 nonies A 2° | **Non** | Dispensé par le II (≤ 150 € HT **et** franchise en base) |
| Référence à l'exonération | 242 nonies A 12° | **Non** | Dispensé par le II |
| « TVA non applicable, article 293 B du CGI » | BOI-TVA-DECLA-40-10-20 § 50 | **Oui** [ADMIN] | Sur la facture **et** sur la note |
| Option TVA sur les débits | 242 nonies A 11° bis | **Non** | Pas d'option — franchise en base |
| Adresse de livraison des biens | 242 nonies A 7° bis | **Non** | Prestation de services, pas de bien livré |
| Autoliquidation / Autofacturation / régimes particuliers | 242 nonies A 13° à 18° | **Non** | Aucun applicable |
| Pénalités de retard, escompte, indemnité 40 € | L441-9 | **Non** | Régime B2B, hors champ (voir 1.3) |

> **Conclusion de la section 3 — ce que ça change pour ouvrance.**
>
> - Une facture ouvrance conforme tient en **onze mentions**, pas dix-huit : la franchise en base et le montant sous 150 € HT en retirent deux, la nature de l'opération en retire six.
> - **Deux mentions manquent aujourd'hui et manquent partout** : la dénomination « EI » accolée au nom de l'auteur (art. R526-27), et la mention « TVA non applicable, article 293 B du CGI » (BOFiP § 50). Elles sont dues sur les factures **comme sur les notes**.
> - **Sur l'adresse, il faut le dire sans détour : « 93600 Aulnay-sous-Bois » ne tient pas.** Trois textes indépendants exigent « l'adresse » du prestataire — le 1° du 242 nonies A pour la facture, l'article 3 de l'arrêté de 1983 pour la note, l'article 19 de la LCEN pour le site — et aucun ne connaît d'adresse partielle. Le BOFiP § 10 admet de substituer *le siège social* à l'adresse, pas une commune à une adresse.
> - **Ce choix a survécu tant qu'aucune facture n'était émise ; il ne survivra pas à la première note obligatoire — c'est-à-dire à la première vente de jeu premium à 69,99 €.** Et il est déjà en tension aujourd'hui sur les mentions légales du site.
> - Ce document **ne choisit pas la solution**. Il constate qu'il en faut une, et que le champ des solutions sourcées est étroit : porter l'adresse réelle, ou obtenir une adresse d'établissement distincte (domiciliation) — dont l'admissibilité en tant que telle est **[ZONE GRISE]** et doit être confirmée par un expert-comptable.

---

## 4. La numérotation

### 4.1 [TEXTE] L'obligation est autonome et elle est dans le décret

Elle ne se déduit d'aucun principe comptable général : elle est écrite, au **7° du I de l'article 242 nonies A de l'annexe II au CGI** (déjà cité en 3.1), verbatim :

> « **Un numéro unique basé sur une séquence chronologique et continue ; la numérotation peut être établie dans ces conditions par séries distinctes lorsque les conditions d'exercice de l'activité de l'assujetti le justifient ; l'assujetti doit faire des séries distinctes un usage conforme à leur justification initiale ;** »

Trois exigences distinctes dans une seule phrase : **unique**, **chronologique**, **continue**. Et une faculté encadrée : les **séries distinctes**.

### 4.2 [ADMIN] Ce que le BOFiP en fait

[BOI-TVA-DECLA-30-20-20-10](https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-10-20121231), « TVA — Règles relatives à l'établissement des factures — Mentions à porter sur les factures — Mentions obligatoires générales », publié le 31/12/2012 :

- **§ 70** : la facture doit porter « un numéro unique basé sur une séquence chronologique et continue ».
- **§ 80** : des séries distinctes peuvent être établies « lorsque les conditions d'exercice de l'activité de l'assujetti le justifient », à condition d'en faire « un usage conforme à leur justification initiale ».
- **§ 90** : pour **chaque série distincte**, la numérotation doit être chronologique à l'émission, continue, et faite de telle sorte que **deux factures émises la même année ne puissent pas porter le même numéro**. L'emploi d'un **préfixe distinct par série** est recommandé.
- **§ 100** : sont des justifications admises de séries distinctes — **plusieurs sites de facturation**, **des catégories de clients soumises à des règles différentes**, **des modes d'émission différents** (facture électronique, papier, autofacturation).
- **§ 110** : la seule pluralité de lieux d'établissement de clients dans des États différents **ne justifie pas** de créer une série par client ou par destination.
- **§ 120-130** : lorsqu'un tiers établit matériellement les factures pour le compte de l'assujetti, la séquence doit rester chronologique, continue et **propre à cet assujetti** — jamais mêlée à la propre facturation du mandataire.

**Réponse à « peut-on avoir plusieurs séries en parallèle ? »** — **Oui**, mais pas librement : il faut une **justification tirée des conditions d'exercice de l'activité**, et l'usage doit rester conforme à cette justification. Le § 100 donne la liste des justifications que l'administration admet. « Une série par Formule » ou « une série par canal de vente » n'y figure pas telle quelle ; « des modes d'émission différents » (papier / électronique / autofacturation) y figure — ce qui deviendra pertinent au moment du passage à la facture électronique (section 5).

### 4.3 Le point décisif : à quel moment le numéro est-il attribué ?

**Au moment où la facture est émise, et une facture n'est émise que quand l'opération est réalisée.** Deux sources concordantes :

**[TEXTE]** — [art. 289 I-3 du CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413), premier alinéa :

> « **La facture est, en principe, émise dès la réalisation de la livraison ou de la prestation de services.** »

**[ADMIN]** — [FAQ DGFiP, version du 01/09/2026](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf), question **3.5**, verbatim :

> « Les modalités de facturation restent identiques : les factures doivent, en principe, être émises **dès la réalisation de la livraison de biens ou de la prestation de services** (article 289-I.3 alinéa 1 du CGI). **La facture doit être émise dès la réalisation du fait générateur retenu pour l'opération en matière de TVA.** »

Le rattachement est donc **au fait générateur**, pas à la naissance de la Commande, ni au clic sur « payer ».

**Ce que cela donne, appliqué au vocabulaire d'ouvrance :**

| Événement | Une facture est-elle émise ? | Un numéro est-il consommé ? |
| --- | --- | --- |
| **Commande** créée (formulaire rempli, rien payé) | Non — aucune prestation réalisée, aucun acompte versé | **Non** |
| Commande **abandonnée**, purgée à 24 h | Non | **Non** |
| **Paiement** encaissé (Stripe) | Le c du 1 du I de l'art. 289 impose une facture pour les acomptes **uniquement dans les cas des a et b** — non applicable à un client particulier | **Non** au titre du CGI. Une **note** peut être due (section 1) |
| **Livraison** du lien (prestation rendue) | C'est le moment que désigne l'art. 289 I-3 | **Oui**, si facture il y a |

**Réponse directe à la question du ticket : une Commande abandonnée ne consomme pas de numéro, et le numéro n'a pas à être attribué au moment de la Commande.** Aucun texte ne rattache le numéro à l'objet métier « Commande » ; l'article 289 I-3 le rattache à l'émission de la facture, et l'émission au fait générateur.

### 4.4 [ZONE GRISE] Ce que personne ne tranche : le trou dans la séquence

Le 7° exige une séquence « **continue** ». Ce qu'il faut faire lorsqu'un numéro a été attribué puis abandonné (facture annulée, brouillon avorté) **n'est traité par aucune source primaire ni par le BOFiP** dans les documents consultés.

La pratique largement diffusée — émettre un avoir portant ce numéro, ou consigner dans un document daté la cause de la discontinuité et les numéros manquants — **ne provient que de blogs de logiciels de facturation**. Aucun d'eux ne cite de texte. **Cela ne vaut rien ici.** À faire trancher par un expert-comptable.

Ce qui est en revanche **sourcé** : le § 90 interdit que **deux factures de la même année portent le même numéro**. La réutilisation d'un numéro abandonné est donc dangereuse si une facture a déjà porté ce numéro, même annulée.

> **Conclusion de la section 4 — ce que ça change pour ouvrance.**
>
> - **Oui, la numérotation continue et chronologique est une obligation autonome**, écrite au 7° du I de l'article 242 nonies A, et non un usage comptable.
> - **Oui, plusieurs séries sont possibles** — mais seulement pour une des raisons que le BOFiP § 100 admet, et avec un préfixe distinct (§ 90).
> - **Non, une Commande ne doit pas consommer un numéro.** Le numéro appartient à la facture, la facture au fait générateur, et le fait générateur à la Livraison. Une Commande abandonnée à 24 h n'a jamais approché le seuil d'émission.
> - **Ce que cela ne dit pas** : ce document n'indique pas où le compteur doit vivre ni comment il doit être alloué. Ce sont des décisions de conception, hors du périmètre de cette recherche.
> - Le point à surveiller, une fois le compteur en place : **ne pas laisser un numéro être attribué avant que la facture ne soit certaine**, faute de quoi on entre dans la zone grise du § 4.4.

---

## 5. La réforme de la facturation électronique — état au 7 septembre 2026

C'est le point le plus daté du dossier. **Le premier palier est déjà passé : il est tombé le 1er septembre 2026, il y a six jours.**

### 5.1 [TEXTE] Les deux articles qui portent la réforme

**Facturation électronique** — [art. 289 bis du CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546660), version en vigueur depuis le **21 février 2026** (loi n° 2026-103 du 19 février 2026, art. 123). Son I pose l'obligation d'émettre, transmettre et recevoir les factures **par l'intermédiaire d'une plateforme agréée**, pour les opérations **entre assujettis établis en France**. Son III institue un **annuaire central** mis à la disposition des plateformes pour l'adressage des factures.

**E-reporting** — [art. 290 du CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046195617), version en vigueur depuis le **21 février 2026**. Son I impose aux assujettis établis en France de transmettre à l'administration, sous forme électronique et **via une plateforme agréée**, les données des opérations **réalisées auprès de personnes non assujetties** et des opérations avec l'étranger.

**Le calendrier** est à l'[article 91 de la loi n° 2023-1322 du 29 décembre 2023 de finances pour 2024](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000048727444), verbatim :

> « Les 2° et 4° du I et le II **s'appliquent aux factures émises à compter du 1er septembre 2026** » — et, pour les PME et microentreprises non membres d'un assujetti unique : « les 2° et 4° du I et le II du présent article **s'appliquent à compter du 1er septembre 2027** ».
>
> « les 3° et 5° du I du présent article s'appliquent aux factures émises ou, à défaut, **aux opérations réalisées à compter du 1er septembre 2026** » — et « les mêmes 3° et 5° **ne s'appliquent qu'à compter du 1er septembre 2027** aux factures émises par les entreprises mentionnées au deuxième alinéa ».

**Terminologie**, à connaître pour ne pas se tromper de vocabulaire : l'[arrêté du 27 juillet 2026 relatif à la généralisation de la facturation électronique](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054499535), entré en vigueur le 29 juillet 2026, **remplace « opérateur de plateforme de dématérialisation partenaire » (PDP) par « plateforme agréée » (PA)** dans les articles 41 septies A et suivants de l'annexe IV au CGI. **« PDP » est l'ancien terme ; « PA » est le terme en vigueur.**

### 5.2 [ADMIN] Le calendrier, tel que la DGFiP l'énonce au 1er septembre 2026

[FAQ DGFiP « Je découvre la facturation électronique », version du 01/09/2026](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf), question **5.1**, verbatim :

> « **Depuis le 1er septembre 2026, toutes les entreprises, quelles que soient leur taille et leur forme juridique, ont l'obligation de recevoir des factures sous format électronique, par l'intermédiaire d'une plateforme agréée** […]. Les grandes entreprises (GE) et les entreprises de taille intermédiaire (ETI) doivent également émettre toutes leurs factures sous format électronique. **Les petites, moyennes et micro-entreprises seront, quant à elles tenues, d'émettre leurs factures au format électronique au plus tard le 1er septembre 2027.** »

Question **8.1**, verbatim :

> « La mise en place de la transmission des données de transaction (e-reporting) suit celle de la facturation électronique : **depuis le 1er septembre 2026 pour les grandes entreprises et pour les établissements de taille intermédiaire, et à partir du 1er septembre 2027 pour les micro, petites et moyennes entreprises.** »

Question **1.2**, verbatim — et c'est le passage qui vise directement le cas d'ouvrance :

> « […] **même si un assujetti réalise exclusivement des opérations n'entrant pas dans le champ du dispositif, il doit être en capacité de recevoir les factures électroniques qui lui seront adressées par ses fournisseurs assujettis et de choisir une plateforme agréée à cet effet. Cette obligation court depuis le 1er septembre 2026** […]. Par exemple, un médecin généraliste ou un ostéopathe doit avoir choisi une plateforme agréée, dès le 1er septembre 2026, afin de recevoir les factures de ses fournisseurs d'énergie ou d'accès internet […]. »

Question **1.1**, verbatim — la règle de tri entre les deux régimes :

> « Il convient tout d'abord de regarder la qualité de votre client.
> - **Si votre client est un particulier ou une personne morale non assujettie, qu'il soit en France ou à l'étranger, alors vous devez transmettre à l'administration des données concernant ces opérations dans le cadre du e-reporting** (I de l'article 290 du CGI).
> - Si votre client est un professionnel […] pour les opérations avec des clients établis sur le territoire français, alors vous devez émettre une facture électronique (article 289 bis du CGI). »

Question **2.1**, verbatim — le choix de la plateforme :

> « **Le choix de la plateforme est totalement libre et relève d'une décision de gestion du chef d'entreprise ; une entreprise peut choisir une ou plusieurs plateforme(s) agréée(s). Chaque entreprise doit signer un accord formel avec la ou les plateforme(s) agréée(s) choisie(s) désignée(s) pour la réception de ses factures électroniques dans l'annuaire de destinataires de factures géré par l'administration.** Un changement de plateforme agréée est possible, à tout moment. »

Question **2.2**, verbatim :

> « **L'obligation de réception des factures au format électronique étant généralisée dès le 1er septembre 2026 pour toutes les entreprises, quelle que soit leur taille et quelle que soit leur forme juridique, vous devez avoir choisir une plateforme agréée, au moins pour recevoir les factures de vos fournisseurs concernés par l'obligation d'émission à cette date.** »

Question **9.3**, verbatim — et **c'est la source qui règle la question de la franchise en base** :

> « Les données de transaction ne sont pas à transmettre au fil de l'eau comme les factures électroniques ou les données de facture. La fréquence de transmission est définie par le régime d'imposition de l'entreprise à la TVA. **Par exemple, si vous êtes franchisé en base, vous les transmettrez tous les deux mois.** »

Question **9.2**, verbatim :

> « L'administration attend les données des opérations que vous réalisez ; les plateformes agréées pourront proposer des services complémentaires facilitant la transmission des données de transaction. **Il ne sera donc pas forcément nécessaire pour l'entreprise d'acquérir un logiciel de facturation ou tout autre équipement spécifique.** »

Enfin, [le tableau officiel des données de transaction B2C à transmettre, mis à jour août 2026](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/japprof_donnees-de-transactions-a-transmettre_vf.pdf), précise ce que le e-reporting B2C attend, et ce n'est **pas** la facture :

> Données « à transmettre **de façon agrégée par jour** » : la date du jour et, pour chaque catégorie de transactions (livraisons de biens soumises à la TVA, **prestations de services soumises à la TVA**, opérations intracommunautaires, TVA sur la marge) : « **la base d'imposition totale HT des opérations de la journée** » et « **le montant de TVA correspondante** », par taux si plusieurs taux s'appliquent. Plus, en en-tête : le **SIREN du redevable du e-reporting** et la **période** de la transmission.

### 5.3 Les cinq réponses demandées

| Question | Réponse | Source |
| --- | --- | --- |
| **(a) Quand une micro-entreprise doit-elle pouvoir *recevoir* une facture électronique ?** | **Depuis le 1er septembre 2026** — donc **c'est déjà exigible**. Toutes les entreprises, quelles que soient leur taille et leur forme juridique. Cela suppose d'**avoir choisi une plateforme agréée** et d'y être inscrit dans l'annuaire | FAQ 5.1, 1.2, 2.2 ; art. 91 LF 2024 |
| **(b) Quand doit-elle *émettre* en électronique ?** | **1er septembre 2027** au plus tard. Entrée volontaire anticipée possible | FAQ 5.1, 1.3 ; art. 91 LF 2024 |
| **(c) Les ventes B2C sont-elles concernées par la facturation électronique ?** | **Non.** La facturation électronique de l'art. 289 bis vise les opérations **entre assujettis établis en France**. Les ventes à un particulier relèvent **uniquement de l'e-reporting** (art. 290 I) | FAQ 1.1 ; art. 289 bis, 290 CGI |
| **(d) Un assujetti en franchise en base est-il dans le champ de l'e-reporting B2C, et à quelle date ?** | **Oui.** La franchise en base est une dispense de déclaration et de paiement, pas une sortie de la qualité d'assujetti ; la FAQ prévoit explicitement une **fréquence de transmission propre aux franchisés en base : tous les deux mois**. **Date : 1er septembre 2027** (micro-entreprise) | FAQ 7.1, 8.1, **9.3** |
| **(e) Qu'est-ce qu'une PA / PDP, et faut-il en choisir une ?** | Une **plateforme agréée (PA)** — anciennement « PDP » — est l'intermédiaire obligatoire qui émet, transmet et reçoit les factures électroniques et transmet les données de e-reporting à l'administration. **Oui, il faut en choisir une** : le choix est libre (une ou plusieurs, changeable à tout moment) mais **pas facultatif**, et il suppose un **accord formel** signé et une inscription à l'annuaire. La liste officielle est publiée sur impots.gouv.fr | Arrêté du 27/07/2026 ; art. 289 bis I ; FAQ 2.1, 2.2, 2.3 |

### 5.4 [ADMIN] La tolérance de démarrage — ce qu'elle est et ce qu'elle n'est pas

[Guide pratique de démarrage au 1er septembre 2026, impots.gouv.fr](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf), verbatim :

> « **Il est précisé que pendant la phase de démarrage, il n'y aura pas d'application des sanctions aux entreprises rencontrant des difficultés dans la mise en œuvre de la réforme mais qui sont engagées dans une trajectoire sérieuse de mise en conformité.** L'administration distinguera ces situations de celles relevant d'une inertie, d'un évitement ou d'un refus durable d'entrer dans le dispositif. Elle tiendra compte des difficultés réelles, documentées et suivies d'actions de correction. **Cette approche ne constitue ni un report ni une suspension de l'obligation.** »

Et sur la réception, verbatim :

> « L'entreprise qui n'a pas encore désigné de plateforme doit donc **engager cette démarche sans attendre** […]. Cette situation ne doit pas conduire l'entreprise à interrompre son activité […]. **En revanche, elle doit être corrigée rapidement. L'entreprise doit pouvoir démontrer qu'elle a engagé les démarches nécessaires** […]. »

> **Conclusion de la section 5 — ce que ça change pour ouvrance.**
>
> - **Une échéance est déjà dépassée.** Depuis le 1er septembre 2026, ouvrance doit **avoir choisi une plateforme agréée pour recevoir** les factures électroniques de ses propres fournisseurs. Ce n'est pas conditionné à ce qu'ouvrance facture quoi que ce soit : la FAQ 1.2 le dit d'un praticien qui ne fait aucune opération dans le champ. La tolérance de démarrage couvre « une trajectoire sérieuse », pas l'absence de démarche.
> - **La vente aux Offrants ne relèvera jamais de la facturation électronique** tant que les Offrants sont des particuliers. Le B2C, c'est de l'**e-reporting** : des **totaux journaliers agrégés HT et TVA**, pas des factures.
> - **La franchise en base ne dispense de rien.** Elle fixe seulement une **fréquence de transmission bimestrielle**.
> - **Deux dates au 1er septembre 2027**, la même : l'obligation d'**émettre** en électronique (le jour où un client sera professionnel) et l'obligation d'**e-reporting B2C**. Il reste **moins de douze mois**.
> - **Ce que cela ne dit pas** : quelle plateforme, ni comment la brancher. Décisions de conception, hors périmètre.

---

## 6. La conservation

### 6.1 [TEXTE] Dix ans au titre du Code de commerce

[Légifrance, art. L123-22 du Code de commerce](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006219327), version en vigueur depuis le 4 janvier 2003, verbatim et intégralement :

> « **Les documents comptables sont établis en euros et en langue française.**
>
> **Les documents comptables et les pièces justificatives sont conservés pendant dix ans.**
>
> **Les documents comptables relatifs à l'enregistrement des opérations et à l'inventaire sont établis et tenus sans blanc ni altération d'aucune sorte, dans des conditions fixées par décret en Conseil d'Etat.** »

Le troisième alinéa est celui qu'on oublie, et c'est celui qui compte pour un système informatique : **« sans blanc ni altération d'aucune sorte »**.

### 6.2 [TEXTE] Six ans au titre du LPF — et dix ans à compter du 1er janvier 2027

[Légifrance, art. L102 B du Livre des procédures fiscales](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041471233), **version en vigueur du 1er janvier 2023 au 1er janvier 2027**, I, verbatim alinéa par alinéa :

> « **Alinéa 1** — Les livres, registres, documents ou pièces sur lesquels peuvent s'exercer les droits de communication, d'enquête et de contrôle de l'administration **doivent être conservés pendant un délai de six ans à compter de la date de la dernière opération mentionnée sur les livres ou registres ou de la date à laquelle les documents ou pièces ont été établis.**
>
> **Alinéa 2** — **Lorsqu'ils sont établis ou reçus sur support informatique, ces livres, registres, documents ou pièces doivent être conservés sous cette forme pendant le délai prévu au premier alinéa du présent I.**
>
> **Alinéa 3** — Sans préjudice du premier alinéa du présent I, lorsque les documents et pièces sont établis ou reçus **sur support papier**, ils peuvent être conservés sur support informatique ou sur support papier, pendant une durée égale au délai prévu au même premier alinéa. **Les modalités de numérisation des factures papier sont fixées par arrêté du ministre chargé du budget.**
>
> **Alinéa 4** — Les pièces justificatives relatives à des opérations ouvrant droit à une déduction en matière de taxes sur le chiffre d'affaires sont conservées pendant le délai prévu au premier alinéa. »

**Point de vigilance daté.** Légifrance publie une **version de l'article L102 B entrant en vigueur le 1er janvier 2027**, dont le I, premier alinéa, porte le délai à **dix ans** : [LEGIARTI000053189496](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053189496/2029-01-01), verbatim :

> « Les livres, registres, documents ou pièces sur lesquels peuvent s'exercer les droits de communication, d'enquête et de contrôle de l'administration **sont conservés pendant un délai de dix ans** à compter de la date de la dernière opération mentionnée sur les livres ou registres ou de la date à laquelle les documents ou pièces ont été établis. »

**Le délai fiscal et le délai commercial s'alignent donc à dix ans au 1er janvier 2027.** D'ici là, la règle prudente est déjà dix ans : c'est le plus long des deux, et le Code de commerce l'impose depuis 2003.

**À partir de quand court le délai ?** Le texte le dit : « **à compter de la date de la dernière opération mentionnée sur les livres ou registres ou de la date à laquelle les documents ou pièces ont été établis** ». Pour une facture ouvrance : **à compter de sa date d'émission**, pas de la clôture de l'exercice.

### 6.3 [ADMIN] Ce que le BOFiP en tire pour les factures

[BOI-CF-COM-10-10-30](https://bofip.impots.gouv.fr/bofip/645-PGP.html/identifiant=BOI-CF-COM-10-10-30-20250903), « Conservation des documents », version du **3 septembre 2025** :

- **§ 10** : les factures papier ou électroniques doivent être conservées **six ans**, conformément à l'article L102 B du LPF, le délai courant « à compter de la date de la dernière opération mentionnée sur les livres ou registres ou de la date à laquelle les documents ou pièces ont été établis ».
- **§ 160** : les factures transmises par voie électronique « **doivent être conservées sur support informatique** pendant un délai de six ans ».
- **§ 200** : « **l'authenticité de l'origine, l'intégrité du contenu et la lisibilité** doivent être garanties **à compter de leur émission et jusqu'à la fin de leur période de conservation** ».
- **§ 300** : pour les factures sécurisées par une **piste d'audit fiable**, « le contenu des factures **et des éléments constitutifs des contrôles** ne doit pas être modifié pendant toute la durée de leur conservation ».

Le § 300 est celui qu'on sous-estime : ce ne sont pas seulement les factures qu'il faut figer, ce sont **les preuves des contrôles** qui établissent la piste d'audit.

### 6.4 [TEXTE] Une facture native électronique doit être conservée sous forme électronique

**Oui, et la règle est dans la loi, pas dans la doctrine.** C'est l'**alinéa 2 du I de l'article L102 B du LPF** cité en 6.2 : « **Lorsqu'ils sont établis ou reçus sur support informatique, ces […] documents ou pièces doivent être conservés sous cette forme** ». Une facture née en PDF ou en XML **ne peut pas** être conservée uniquement sous forme imprimée.

L'inverse est permis, et encadré : l'alinéa 3 autorise la numérisation d'un document **né papier**, selon des modalités fixées par arrêté. Cet arrêté est l'[article A102 B-1 du LPF](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031960071/2026-03-03) (arrêté du 22 mars 2017), verbatim et intégralement :

> « **I.** – Le transfert des documents mentionnés au I bis de l'article L. 102 B établis originairement sur support papier vers un support informatique est réalisé **dans des conditions garantissant leur reproduction à l'identique**. Le résultat de cette numérisation est **la copie conforme à l'original en image et en contenu**. Les couleurs sont reproduites à l'identique, notamment en cas de mise en place d'un code couleur.
>
> **Le document ainsi numérisé est conservé sous format PDF (Portable Document Format) assorti d'une signature électronique conforme, au moins, au référentiel général de sécurité (RGS) de niveau une étoile.**
>
> Le document numérisé n'est retenu comme pièce constitutive **des contrôles mentionnés au 1° du VII de l'article 289 du code général des impôts** que s'il fait apparaître tout ajout, remarque ou information qui aurait été annoté sur le document papier.
>
> En cas de modification ou de correction des données portées sur un document numérisé, **seul le document corrigé et numérisé à nouveau** est retenu comme pièce constitutive des contrôles précités.
>
> **II.** – Le I est applicable à la documentation décrivant les modalités de réalisation des contrôles mentionnés au 1° du VII de l'article 289 du code général des impôts. »

**Attention au champ.** L'article A102 B-1 régit la **numérisation d'un document papier**, pas la conservation d'une facture native électronique. Il est souvent cité à contresens. Ce qu'il apporte tout de même : le **niveau d'exigence** que l'administration attache à la valeur probante — copie conforme, format PDF, signature électronique RGS une étoile, traçabilité des corrections.

### 6.5 [TEXTE] Les quatre voies de sécurisation, et le sens de « piste d'audit fiable »

[Art. 289 V et VII du CGI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413), verbatim :

> « **V.** – **L'authenticité de l'origine, l'intégrité du contenu et la lisibilité de la facture doivent être assurées à compter de son émission et jusqu'à la fin de sa période de conservation.**
>
> **VII.** – Pour satisfaire aux conditions prévues au V, l'assujetti peut émettre ou recevoir des factures :
>
> **1°** Soit sous forme électronique en recourant à toute solution technique autre que celles prévues aux 2°, 3° et 4°, ou sous forme papier, **dès lors que des contrôles documentés et permanents sont mis en place par l'entreprise et permettent d'établir une piste d'audit fiable entre la facture émise ou reçue et la livraison de biens ou prestation de services qui en est le fondement** ;
>
> **2°** Soit en recourant à la procédure de **signature électronique qualifiée** au sens du règlement (UE) n° 910/2014 […] ;
>
> **3°** Soit sous la forme d'un **message structuré selon une norme convenue entre les parties**, permettant une lecture par ordinateur et pouvant être traité automatiquement et de manière univoque […] ;
>
> **4°** Soit en recourant à la procédure de **cachet électronique qualifié** au sens du règlement (UE) n° 910/2014 […]. »

Quatre voies, au choix. La 1° — la piste d'audit fiable — est celle de la petite entreprise sans signature ni cachet qualifiés, mais elle a un prix : des **contrôles documentés et permanents**, dont la documentation elle-même doit être conservée et figée (§ 300 du BOFiP, art. A102 B-1 II).

### 6.6 Ce qui rendrait un simple enregistrement en base de données non conforme

Ce paragraphe **rapproche** des exigences sourcées ci-dessus. Il ne prescrit aucune architecture.

| Exigence sourcée | Où | Ce qu'un stockage en base ne satisfait pas de lui-même |
| --- | --- | --- |
| Conserver **sous forme électronique** ce qui est né électronique | L102 B I al. 2 | Satisfait — c'est le seul point qui l'est nativement |
| **Intégrité du contenu** garantie de l'émission jusqu'à la fin de la conservation | 289 V ; BOFiP § 200 | Une ligne SQL est **modifiable et supprimable** par construction. `UPDATE` ne laisse pas de trace |
| **Lisibilité** garantie pendant toute la durée | 289 V ; BOFiP § 200 | Des colonnes disséminées ne sont pas un document lisible ; il faut pouvoir **restituer la facture telle qu'émise**, dix ans plus tard, sans dépendre du code applicatif de l'époque |
| **Authenticité de l'origine** | 289 V | Rien dans une base ne l'établit sans l'une des quatre voies du VII |
| **Piste d'audit fiable** : contrôles **documentés et permanents** reliant la facture à la prestation | 289 VII 1° | Exige des contrôles écrits et exécutés, pas seulement des données. **La documentation des contrôles doit elle-même être conservée et non modifiée** (BOFiP § 300 ; A102 B-1 II) |
| **« Sans blanc ni altération d'aucune sorte »** | L123-22 al. 3 | Une purge, une migration de schéma destructrice ou une correction en place sont des altérations |
| **Dix ans** (six ans fiscal jusqu'au 31/12/2026) à compter de la date d'établissement | L123-22 al. 2 ; L102 B I al. 1 | Une base de production suit le cycle de vie de l'application, pas un calendrier de dix ans |

> **Conclusion de la section 6 — ce que ça change pour ouvrance.**
>
> - **Dix ans, à compter de la date d'émission de chaque facture ou note**, pas de la clôture de l'exercice. Le Code de commerce l'impose déjà (L123-22) ; le LPF s'y aligne au **1er janvier 2027**.
> - **Les notes** de l'arrêté de 1983 ont leur propre délai — **deux ans** (art. 6) — mais si elles servent de pièce justificative comptable, le délai de dix ans de L123-22 les rattrape. **[ZONE GRISE]** : aucune source consultée n'articule les deux délais.
> - **Une facture née électronique reste électronique** (L102 B I al. 2). Imprimer et jeter le fichier est non conforme.
> - **Ce n'est pas le stockage qui pose problème, c'est la mutabilité.** Les textes exigent l'intégrité, la lisibilité et l'authenticité pendant dix ans, plus des contrôles documentés et figés. Aucune source ne dit « base de données interdite » ; toutes disent « le contenu ne doit pas pouvoir être modifié ».
> - **Ce que ce document ne tranche pas** : comment obtenir cette immutabilité. C'est une décision de conception.

---

## Ce que ça impose à ouvrance

### Obligatoire aujourd'hui, et non fait

1. **Délivrer une note pour toute prestation ≥ 25 € TTC** — donc **toute vente de jeu premium (69,99 €)** et **toute carte animée à partir du 6ᵉ Supplément (26,99 €)**. Sans demande du client, avant paiement du prix. Mentions de l'[art. 3 de l'arrêté 83-50/A](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459003). Double exemplaire, conservation deux ans.
2. **Délivrer une note sur simple demande** pour toute prestation < 25 € TTC ([art. 1er](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032459194)).
3. **Fournir la confirmation du contrat sur support durable**, avec **toutes les informations de L221-5 et le formulaire type de rétractation**, au plus tard **avant le début de l'exécution** ([L221-13](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563210)). Aucun seuil. **Le reçu Stripe ne le fait pas.**
4. **Recueillir la demande expresse d'exécution anticipée** et la **reconnaissance de la perte du droit de rétractation**, et en fournir confirmation ([L221-25](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000044563179), [L221-26](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563174)). À défaut, **le consommateur ne doit aucune somme**.
5. **Porter la mention « TVA non applicable, article 293 B du CGI »** sur toute facture, note ou document en tenant lieu ([BOI-TVA-DECLA-40-10-20 § 50, 01/07/2026](https://bofip.impots.gouv.fr/bofip/1079-PGP.html/identifiant=BOI-TVA-DECLA-40-10-20-20260701)).
6. **Porter « EI » ou « entrepreneur individuel » accolé au nom de l'auteur** sur tous les documents professionnels, et dans l'intitulé du compte bancaire dédié ([R526-27](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045697814)).
7. **Porter une adresse complète.** « 93600 Aulnay-sous-Bois » ne satisfait ni le 1° du 242 nonies A, ni l'art. 3 de l'arrêté de 1983, ni l'art. 19 de la LCEN. **Voir 3.5 : c'est la conséquence la plus personnelle de ce document, et elle est due dès la première note obligatoire.**
8. **Avoir choisi une plateforme agréée pour *recevoir* les factures électroniques.** Échéance : **1er septembre 2026 — passée depuis six jours** ([FAQ DGFiP 1.2, 2.2, 5.1](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf)). Sanctions suspendues pour qui démontre une trajectoire sérieuse, **mais l'obligation n'est ni reportée ni suspendue**.
9. **Conserver dix ans** documents comptables et pièces justificatives, à compter de leur établissement ([L123-22](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006219327)), sous forme électronique pour ce qui est né électronique ([L102 B I al. 2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041471233)), avec intégrité, lisibilité et authenticité garanties ([289 V](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413)).

### Pas obligatoire

- **La facture au sens de l'article 289 du CGI**, tant que les Offrants sont des particuliers ([BOI-TVA-DECLA-30-20-10-10 § 20](https://bofip.impots.gouv.fr/bofip/13242-PGP.html/identifiant=BOI-TVA-DECLA-30-20-10-10-20211222)).
- **Les mentions de l'article L441-9 du Code de commerce** (pénalités de retard, escompte, indemnité forfaitaire de 40 €) : régime B2B.
- **Le n° de TVA intracommunautaire (2°) et la référence à l'exonération (12°)** : dispensés deux fois par le II du 242 nonies A.
- **La facturation électronique des ventes aux Offrants** : le B2C n'y est pas, jamais. C'est l'e-reporting.
- **Attribuer un numéro de facture à une Commande.** Le numéro appartient à la facture, la facture au fait générateur ([289 I-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413) ; [FAQ DGFiP 3.5](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf)). **Une Commande abandonnée et purgée à 24 h ne consomme aucun numéro.**
- **Un logiciel de caisse certifié** : les assujettis en franchise en base en sont exclus ([BOI-TVA-DECLA-30-10-30, version du 25/03/2026, § 25](https://bofip.impots.gouv.fr/bofip/10691-PGP.html/identifiant=BOI-TVA-DECLA-30-10-30-20260325)).

### Dates butoirs

| Date | Ce qui tombe | Source |
| --- | --- | --- |
| **1er sept. 2026** *(passé)* | Capacité de **recevoir** une facture électronique via une plateforme agréée — toutes entreprises | FAQ 5.1 ; art. 91 LF 2024 |
| **1er sept. 2026** *(passé)* | 4 nouvelles mentions au 242 nonies A dont **SIREN du client** et **catégorie de l'opération (PS)** | FAQ 3.4 ; décret 2022-1299 |
| **1er janv. 2027** | Délai de conservation du **LPF porté à dix ans** | [L102 B, version 2027](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053189496/2029-01-01) |
| **1er janv. 2027** | Terme des versions actuelles de **L441-9 C. com.** et de l'**art. 19 LCEN** — à revérifier | Légifrance |
| **1er sept. 2027** | Obligation d'**émettre** en facture électronique (micro-entreprises) | FAQ 5.1 ; art. 91 LF 2024 |
| **1er sept. 2027** | Obligation d'**e-reporting B2C**, fréquence **bimestrielle** en franchise en base | FAQ 8.1, **9.3** |

### Les cinq zones grises à faire trancher

1. **Le moment de la note en vente à distance prépayée** — « avant paiement du prix » n'a pas de sens quand le paiement précède l'exécution (§ 1.6).
2. **L'affichage de l'art. 2 et le « double exemplaire » de l'art. 4** transposés en ligne (§ 1.6).
3. **L'admissibilité d'une adresse de domiciliation** en substitution de l'adresse du domicile (§ 3.5).
4. **Le trou dans la séquence de numérotation** : aucune source primaire ni doctrinale ne dit quoi faire d'un numéro abandonné (§ 4.4).
5. **L'articulation des délais de conservation** — deux ans pour la note (arrêté art. 6), dix ans pour la pièce justificative (L123-22) (§ 6).
