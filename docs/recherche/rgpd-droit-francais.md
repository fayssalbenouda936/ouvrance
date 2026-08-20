# Volet juridique français — base légale, droit à l'image, doctrine CNIL, conservation

**Recherche du ticket [#4](https://github.com/fayssalbenouda936/ouvrance/issues/4).** Pages consultées le **20 août 2026**. Extraits verbatim, chaque affirmation porte sa source.

Ce document complète [`rgpd-conditions-modeles.md`](./rgpd-conditions-modeles.md) (conditions Seedance / Nano Banana Pro / fal.ai) et [`rgpd-sous-traitants.md`](./rgpd-sous-traitants.md) (Cloudflare, Stripe, Brevo, Resend, Formspree). Il traite ce qu'ils ne traitaient pas : le **droit français et européen applicable à ouvrance**.

> ⚠️ **Ce document n'est pas un avis juridique.** Il est écrit par un agent, pas par un juriste. Trois registres sont distingués partout et il faut les lire comme tels :
> - **[TEXTE]** — ce que la loi ou le règlement dit, verbatim, avec sa référence.
> - **[CNIL]** — ce que l'autorité recommande ou a sanctionné. Opposable en pratique, mais ce n'est pas la loi.
> - **[ZONE GRISE]** — ce qu'aucune source primaire ne tranche. **À faire trancher par un avocat avant mise en vente.**

**Vocabulaire.** Les termes du domaine sont ceux fixés au ticket [#2](https://github.com/fayssalbenouda936/ouvrance/issues/2) : l'**Offrant** achète et personnalise, le **Destinataire** ouvre le Lien, et la **Personne représentée** est le tiers dont le visage ou la voix figure dans le Cadeau. C'est cette dernière qui n'a aucune relation avec la plateforme — et tout ce document parle d'elle.

---

## 1. Qualification : donnée personnelle ordinaire ou donnée biométrique de l'article 9 ?

C'est la première question à trancher, parce qu'elle commande tout le reste. Si les photos et vocaux relèvent de l'article 9, **seul le consentement explicite de la Personne représentée** peut fonder le traitement, et l'intérêt légitime devient inaccessible. S'ils n'en relèvent pas, l'éventail des bases légales reste ouvert.

### 1.1 [TEXTE] La définition de l'article 4, point 14 — trois éléments, pas un

[RGPD art. 4(14)](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1), verbatim :

> « les données à caractère personnel **résultant d'un traitement technique spécifique**, relatives aux caractéristiques physiques, physiologiques ou comportementales d'une personne physique, **qui permettent ou confirment son identification unique**, telles que **des images faciales** ou des données dactyloscopiques »

Et l'[article 9 §1](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679) n'interdit pas les données biométriques en général — il vise :

> « le traitement des données génétiques, **des données biométriques aux fins d'identifier une personne physique de manière unique**, des données concernant la santé […] est interdit »

La finalité est donc dans le texte de l'interdiction elle-même. Une donnée biométrique traitée à une autre fin que l'identification unique n'est pas dans le champ de l'article 9.

### 1.2 [TEXTE] Le considérant 51 dit explicitement que la photo n'y suffit pas

[Considérant 51 du RGPD](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679), verbatim :

> « **Le traitement des photographies ne devrait pas systématiquement être considéré comme constituant un traitement de catégories particulières de données à caractère personnel**, étant donné que celles-ci ne relèvent de la définition de données biométriques **que lorsqu'elles sont traitées selon un mode technique spécifique permettant l'identification ou l'authentification unique d'une personne physique**. »

### 1.3 [CNIL/CEPD] Les trois critères cumulatifs du CEPD

Les [lignes directrices 3/2019 du CEPD sur le traitement des données à caractère personnel par dispositifs vidéo](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices_fr.pdf) (version 2.0, adoptée le 29 janvier 2020) posent la grille de lecture opérationnelle.

**§74** :

> « Les enregistrements vidéo représentant une personne **ne peuvent toutefois pas être considérés comme des données biométriques au sens de l'article 9 s'ils n'ont pas fait l'objet d'un traitement technique spécifique en vue de contribuer à l'identification d'une personne**. »

**§76 — les trois critères** :

> « - **la nature des données** : les données se rapportent aux caractéristiques physiques, physiologiques ou comportementales d'une personne physique ;
> - **les moyens et modalités de traitement** : les données résultent « d'un traitement technique spécifique » ;
> - **la finalité du traitement** : les données doivent être traitées **afin d'identifier une personne physique de manière unique**. »

**§80 — et l'exclusion qui nous concerne** :

> « lorsque le traitement vise, par exemple, à distinguer deux catégories de personnes **et non à identifier une personne physique de manière unique**, celui-ci **ne relève pas de l'article 9**. »

À l'inverse, **§82** : l'article 9 s'applique « si le responsable du traitement **conserve** des données biométriques (le plus souvent au moyen de **modèles** créés par l'extraction de caractéristiques clés issues de données biométriques brutes, telles que les mesures du visage obtenues à partir d'une image) **afin d'identifier une personne de manière unique** ».

### 1.4 Application à ouvrance — la réponse, critère par critère

| Critère CEPD | Photo de visage téléversée pour incrustation | Vocal téléversé |
| --- | --- | --- |
| **Nature** — caractéristique physique / comportementale | **Oui** | **Oui** (la voix est une caractéristique physiologique) |
| **Moyens** — « traitement technique spécifique » | **Non** pour une simple incrustation (redimensionnement, masque, compositing) ; **oui** dès qu'un modèle extrait un gabarit de visage pour préserver la ressemblance | **Non** pour une simple lecture ; **oui** si un modèle extrait une empreinte vocale |
| **Finalité** — **identifier de manière unique** | **Non.** La finalité est de *représenter* une personne dans une fiction, jamais de la *reconnaître* ou de la retrouver | **Non.** La finalité est le timbre, jamais la reconnaissance du locuteur |

> **Conclusion.** Le troisième critère n'étant pas rempli, et le RGPD exigeant les trois cumulativement, **une photo de visage téléversée pour incrustation n'est pas un traitement biométrique au sens de l'article 9**. C'est une **donnée personnelle ordinaire**, à haut risque, mais ordinaire. Idem pour la voix.
>
> **Ce que cela change concrètement** : l'article 9 §2 a) — consentement **explicite** de la personne concernée, sans autre issue — ne s'impose pas. L'article 6 reste ouvert. **Ce que cela ne change pas** : l'article 6 doit quand même être satisfait, et la section 2 montre que c'est là que le vrai problème se trouve.

### 1.5 [ZONE GRISE] Trois réserves qui peuvent renverser la qualification

1. **La préservation d'identité des modèles génératifs.** Un `reference-to-video` qui « garde le même visage d'un plan à l'autre » calcule bien un plongement (*embedding*) de visage. Le critère « moyens » est alors rempli. On tient encore par le critère « finalité » — mais aucune source primaire ne dit ce qu'il advient quand le gabarit sert à *reproduire* plutôt qu'à *identifier*, et le CEPD n'a pas rendu de position sur ce point. **À faire trancher.** La position de repli, si l'on veut supprimer le risque : traiter le flux comme si l'article 9 s'appliquait, c'est-à-dire exiger le consentement explicite de la Personne représentée — ce qui, comme le montre la section 2, est de toute façon la seule voie tenable.

2. **Le contenu de la photo peut être sensible par lui-même.** L'article 9 §1 vise aussi les données « **révélant** l'origine raciale ou ethnique […] les convictions religieuses ou philosophiques ». Une photo de mariage religieux, un signe religieux visible, un fauteuil roulant (santé) : la photo devient une donnée de l'article 9 **par son contenu**, indépendamment de tout traitement biométrique. Sur un produit dont les occasions incluent le mariage, ce n'est pas théorique. **Le formulaire ne peut pas filtrer cela ; seule la porte de validation humaine le peut.**

3. **Le DPA de fal.ai décline explicitement ce cas** — cité dans [`rgpd-sous-traitants.md`](./rgpd-sous-traitants.md) : « The Services are **not designed for special categories of Personal Data** ». Si la réserve 1 ou 2 se réalise, le sous-traitant a contractuellement écarté sa responsabilité.

---

## 2. Base légale : le consentement de l'Offrant ne suffit pas

### 2.1 [TEXTE] Ce que l'article 6 permet, et ce qu'il exige

[RGPD art. 6 §1](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2) : le traitement n'est licite que si l'une des six bases est réunie. Passons-les au crible **pour la Personne représentée** — pas pour l'Offrant, dont le cas est banal.

| Base | Disponible pour la Personne représentée ? |
| --- | --- |
| **a) consentement** | Oui — mais il doit venir **d'elle**, pas de l'Offrant (voir 2.2) |
| **b) contrat** | **Non.** « un contrat **auquel la personne concernée est partie** ». La Personne représentée n'est partie à rien. C'est précisément la particularité du produit |
| **c) obligation légale** | Non |
| **d) intérêts vitaux** | Non |
| **e) mission d'intérêt public** | Non |
| **f) intérêt légitime** | Théoriquement ouvert, en pratique très fragile (voir 2.3) |

