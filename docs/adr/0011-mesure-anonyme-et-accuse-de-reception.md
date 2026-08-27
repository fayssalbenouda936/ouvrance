# La mesure ignore qui, l'accusé de réception ignore tout le reste

Un Cadeau est observé par **deux canaux disjoints**, et la disjonction est la décision :

- **L'accusé de réception** sait de quel Cadeau il s'agit et n'apprend que **deux dates sans heure** : `premiere_ouverture_le` et `termine_le`, écrites sur le Cadeau lui-même. L'écriture de la première est idempotente.
- **La mesure** apprend tout du parcours — étape atteinte, issue, échecs de lecture — et **ne porte aucun identifiant** : ni Lien, ni Lien condensé, ni identifiant de Commande, ni IP, ni chaîne de User-Agent, ni horodatage plus fin que la journée.

**Rien n'est écrit sur le terminal du Destinataire** : ni cookie, ni `localStorage`, ni IndexedDB, ni empreinte. Aucun outil tiers de mesure d'audience n'est installé. Le stockage est **deux tables D1** ; l'observabilité d'exploitation est celle, native, de Cloudflare.

**Un Lien n'apparaît jamais dans un journal**, et la route `/cadeau/[lien]` sert `Referrer-Policy: no-referrer`.

## Pourquoi

**Le canal nommé est pauvre parce qu'un accusé de réception n'a pas besoin d'être riche.** Le statut existe d'abord pour ouvrance : un Cadeau payé qui ne s'ouvre pas doit être visible, sinon on ne peut ni le réparer ni le rembourser. Le montrer à l'Offrant est un usage second du même fait, et c'est cette hiérarchie des finalités qui fait tenir l'intérêt légitime — là où l'ADR sur le droit à l'image l'écartait, parce qu'y existait une solution moins intrusive évidente. Ici il n'y en a aucune : on ne peut pas demander à un Destinataire si la vidéo a démarré.

L'appauvrissement est **à l'écriture, pas à l'affichage**. Stocker un horodatage pour l'arrondir au moment de le montrer laisse l'heure exposée à la première réquisition, au premier bogue, à la première fonctionnalité ajoutée par quelqu'un qui ignorait la règle. La date est ce qu'on stocke.

**Le canal anonyme n'a pas d'identifiant parce qu'un identifiant pseudonyme n'est pas anonyme.** Condenser le Lien, ou condenser l'IP et le User-Agent comme le font les outils sans cookie du marché, produit une donnée personnelle qui a seulement l'air de ne pas en être. On n'en met pas.

**Rien sur le terminal, parce que l'article 82 de la loi Informatique et Libertés se déclenche à l'écriture, pas au traitement.** N'écrire rien met hors champ au lieu d'exempter, et supprime le bandeau de consentement. Ce bandeau tomberait sur l'écran d'ouverture d'un cadeau, avant le cadeau, sous forme de fenêtre modale à deux boutons puisque refuser doit être aussi simple qu'accepter. C'est le moment le plus fragile du produit. On refuse le bandeau en refusant ce qui le rend nécessaire.

Le fait technique va dans le même sens : `setDomStorageEnabled` vaut `false` par défaut en WebView Android, donc un identifiant de mesure côté client serait silencieusement cassé sur les liens ouverts depuis TikTok et WhatsApp — exactement le trafic qui compte.

**Aucun outil tiers, parce que chaque outil est un sous-traitant, une ligne d'AIPD, une ligne de politique de confidentialité et un script sur l'écran d'amorce**, pour un entonnoir qui vit à l'intérieur d'une seule page et d'un canevas WebGL, à un volume où une requête SQL bat un tableau de bord. Cloudflare est conservé parce qu'il héberge déjà et voit déjà chaque requête : sa surface juridique marginale est nulle.

## Conséquences

- **L'Offrant voit trois états et une date** : « pas encore ouvert », « ouvert le J », « terminé le J ». Jamais d'heure, jamais un compteur de réouvertures, jamais une progression étape par étape, jamais de temps réel. Règle de tranchage pour les cas futurs : *l'Offrant n'apprend rien qu'il n'apprendrait en demandant au Destinataire.*
- **Le clic sur le lien de virement est mesuré dans le canal anonyme et n'est jamais montré à l'Offrant.**
- **« Ouvert » s'écrit au tap sur « Toucher pour commencer », pas au GET de la page** : les robots d'aperçu de WhatsApp, iMessage et Signal récupèrent l'URL et marqueraient l'ouverture à l'envoi du SMS.
- **L'énumération des étapes est déclarée par l'expérience**, dans le registre déjà posé pour la Personnalisation. Le noyau ne connaît pas les salles.
- **L'échec de lecture se détecte par le rejet de la promesse `play()`**, complété d'un chien de garde sur `currentTime` : aucune API ne signale le mode économie d'énergie.
- **Dériver puis jeter, au bord** : le moteur d'exécution est réduit à une énumération de cinq valeurs avant écriture ; la chaîne User-Agent et l'IP ne sont jamais stockées.
- **Aucun échantillonnage.**
- **Le point de terminaison de mesure est public et non authentifié** : son schéma n'accepte aucune chaîne libre, seulement des énumérations fermées, et il est limité en débit au bord.
- **Conservation** : 13 mois de lignes de mesure puis destruction, compteurs mensuels agrégés conservés sans limite ; les deux dates vivent et meurent avec le Cadeau. **Une troisième date échappe à ce régime** : la dernière ouverture, écrasée à chaque fois, dont dépend l'extinction du Cadeau. Elle ne peut pas être effacée sur opposition sans tuer le Cadeau, et elle trahit qu'il y a eu réouverture — ce que les deux autres taisent. Elle se déclare comme telle dans la politique de confidentialité, au titre du cycle de vie et non de la mesure.
- **Droit d'opposition effectif** : les dates sont effacées et l'Offrant lit « le destinataire a demandé que ce cadeau ne soit pas suivi », jamais « pas encore ouvert ».
- **On renonce aux entonnoirs par session, à l'identité inter-sessions et à tout tableau de bord livré.** Les chiffres se lisent en SQL, écrit à la main.
- **À faible volume, la table de mesure n'est pas anonyme par les mathématiques** : un jour à un seul Cadeau ouvert la rend réidentifiable. Ce qui la défend est la pauvreté de son contenu, pas le k-anonymat.
