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

---

## 4. Règlement IA (AI Act) — applicable depuis dix-huit jours, et il vise le produit

Ce volet n'était pas au brief. Il s'impose quand même : **l'article 50 du règlement (UE) 2024/1689 est applicable depuis le 2 août 2026**, soit dix-huit jours avant la rédaction de ce document.

### 4.1 [TEXTE] ouvrance est un « déployeur »

[Règlement (UE) 2024/1689, art. 3, point 4](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) :

> « **«déployeur»**, une personne physique ou morale […] **utilisant sous sa propre autorité un système d'IA** sauf lorsque ce système est utilisé dans le cadre d'une **activité personnelle à caractère non professionnel** »

ouvrance appelle Seedance et Nano Banana Pro sous sa propre autorité, à titre professionnel : c'est un déployeur. Les fournisseurs sont ByteDance/BytePlus et Google ; fal.ai est un intermédiaire.

### 4.2 [TEXTE] Une cinématique ouvrance est un « hypertrucage » au sens du texte

Art. 3, point 60 :

> « **«hypertrucage»**, une image ou un contenu audio ou vidéo **généré ou manipulé par l'IA, présentant une ressemblance avec des personnes** […] existants et **pouvant être perçu à tort par une personne comme authentiques ou véridiques** »

La définition est remplie dès qu'une Personne représentée est reconnaissable dans la sortie.

### 4.3 [TEXTE] L'obligation de l'article 50 §4 — et l'assouplissement « œuvre créative »

Art. 50 §4, premier alinéa, verbatim :

> « Les **déployeurs** d'un système d'IA qui génère ou manipule des images ou des contenus audio ou vidéo **constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA**. […] **Lorsque le contenu fait partie d'une œuvre ou d'un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l'existence de tels contenus générés ou manipulés d'une manière appropriée qui n'entrave pas l'affichage ou la jouissance de l'œuvre.** »

Art. 50 §5 :

> « Les informations visées aux paragraphes 1 à 4 sont fournies aux personnes physiques concernées **de manière claire et reconnaissable au plus tard au moment de la première interaction ou de la première exposition**. »

> **Lecture pour ouvrance.** Un jeu d'infiltration « braquage du musée » est manifestement une œuvre de fiction : l'assouplissement s'applique, et il n'est **pas** exigé de placarder un bandeau qui gâche l'expérience. Mais l'obligation ne disparaît pas — elle se réduit à une **divulgation de l'existence** du contenu généré, faite **au plus tard à la première exposition**, donc **sur l'écran d'ouverture du Lien**, pas dans un pied de page.
>
> C'est exactement la même mention que celle qu'exige l'article 226-8 du Code pénal (§3.3). **Une seule mention, bien placée, satisfait les deux textes.**

### 4.4 [TEXTE] La sanction

Art. 99 §4 g) : la non-conformité aux « obligations de transparence pour les fournisseurs et les déployeurs **conformément à l'article 50** » est passible d'une amende administrative « pouvant aller **jusqu'à 15 000 000 EUR** ou, si l'auteur de l'infraction est une entreprise, **jusqu'à 3 % de son chiffre d'affaires annuel mondial total** […] le montant le plus élevé étant retenu ».

Art. 99 §6 tempère pour les petites structures : « Dans le cas des **PME**, y compris les jeunes pousses, chaque amende […] s'élève au maximum aux pourcentages ou montants visés […] **le chiffre le plus faible étant retenu**. » Pour ouvrance, le plafond pratique est donc 3 % du chiffre d'affaires, pas 15 M€ — mais l'obligation est la même.

### 4.5 [TEXTE] Date d'application

Art. 113 : « Il est applicable à partir du **2 août 2026**. » Le chapitre IV (dont l'article 50) n'est dans aucune des exceptions a), b) ou c). **L'obligation est en vigueur maintenant, avant même la première vente du nouveau jalon.**

---

## 5. Informer la Personne représentée — l'article 14, l'obligation la plus oubliée

### 5.1 [TEXTE] Pourquoi c'est l'article 14 et pas l'article 13