### 2.2 [TEXTE] Le consentement de l'Offrant est juridiquement sans objet

[RGPD art. 4(11)](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1) :

> « toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle **la personne concernée** accepte […] que des données à caractère personnel **la concernant** fassent l'objet d'un traitement »

Le consentement est, par définition textuelle, **celui de la personne concernée**. L'Offrant n'est pas la personne concernée par les données de la Personne représentée. Son clic ne consent à rien la concernant.

> **Réponse directe à la question du ticket : non, le consentement de l'Offrant ne suffit pas.** Ce n'est pas une question d'appréciation ; c'est la définition même du mot dans le règlement.

### 2.3 [TEXTE + CNIL] L'intérêt légitime : pourquoi il ne tient pas ici

[RGPD art. 6 §1 f)](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2) : le traitement doit être « nécessaire aux fins des intérêts légitimes poursuivis par le responsable du traitement ou par un tiers », **sauf** si prévalent les droits fondamentaux de la personne concernée.

[CNIL — fiche « Intérêt légitime »](https://www.cnil.fr/fr/les-bases-legales/interet-legitime) pose **trois conditions cumulatives** : intérêt légitime (licite, précis, réel et présent), traitement **nécessaire** (« il n'existe pas de solution moins intrusive pour la vie privée »), et **mise en balance** favorable. La CNIL précise que la balance doit tenir compte des « **attentes raisonnables** » des personnes, « sans les surprendre », et qu'elle **exclut** l'intérêt légitime quand le traitement « heurte » gravement les droits fondamentaux ou dépasse ces attentes raisonnables.

Appliqué à ouvrance, la balance penche du mauvais côté sur les trois branches :

- **Intérêt** : vendre un cadeau. Intérêt commercial licite, mais faible en poids.
- **Nécessité** : une solution moins intrusive existe et est évidente — **demander à la Personne représentée**. Dès lors que l'alternative existe, la condition de nécessité tombe.
- **Attentes raisonnables** : personne ne s'attend à voir son visage animé et sa voix synthétisée dans un produit vendu 69,99 € par une société qu'elle ne connaît pas. C'est l'exemple type du « surprendre les personnes ».

> **Conclusion.** L'intérêt légitime n'est pas défendable comme base légale du traitement des médias de la Personne représentée. **La seule base tenable est le consentement de la Personne représentée elle-même** (art. 6 §1 a), et — si la réserve 1.5 se réalise — **explicite** au sens de l'art. 9 §2 a).
>
> Cette conclusion converge exactement avec ce que les conditions des trois fournisseurs exigent déjà (voir [`rgpd-conditions-modeles.md`](./rgpd-conditions-modeles.md)) : BytePlus « without the **explicit consent** of the relevant individuals », Google « without **legally-required consent** », fal.ai « without **their** consent ». Le droit et les contrats disent la même chose.

### 2.4 Que vaut la déclaration sur l'honneur de l'Offrant ?

Il faut séparer deux choses que la case à cocher confond toujours.

**Ce qu'elle ne vaut pas — la base légale.** Une déclaration de l'Offrant ne crée pas un consentement de la Personne représentée. Si la Personne représentée n'a rien accepté, le traitement est sans base légale, **quelle que soit la case cochée**. [RGPD art. 5 §2 et art. 7 §1](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2) : le responsable du traitement doit **démontrer** la licéité et **prouver** le consentement — une déclaration d'un tiers ne prouve rien sur la volonté de la personne concernée.

**Ce qu'elle vaut quand même — et ce n'est pas rien** :

1. **Elle est exigée par les conditions des fournisseurs.** BytePlus, Google et fal.ai imposent d'avoir obtenu le consentement ; la déclaration est la trace qu'ouvrance a posé la question.
2. **Elle déplace la responsabilité contractuelle** entre ouvrance et l'Offrant. Elle ne la déplace **pas** vis-à-vis de l'autorité de contrôle ni de la Personne représentée : ouvrance reste responsable de traitement, et cette qualité ne se cède pas par contrat.
3. **Elle est un élément d'accountability** (art. 5 §2), à condition d'être **horodatée, journalisée et conservée**, pas seulement affichée.

> **[ZONE GRISE]** Nulle part une source primaire ne dit qu'une déclaration sur l'honneur d'un tiers **suffit**. La CNIL n'a pas publié de position sur les plateformes de cadeaux personnalisés. La pratique du marché (impression de photos, livres photo, faire-part) repose de fait sur ce mécanisme, mais aucune de ces industries ne fait *parler et bouger* le visage d'un tiers. **À faire trancher par un avocat.**

**La conséquence produit** : puisque la déclaration ne fabrique pas la base légale, il faut un dispositif qui donne à la Personne représentée une chance réelle de savoir et de s'opposer. C'est l'objet de l'obligation d'information de l'article 14, traitée en section 5.

---

## 3. Droit à l'image et droit à la voix en droit français

Le RGPD n'épuise pas la question. Le droit français ajoute **deux couches indépendantes** qui s'appliquent *en plus*, avec leurs propres sanctions : une civile et une **pénale**. La couche pénale est la plus lourde et la moins connue.

### 3.1 [TEXTE] Article 9 du Code civil — la couche civile

[Légifrance, art. 9 du Code civil](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006419288), version en vigueur depuis le 19 juillet 1970, verbatim :

> « Chacun a droit au respect de sa vie privée. Les juges peuvent, sans préjudice de la réparation du dommage subi, prescrire toutes mesures, telles que **séquestre, saisie et autres, propres à empêcher ou faire cesser une atteinte à l'intimité de la vie privée** : ces mesures peuvent, **s'il y a urgence, être ordonnées en référé**. »

Le droit à l'image n'est pas nommé dans le texte : il est une construction prétorienne assise sur cet article. Deux conséquences opérationnelles se lisent directement dans la lettre :

- **La réparation du dommage** et **les mesures d'arrêt** sont cumulables. Une Personne représentée peut obtenir des dommages-intérêts **et** le retrait.
- **Le référé.** Le retrait peut être ordonné en urgence, en quelques jours. Un Cadeau livré peut donc devoir être coupé très vite. **Cela impose un mécanisme technique de coupure immédiate d'un Lien** — voir section 6.

### 3.2 [ÉTAT] Ce que l'administration française énonce comme le droit applicable

[service-public.gouv.fr, fiche « Droit à l'image »](https://www.service-public.gouv.fr/particuliers/vosdroits/F32103), qui vise le Code civil (art. 7 à 16-14) et le Code pénal (art. 226-1 à 226-9) :

> « Il est nécessaire d'avoir **votre accord écrit** pour utiliser une image où vous êtes **reconnaissable** » — pour la diffusion, la publication, la reproduction **ou la commercialisation**.

Et, sur les exceptions (image d'actualité, lieu public, foule) :

> « Votre accord **n'est pas nécessaire** pour diffuser certaines images à condition que votre **dignité** soit respectée et **votre image ne soit pas utilisée dans un but commercial**. »

> **La finalité commerciale ferme la porte à toutes les exceptions.** Un Cadeau ouvrance est vendu 14,99 € ou 69,99 € : le but commercial est constitué, y compris si la diffusion est privée. La question posée au ticket — « quand l'image sert un produit commercial même à diffusion privée » — se répond donc ainsi : **la diffusion restreinte n'est pas une exception**, elle réduit le préjudice, pas l'illicéité.

Mineurs : « Si l'image est diffusée par un tiers, **l'autorisation des parents (ou du responsable légal) doit obligatoirement être obtenue par écrit**. » — Deux titulaires de l'autorité parentale, donc deux accords.

### 3.3 [TEXTE] Article 226-8 du Code pénal — la couche pénale, et elle vise exactement ouvrance

C'est la disposition la plus importante de tout ce document. [Légifrance, art. 226-8 du Code pénal](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070719/LEGISCTA000006165310/), **section 2 « De l'atteinte à la représentation de la personne »**, version en vigueur depuis le **23 mai 2024** (loi n° 2024-449 du 21 mai 2024 dite SREN, art. 15), verbatim :

> « Est puni d'**un an d'emprisonnement et de 15 000 euros d'amende** le fait de porter à la connaissance **du public ou d'un tiers**, par quelque voie que ce soit, **le montage réalisé avec les paroles ou l'image d'une personne sans son consentement**, s'il n'apparaît pas à l'évidence qu'il s'agit d'un montage ou s'il n'en est pas expressément fait mention. **Est assimilé à l'infraction mentionnée au présent alinéa et puni des mêmes peines le fait de porter à la connaissance du public ou d'un tiers, par quelque voie que ce soit, un contenu visuel ou sonore généré par un traitement algorithmique et représentant l'image ou les paroles d'une personne, sans son consentement**, s'il n'apparaît pas à l'évidence qu'il s'agit d'un contenu généré algorithmiquement ou s'il n'en est pas expressément fait mention. »

Peines portées à **deux ans et 45 000 €** lorsque les faits sont commis par la voie d'un service de communication au public en ligne. L'article 226-8-1, issu du même texte, porte à **deux ans et 60 000 €** le montage **à caractère sexuel** (trois ans et 75 000 € en ligne).

**Trois éléments de ce texte s'appliquent mot à mot au produit :**

1. **« ou d'un tiers ».** L'infraction n'exige **pas** une diffusion publique. Envoyer le Lien au seul Destinataire suffit à porter le contenu « à la connaissance d'un tiers ». **L'argument « c'est privé, c'est un cadeau » ne protège de rien au pénal.**
2. **« un contenu visuel ou sonore généré par un traitement algorithmique ».** L'alinéa ajouté par la loi SREN vise explicitement les contenus générés par IA. Une cinématique Seedance qui fait bouger ou parler la Personne représentée est exactement l'objet du texte.
3. **La cause d'exonération est une mention.** L'infraction n'est constituée que « **s'il n'apparaît pas à l'évidence** qu'il s'agit d'un montage / d'un contenu généré algorithmiquement **ou s'il n'en est pas expressément fait mention** ».

> **Conséquence produit, non négociable et facile à tenir** : **toute expérience contenant l'image ou la voix d'une personne réelle doit porter une mention visible et permanente indiquant qu'il s'agit d'un contenu généré par IA.** C'est une exonération offerte par le texte lui-même. Ne pas la prendre serait absurde : elle coûte un libellé à l'écran et neutralise le volet pénal le plus lourd. Elle doit être **dans l'expérience vue par le Destinataire**, pas seulement dans les CGU que seul l'Offrant lit.

### 3.4 Le droit à la voix

Aucun texte français ne consacre un « droit à la voix » sous ce nom. Il se reconstitue par deux voies, toutes deux déjà citées :

- **Article 9 du Code civil** — la voix est un attribut de la personnalité protégé par la même construction prétorienne que l'image.
- **Article 226-8 du Code pénal** — et là c'est **dans le texte** : « le montage réalisé avec **les paroles** ou l'image d'une personne », et « un contenu visuel **ou sonore** généré par un traitement algorithmique et représentant l'image **ou les paroles** d'une personne ».

> **La voix n'est pas un cas secondaire de l'image : elle est nommée en premier dans le texte pénal.** Or `audio_urls` de Seedance 2.5 accepte jusqu'à 10 fichiers de référence servant à la voix (voir [`rgpd-conditions-modeles.md`](./rgpd-conditions-modeles.md)). Le vocal téléversé est donc, des deux médias, celui qui expose le plus.

### 3.5 [ZONE GRISE] La jurisprudence de la Cour de cassation

Le brief demandait la jurisprudence de la Cour de cassation sur l'exploitation commerciale de l'image. **Elle n'a pas pu être établie sur source primaire dans cette session** : Judilibre et le moteur de Légifrance sont rendus côté client et ne renvoient rien à une récupération directe, et le budget de recherche web de la session était épuisé. **Aucun numéro de pourvoi n'est cité ici, précisément pour ne pas en inventer un.**

Ce que l'on peut affirmer sans elle, parce que cela vient de sources primaires vérifiées : le fondement textuel (art. 9 C. civ.), l'exigence d'accord écrit et l'exclusion des exceptions en cas de but commercial ([service-public.gouv.fr](https://www.service-public.gouv.fr/particuliers/vosdroits/F32103)), et l'incrimination pénale du montage et du contenu généré algorithmiquement (art. 226-8 C. pén.). **Cela suffit à fonder toutes les obligations produit de la section 10.** La recherche de jurisprudence reste à faire pour chiffrer le risque indemnitaire — c'est une question de montant, pas de principe.
