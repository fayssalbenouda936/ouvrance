# Un Lien ne fuit jamais — ni dans un aperçu, ni dans un référent

Le Lien est un secret, et son support est une URL. Tout mécanisme qui recopie une URL ailleurs est donc une fuite, qu'il soit fait pour ça ou non. Quatre en sont capables, et les quatre sont traités.

- **L'aperçu de messagerie.** Un Cadeau expose des métadonnées de partage **identiques pour tous les Cadeaux** : `og:site_name` à la marque, un titre fixe, une description fixe, une image unique servie depuis le domaine R2 public. Aucune donnée de Commande — ni prénom, ni occasion, ni nature de l'expérience — et **aucune génération par commande**. Le `<title>` du document est le même que le titre de partage.
- **Le référent sortant.** La route du Cadeau et le Worker qui sert les dérivés répondent en `Referrer-Policy: no-referrer`, et le lien de virement de la Récompense porte `rel="noopener noreferrer"` sans exception.
- **Les moteurs.** `noindex, nofollow` en balise **et** `X-Robots-Tag: noindex` en en-tête HTTP. `robots.txt` n'interdit rien et ne nomme pas la route des cadeaux.
- **La forme de l'URL.** Le Lien est un segment de chemin, jamais une chaîne de requête.

## Pourquoi

**Parce que la fuite la plus grave n'est pas celle qu'on regarde.** La Récompense se termine par un lien sortant vers le lien de virement de l'Offrant. Sans `Referrer-Policy`, ce domaine tiers reçoit l'URL complète du Cadeau dans l'en-tête `Referer` — il peut ouvrir un cadeau privé, et **révoquer le Lien ne rattrape pas ce qui est déjà dans ses journaux**. Aucune des protections habituelles — URL non devinable, `noindex` — ne couvre ce cas, parce que ce n'est pas un attaquant qui va chercher l'URL : c'est le navigateur qui la donne.

**Parce que l'aperçu personnalisé est tentant et coûte la surprise.** Le legacy le faisait : `apps/gifts/mohamed-lina/index.html` annonçait « Mohamed & Lina, une surprise vous attend au bout de la poursuite… 💍 ». Un aperçu nominatif se remarque et se clique davantage — c'est un vrai gain de taux d'ouverture. Mais il ne s'affiche pas dans une page qu'on choisit d'ouvrir : il s'affiche dans la **notification d'écran verrouillé** du Destinataire, avant tout geste. Un produit dont la valeur entière est la surprise divulgâchait prénoms, occasion et nature de l'expérience dans l'aperçu de son propre lien.

**Parce qu'un aperçu par commande serait aussi un rendu par vente.** Générer une image de partage par Cadeau produit un dérivé personnel de plus, qu'il faudrait servir publiquement pour qu'il soit lisible par les robots des messageries — donc hors de la vérification du Lien qui protège tous les autres dérivés. La règle « rien ne se rend à la vente » et la règle « les dérivés personnels meurent avec le Lien » tombent ensemble.

**Parce que la marque, elle, ne divulgâche rien.** Le nom ne dit rien au Destinataire, alors qu'un lien nu dans un SMS ressemble à de l'hameçonnage. Il reste donc dans l'aperçu — et c'est le seul référencement qui rapporte quelque chose : chaque Lien collé dans une conversation est une impression de marque, et c'est elle qui alimente la requête de marque que le site vise.

## Conséquences

- **Le tiers n'apprend jamais le Lien**, `no-referrer` s'en charge. Le clic sur le lien de virement reste néanmoins comptable — il se mesure chez nous, avant la navigation, dans le canal anonyme. C'est le renoncement que cet ADR croyait devoir consentir et qui n'était pas dû.
- **Une ouverture de Cadeau ne se compte jamais sur un `GET` du document.** Quand un Lien est collé, la messagerie récupère la page pour construire l'aperçu, et cette requête est indiscernable d'une ouverture réelle. Un compteur naïf déclencherait « ouvert par le destinataire » dans la seconde où l'Offrant colle le lien.
- **Les balises `og:` sont les premières du `<head>`**, avant tout script et toute feuille de style : les robots des messageries ne lisent que le début du document.
- **Une seule image de partage existe pour tous les Cadeaux**, hachée et `immutable` sur le domaine R2 public. Elle ne montre aucun décor.
- **Le Lien ne passe jamais en paramètre d'URL**, y compris dans un futur outil d'assistance ou de diagnostic : un paramètre finit dans les référents et les journaux beaucoup plus facilement qu'un chemin.