Les données de la Personne représentée ne sont **pas collectées auprès d'elle** : elles viennent de l'Offrant. C'est le champ exact de [l'article 14 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3), qui impose de fournir identité du responsable, finalités, catégories de données, destinataires, transferts hors UE, durée de conservation, droits, droit de réclamation auprès de la CNIL, et **la source des données**.

Art. 14 §3 a) : les informations sont fournies « **dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois** ».

### 5.2 [ZONE GRISE] L'exception « effort disproportionné » ne sauve pas ouvrance

Art. 14 §5 b) : l'obligation tombe « **si la fourniture de telles informations se révèle impossible ou exigerait des efforts disproportionnés** ».

Tentant. Mais l'argument est faible ici, pour une raison factuelle : dans le scénario le plus fréquent du produit, la Personne représentée **est le Destinataire lui-même** — celui à qui le Lien est transmis. Et l'Offrant, lui, la connaît toujours. Là où l'on peut demander, l'effort n'est pas disproportionné.

> **[ZONE GRISE]** Il faut distinguer deux configurations que le produit confond aujourd'hui :
> - **Personne représentée = Destinataire.** Elle recevra le Lien. L'information peut lui être donnée **à l'ouverture**, et le retrait de consentement exercé immédiatement. Configuration gérable.
> - **Personne représentée ≠ Destinataire** (le cadeau met en scène un tiers qui ne verra rien — le couple d'amis, un parent absent). Là, personne n'informe personne. **C'est la configuration réellement problématique** et aucune source primaire ne dit comment s'en sortir autrement qu'en passant par l'Offrant. **À faire trancher.**
>
> **Conséquence produit** : le formulaire doit **demander, pour chaque média, si la personne qui y figure est le Destinataire ou un tiers**, parce que les obligations diffèrent. Ce champ n'existe pas aujourd'hui.

### 5.3 [TEXTE] Les droits qu'il faut pouvoir servir, et en combien de temps

| Droit | Article | Ce que ça impose techniquement |
| --- | --- | --- |
| **Effacement** | Art. 17 §1 b) « la personne concernée **retire le consentement** […] et il n'existe pas d'autre fondement juridique » ; c) opposition ; d) « les données ont fait l'objet d'un **traitement illicite** » | Supprimer les médias d'une Commande **et** couper le Lien d'un Cadeau livré |
| **Opposition** | Art. 21 §1 — mais il ne vise que les traitements fondés sur l'art. 6 §1 e) ou f). Sur base consentement, c'est le **retrait du consentement** (art. 7 §3) qui joue, et il est plus fort : il s'exerce **sans motif** | Un moyen de retrait accessible sans compte |
| **Délai** | Art. 12 §3 — « dans les meilleurs délais et en tout état de cause dans un **délai d'un mois** » | Une adresse de contact réellement relevée, et une procédure écrite |

> **Point de conception majeur.** Parce que la base légale est le consentement (§2.3) et non l'intérêt légitime, la Personne représentée peut retirer son consentement **à tout moment et sans avoir à se justifier**. Un Cadeau livré doit donc pouvoir être **coupé unilatéralement**, sans négociation avec l'Offrant qui l'a payé. C'est un conflit commercial inévitable : **il doit être annoncé dans les CGU, pas découvert le jour où il arrive.**

### 5.4 [CNIL] Ce que la doctrine CNIL apporte — et ce qu'elle n'apporte pas

Trois ressources de la CNIL ont été consultées directement et sont utilisables :

