# Le jeton de suivi lit, l'email écrit

Le jeton de `/suivi/[jeton]` reste un porteur qui vit et meurt avec le Cadeau, et il ne donne que la **lecture** : les trois états, la date sans heure, le Lien, le bouton « signaler un problème ».

**Changer le Lien de virement exige une preuve de possession fraîche de la boîte de l'Offrant.** Le bouton « changer mon lien de virement » n'ouvre pas un champ : il envoie, à l'adresse enregistrée sur la Commande, un **lien d'écriture à usage unique valable trente minutes**. C'est lui qui autorise l'écriture, jamais le jeton de suivi.

Trois règles fermes l'entourent, et sans elles la preuve ne prouve rien :

- **L'adresse email de l'Offrant n'est modifiable depuis aucune surface porteuse** — ni `/suivi`, ni le lien d'écriture. Elle se change en écrivant à ouvrance, et cela seulement.
- **Le jeton de suivi se remplace, il n'expire pas.** L'email de notification porte un « ce n'est pas moi » qui, en un clic, restaure la valeur précédente du Lien de virement, émet un jeton neuf, révoque l'ancien et invalide les liens d'écriture en attente.
- **`/suivi/[jeton]` porte les protections d'URL du Lien** (ADR-0015) : `Referrer-Policy: no-referrer`, `noindex` en balise **et** `X-Robots-Tag`, segment de chemin et jamais chaîne de requête.

## Pourquoi

**Parce que le vecteur n'est pas celui qu'on protégeait.** Le jeton n'arrive pas par le Lien : il arrive par l'email « votre cadeau est prêt », donc il vit dans la boîte de l'Offrant et nulle part ailleurs. Le Destinataire ne l'a jamais eu. Il ne fuit donc que de deux façons — la boîte est compromise, ou l'email est **transféré**. Le second cas n'est pas une hypothèse d'école : cet email porte aussi le Lien, et « tiens, voilà le lien » est exactement ce qu'un Offrant fait avec. Un dispositif qui ne traite pas le transfert ne traite rien.

**Parce que la notification après coup ne défend que le cas où elle est inutile.** Contre une boîte compromise, elle arrive dans la boîte de l'attaquant, qui l'efface. Contre un transfert, elle arrive bien chez l'Offrant — mais après, et le Destinataire a pu virer entre-temps. Elle est un bon instrument de constat et un mauvais instrument de prévention ; on la garde pour ce qu'elle fait.

**Parce que la confirmation par email avant effet est la bonne idée dans la mauvaise forme.** Elle défend précisément le transfert : celui qui détient le jeton n'a pas la boîte, donc il ne confirme pas. Mais posée comme une deuxième étape après le formulaire, elle fait payer l'aller-retour à *tous* les gestes légitimes en gardant un jeton d'écriture qui, lui, continue de vivre deux ans. **La retourner coûte le même aller-retour et supprime le jeton d'écriture** : la capacité d'écrire n'est plus une chaîne qui a fuité il y a dix-huit mois, c'est la possession de la boîte à cet instant. Le geste que l'Offrant connaît déjà — un lien reçu par email — remplace un compte qu'ouvrance ne veut pas ouvrir.

**Parce que la friction invoquée n'existe pas au moment où elle compterait.** Le cas urgent est un lien Revolut périmé pendant que le Destinataire ouvre le cadeau. Mais un lien mort est mort de toute façon : trente secondes d'aller-retour ne sont pas ce qui décide, et l'ADR-0016 a déjà écarté la vraie cause en demandant le lien permanent plutôt que le lien de demande à sept jours.

**Parce que la liste close borne autre chose que ce qu'on croyait.** #28 la présentait comme empêchant de viser « un domaine de collecte inventé ». Ce n'est pas là qu'est sa force : un compte Revolut s'ouvre en dix minutes. Sa force est que Revolut, PayPal et Lydia sont des prestataires régulés qui vérifient l'identité — **le détournement reste possible, mais il est attribuable et le virement est traçable**, là où un domaine de collecte ne laisse rien. Elle borne l'impunité, pas la perte. Le dire ainsi évite de s'en contenter.

**Parce que la boîte compromise ne se défend pas d'ici, et qu'il faut l'écrire.** Aucun dispositif accessible à ouvrance — pas de compte, pas de mot de passe, pas de second facteur — ne résiste à un attaquant qui lit les emails de l'Offrant. Ce qui reste alors est la marche arrière en un clic et la trace en D1. C'est la limite honnête du dispositif, et c'est la même que celle de tout produit sans compte.

**Parce que la victime n'est pas le client.** #13 avait pesé le dégât maximal d'un Lien détenu par un tiers à un remboursement — une perte qu'ouvrance porte, sur une personne qui a contracté avec elle. Ici la perte est celle du **Destinataire**, qui n'a rien signé, n'a pas de compte, et ne peut rien vérifier. C'est cette asymétrie qui paie l'aller-retour, pas une estimation de la probabilité de l'attaque : à cinq cadeaux vendus, cette probabilité est proche de zéro et ne justifierait rien.

## Conséquences

- **Le jeton de suivi vit aussi longtemps que le Cadeau** et meurt à l'Extinction avec le reste. La question de sa durée est close : ce n'est pas la durée qui était le problème, c'est le pouvoir.
- **Le lien d'écriture est à usage unique et à trente minutes**, il n'ouvre que le champ `lien_virement`, contre la même liste close et le même schéma Zod qu'au dépôt. Rien d'autre du Cadeau n'est atteignable, depuis aucune des deux surfaces.
- **L'email de notification nomme l'ancienne et la nouvelle valeur en clair** — service et identifiant, pas seulement « votre lien a changé ». Un Offrant ne reconnaît pas une substitution qu'on ne lui montre pas.
- **Pas de délai d'effet, pas de plafond d'un changement par jour.** Les deux coûtent au geste légitime et ne rapportent rien une fois l'écriture liée à la boîte : celui qui tient la boîte attend quelques heures, et celui qui ne la tient pas n'écrit jamais.
- **Un lien d'écriture ne s'émet plus sur un Cadeau éteint**, et `/suivi` d'un Cadeau éteint ne montre aucun Lien de virement, ancien ou neuf.
- **La Récompense montre l'adresse en clair** — le service et l'identifiant du compte, jamais un bouton nu. C'est la seule vérification qu'un Destinataire puisse faire lui-même : il reconnaît le nom de l'Offrant, ou il ne le reconnaît pas. La mise en page appartient à l'ADR-0016 et au lecteur, la lisibilité de l'adresse est une contrainte de sécurité.
- **Le trafic de `/suivi` n'entre pas dans le canal anonyme de l'ADR-0011.** C'est une surface d'Offrant identifié, pas un parcours de Destinataire ; l'y verser mélangerait les deux finalités que cet ADR sépare.
- **Le jeton de suivi n'apparaît jamais dans un journal**, au même titre que le Lien. La page `/suivi` affiche le Lien : qui tient l'un tient l'autre, et les deux méritent donc le même traitement.