- [« Les durées de conservation des données »](https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees) — le cycle en **trois phases** (base active / archivage intermédiaire / archivage définitif), et le principe : « La définition de la durée de conservation relève de l'analyse de conformité que le responsable de traitement doit mener pour son traitement. » Utilisée en §6.
- [« Intérêt légitime »](https://www.cnil.fr/fr/les-bases-legales/interet-legitime) — les trois conditions cumulatives et les attentes raisonnables. Utilisée en §2.3.
- [« Ce qu'il faut savoir sur l'AIPD »](https://www.cnil.fr/fr/ce-quil-faut-savoir-sur-lanalyse-dimpact-relative-la-protection-des-donnees-aipd) et la [liste des traitements pour lesquels une AIPD est requise](https://www.cnil.fr/sites/cnil/files/atoms/files/liste-traitements-aipd-requise.pdf). Utilisées en §9.

> **[ZONE GRISE] — honnêteté sur ce qui n'a pas pu être établi.** Le brief demandait « les recommandations de la CNIL sur l'IA générative » et « les sanctions pertinentes ». Le hub [cnil.fr/fr/intelligence-artificielle](https://www.cnil.fr/fr/intelligence-artificielle) a bien été atteint, mais il ne présente que des actualités (note exploratoire sur l'IA agentique du 20/07/2026, publication CEPD sur l'anonymisation et le moissonnage du 09/07/2026, affiche PIPC-CNIL du 27/05/2026, enquête européenne du 05/05/2026, projet PANAME du 26/02/2026) ; **les pages de fiches pratiques IA et de sanctions n'ont pas répondu** (404 sur les URL essayées), et le budget de recherche web de la session était épuisé, empêchant de retrouver les URL exactes.
>
> **Aucune délibération de sanction n'est donc citée ici, et aucun numéro de délibération n'est inventé.** C'est un manque réel de ce document. Il ne change pas les conclusions, qui reposent toutes sur des textes — mais **la relecture par un avocat devra couvrir la doctrine CNIL récente sur l'IA générative**, l'endroit le plus susceptible de contenir une position spécifique sur la génération de visages de tiers.

---

## 6. Durées de conservation et droit à l'effacement

### 6.1 Le point d'architecture qui désamorce la moitié du problème

Avant de parler de durées, il faut rendre explicite une conséquence de **l'invariant économique** fixé au ticket [#1](https://github.com/fayssalbenouda936/ouvrance/issues/1), parce qu'elle change la qualification juridique de tout le flux :

> « Une cinématique se génère **une fois** et se revend indéfiniment. Seedance 2.5 ne tourne qu'à l'écriture d'une expérience, **jamais à la vente d'une commande**. La personnalisation est une couche de texte, de photos et d'audio **posée par-dessus un rendu maître figé**. »

**Donc : dans l'architecture cible, les médias de la Personne représentée ne sont jamais envoyés à un modèle génératif.** Ils sont stockés dans R2 et composités dans le navigateur du Destinataire, par-dessus une vidéo maître qui, elle, ne contient aucune personne réelle.

C'est le contraire du *legacy*, où `outils/fal.mjs` convertit les fichiers locaux en data URI et les fait transiter par fal. **Le ticket #4 posait la question de la qualification de ce transit : dans l'architecture cible, il n'existe plus.**

Quatre conséquences, toutes favorables :

1. **Les interdictions de BytePlus 3.5, de la PUP Google 1.6 et de l'AUP fal.ai ne sont pas déclenchées** par les commandes. Elles restent pleinement applicables à l'**écriture** des expériences maîtres — mais celles-ci ne mettent en scène aucune personne réelle, donc elles ne posent pas de problème non plus. La conclusion de [`rgpd-conditions-modeles.md`](./rgpd-conditions-modeles.md) — « aucune des deux voies via fal.ai n'est tenable en l'état » — vaut pour un scénario où l'on aurait fait générer le visage d'un tiers par un modèle. **La bonne réponse n'est pas de changer de fournisseur : c'est de ne jamais lui envoyer ces médias.**
2. **Aucun transfert hors UE des médias de la Personne représentée**, si le bucket R2 est en `jurisdiction=eu` et privé (cf. [`rgpd-sous-traitants.md`](./rgpd-sous-traitants.md)).
3. **Le critère « moyens » de l'article 4(14) tombe pour de bon** (§1.4) : une incrustation navigateur n'extrait aucun gabarit. La réserve 1.5.1 disparaît.
4. **Mais l'article 226-8 du Code pénal continue de s'appliquer**, parce que son premier membre de phrase ne parle pas d'IA du tout : « **le montage** réalisé avec les paroles ou l'image d'une personne sans son consentement ». Coller un visage réel dans une scène de braquage **est** un montage. La mention de §3.3 reste obligatoire.

> **À porter comme règle d'architecture, pas comme note de conformité : aucun média téléversé par un Offrant ne doit jamais atteindre un point de terminaison de modèle génératif.** C'est vérifiable en test.

### 6.2 [TEXTE + CNIL] Le principe, et le cycle en trois phases

[RGPD art. 5 §1 e)](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2) : les données sont « **conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire** au regard des finalités ». Et art. 5 §2 : « Le responsable du traitement est responsable du respect du paragraphe 1 et **est en mesure de démontrer que celui-ci est respecté** ».

[CNIL, « Les durées de conservation des données »](https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees) : trois phases — **base active** (« la durée nécessaire à la réalisation de l'objectif »), **archivage intermédiaire** (les données ne servent plus la finalité initiale mais présentent un intérêt administratif ou doivent être conservées légalement ; « consultées de manière ponctuelle et motivée par des personnes spécifiquement habilitées »), **archivage définitif**. Et le principe d'imputation : « La définition de la durée de conservation relève de **l'analyse de conformité que le responsable de traitement doit mener** pour son traitement. »

**Traduction pour ouvrance** : personne ne fournira ces durées ; il faut les fixer et savoir les justifier. Ci-dessous une proposition chiffrée, avec le raisonnement de chaque ligne.

### 6.3 Proposition de durées, ligne par ligne

| Donnée | Base active | Archivage intermédiaire | Fondement du chiffre |
| --- | --- | --- | --- |
| **Médias de la Personne représentée** (photos, vocaux) dans R2 | **Durée de vie du Lien** — voir 6.4 | **Aucun.** Purge sèche | Art. 5 §1 e). Passé l'expiration du Lien, plus aucune finalité ne les justifie |
| **Médias d'une Commande non payée** | **24 heures** | Aucun | Voir section 7 — le chiffre est adossé à la durée de vie maximale d'une session Stripe |
| **Contenu de personnalisation non personnel** (messages, montant, choix de casting) | Durée de vie du Lien | Aucun | Même raisonnement ; le message peut d'ailleurs contenir des données personnelles, à traiter comme tel |
| **Identité et email de l'Offrant, données de commande** | Durée de la relation commerciale | **5 ans** | [Art. L110-4 du Code de commerce](https://entreprendre.service-public.gouv.fr/vosdroits/F10029) — prescription des obligations commerciales, cité par service-public comme durée de conservation des contrats commerciaux |
| **Pièces comptables et factures** | Exercice en cours | **10 ans** à compter de la clôture de l'exercice | [Art. L123-22 du Code de commerce](https://entreprendre.service-public.gouv.fr/vosdroits/F10029) |
| **Preuve du consentement et déclaration de l'Offrant** (horodatage, version du libellé, IP) | Durée de vie du Lien | **5 ans** après | Art. 5 §2 et art. 7 §1 : il faut pouvoir **démontrer**. Aligné sur la prescription de l'art. L110-4 |
| **Journal des demandes d'effacement** et des suites données | — | **5 ans** | Même raisonnement d'*accountability* |
| **Logs techniques** (accès au Lien, erreurs) | — | **6 mois**, sans donnée d'identification du Destinataire | **[ZONE GRISE]** — 6 mois est la durée usuellement retenue pour les logs de connexion, mais **la délibération CNIL correspondante n'a pas pu être vérifiée dans cette session**. À confirmer |

**Un point de droit de la consommation à ne pas confondre.** service-public indique une obligation de conservation de **10 ans** pour les « contrats conclus par voie électronique » — mais **seulement à partir de 120 €** ([même source](https://entreprendre.service-public.gouv.fr/vosdroits/F10029)). La carte à 14,99 € et le jeu à 69,99 €, même avec les suppléments à 3 € l'unité plafonnés à 7 unités (soit 90,99 € au maximum), **restent sous le seuil**. Cette obligation ne s'applique donc pas à ouvrance — mais elle s'appliquerait dès qu'une formule ou un panier dépasserait 120 €, ce qui est exactement le cas des formules Extra (149 €) et Ultimate (349 €) mises hors périmètre. **À rouvrir si elles reviennent.**

### 6.4 La durée de vie du Lien — le chiffre que le ticket #1 a laissé ouvert

Le ticket [#1](https://github.com/fayssalbenouda936/ouvrance/issues/1) classe « expiration des liens de cadeau, purge » dans *Not yet specified*, en précisant que cela « dépend du RGPD ». Voici la proposition et son raisonnement.

**Proposition : le Lien est actif 12 mois à compter de la livraison. À l'expiration, les médias de la Personne représentée sont purgés et le Lien renvoie une page d'expiration.**

Pourquoi 12 mois :

- **Plancher.** Un cadeau se consomme en quelques jours. Une durée courte (30 jours) serait défendable au regard de l'article 5 §1 e) mais détruirait la valeur perçue : un cadeau qu'on ne peut plus revoir n'est pas un cadeau.
- **Plafond.** Au-delà d'un an, la finalité « offrir et faire vivre une expérience » est épuisée. Conserver le visage et la voix d'un tiers *pour le cas où* est exactement ce que l'article 5 §1 e) interdit.
- **Le chiffre est adossé à un fait, pas à une préférence** : la relecture d'un cadeau se fait à la date anniversaire de l'événement. **12 mois couvre exactement un anniversaire, pas deux.** C'est le plus petit nombre qui préserve l'usage réel.
- **Effet de bord commercial favorable** : l'email d'avertissement 30 jours avant l'expiration est un point de contact naturel, et une prolongation payante est une offre honnête — à condition qu'elle exige **un nouveau consentement**, pas une reconduction tacite.

### 6.5 Supprimer un Cadeau déjà livré — ce que ça veut dire techniquement

C'est la question la plus concrète du ticket. Trois niveaux, à ne pas confondre :

1. **Couper le Lien** — le Cadeau devient inaccessible. **Effet immédiat exigible** : l'article 9 du Code civil permet au juge d'ordonner l'arrêt **en référé** (§3.1), et l'article 12 §3 du RGPD impose au plus un mois. **Il faut donc un interrupteur, pas une procédure.** Concrètement : un champ d'état sur le Cadeau, vérifié à chaque requête, et **jamais** de bucket R2 public ni d'URL présignée de longue durée — sinon la coupure n'en est pas une, le CDN de Cloudflare continuant de servir des copies mises en cache hors UE (cf. [`rgpd-sous-traitants.md`](./rgpd-sous-traitants.md)).
2. **Effacer les médias** — suppression des objets R2 du préfixe de la Commande, sans corbeille ni sauvegarde de longue durée. Toute sauvegarde doit avoir une rotation courte et documentée, faute de quoi l'effacement est fictif.
3. **Ce qu'on conserve malgré tout** — [art. 17 §3](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3) autorise à conserver ce qui est nécessaire au respect d'une obligation légale et à « la constatation, l'exercice ou la défense de droits en justice ». Sont donc conservés : **la facture** (10 ans), **l'enregistrement de commande minimal** (5 ans), **la preuve du consentement** et **la trace de l'effacement lui-même**. Ne sont **pas** conservés : les photos, les vocaux, les messages.

> **Le point qui fâche, et il faut le décider maintenant.** Si la Personne représentée demande l'effacement, le Cadeau payé par l'Offrant est coupé. Faut-il rembourser ? Le droit ne l'impose pas explicitement, mais un juge peut voir dans un service devenu inexécutable une raison de restitution. **Le plus simple et le plus honnête : l'annoncer dans les CGU et rembourser au prorata du temps restant.** Le coût marginal d'une commande étant de 1,39 € (ticket [#5](https://github.com/fayssalbenouda936/ouvrance/issues/5)), le remboursement est économiquement indolore et supprime tout le contentieux. **[ZONE GRISE]** sur l'obligation ; certitude sur l'intérêt.

---

## 7. La purge des commandes non payées — la conséquence directe de « formulaire puis paiement »

### 7.1 Le problème, énoncé sans détour

Le ticket [#1](https://github.com/fayssalbenouda936/ouvrance/issues/1) a tranché : « **Formulaire puis paiement** — le bouton payer est à la fin du formulaire. Décision prise contre la recommandation initiale ; la conséquence RGPD (données déposées avant tout contrat) est portée par le ticket RGPD sous forme de **purge courte des commandes non payées**. »

En clair : à chaque abandon de tunnel, **les photos et la voix d'un tiers restent dans R2 sans qu'aucun contrat n'ait jamais existé**. Et pour la Personne représentée, la base « mesures précontractuelles » de l'article 6 §1 b) n'est même pas disponible : elle n'est partie à aucune mesure précontractuelle (§2.1). **La seule base reste le consentement, pour un traitement dont la finalité — livrer un cadeau — ne se réalisera jamais.**

L'article 5 §1 e) est alors sans ambiguïté : la durée nécessaire est **le temps de payer**, et rien de plus.

### 7.2 La durée : 24 heures

**Proposition chiffrée : purge de tous les médias d'une Commande non payée 24 heures après sa création.**

Le raisonnement, et c'est ce qui rend le chiffre défendable devant une autorité de contrôle : **il n'est pas arbitraire, il est adossé à une contrainte technique externe et vérifiable.**

[Documentation Stripe, « Gérer un stock limité »](https://docs.stripe.com/payments/checkout/managing-limited-inventory), consultée le 20 août 2026 :

> « La valeur doit être comprise entre **30 minutes et 24 heures** après l'heure actuelle. Si vous ne spécifiez pas `expires_at`, la valeur par défaut est **24 heures** après l'heure actuelle. »

> **24 heures est donc la durée maximale pendant laquelle un paiement peut encore aboutir.** Passé ce délai, Stripe lui-même déclare la session `expired` : la finalité est éteinte, pas par choix mais par construction. Conserver les médias une heure de plus, c'est conserver le visage d'un tiers pour une finalité qui n'existe plus. **Aucune durée supérieure n'est justifiable, et la durée n'a pas à être négociée : elle est imposée par la plomberie du paiement.**

Si le commerce réclamait une fenêtre de relance de panier abandonné, le plafond argumentable serait **72 heures**, et il faudrait alors : l'annoncer explicitement dans la case à cocher, et le justifier au registre. **Ce n'est pas recommandé** — la relance de panier abandonné vaut 1,39 € de coût marginal évité, contre la conservation des données biométriques d'une personne qui n'a rien demandé.

### 7.3 Le mécanisme : trois déclencheurs, parce qu'un seul ne couvre pas tout

Il y a **trois façons** de ne pas payer, et une seule d'entre elles émet un événement.

| Cas | Ce qui se passe | Déclencheur de purge |
| --- | --- | --- |
| **A.** L'Offrant remplit le formulaire, arrive sur Stripe, n'achève pas | Stripe passe la session à `expired` et **émet `checkout.session.expired`** | **Webhook signé.** Purge immédiate du préfixe R2 de la Commande |
| **B.** L'Offrant remplit le formulaire et ferme l'onglet **avant** de cliquer payer | Aucune session Stripe n'existe. **Aucun événement, jamais** | **Cron.** Balayage horaire supprimant toute Commande en état `brouillon` ou `impayée` de plus de 24 h |
| **C.** Le webhook est perdu, rejoué en échec, ou l'endpoint est indisponible | La Commande reste impayée en base indéfiniment | **Le même cron**, qui sert de filet |

Trois exigences d'implémentation qui découlent de ce tableau :

1. **Le cron est la garantie, pas le webhook.** Le webhook est une optimisation qui purge plus tôt ; c'est le balayage périodique qui rend la purge *inévitable*. Un système qui ne repose que sur le webhook ne couvre pas le cas B, qui est probablement le plus fréquent.
2. **La purge doit être vérifiable.** Elle doit écrire une ligne dans un journal (identifiant de commande, horodatage, nombre d'objets supprimés) — c'est la preuve exigée par l'article 5 §2.
3. **Elle doit supprimer les objets R2, pas seulement la ligne en base.** Un enregistrement effacé qui laisse les fichiers orphelins dans le bucket est le mode d'échec par défaut de ce genre de mécanisme. **À tester explicitement** : créer une commande, ne pas payer, avancer l'horloge, vérifier que `list` sur le préfixe ne renvoie rien.

> **Et une conséquence de conception qui ne coûte rien : ne téléverser les médias qu'au dernier moment.** Si le formulaire n'envoie les fichiers dans R2 qu'au clic sur « payer » plutôt qu'à chaque étape, le cas B — le plus fréquent et le seul non instrumenté — **cesse d'exister**. C'est la minimisation de l'article 5 §1 c) appliquée au tunnel : la meilleure purge est celle qui n'a rien à purger. Cela ne remet pas en cause la décision « formulaire puis paiement », qui porte sur l'**ordre des écrans**, pas sur le moment du téléversement.
