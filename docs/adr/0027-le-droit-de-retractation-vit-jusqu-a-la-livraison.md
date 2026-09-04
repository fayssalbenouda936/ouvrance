# Le droit de rétractation vit jusqu'à la livraison

Les conditions générales de vente écrivent que l'offrant peut annuler sa commande **sans motif et remboursé intégralement jusqu'à la livraison**, alors même que la loi autorisait à éteindre ce droit dès le paiement. La case de renoncement reste au formulaire, obligatoire ; elle ne mord qu'à l'instant où le lien est remis.

## Pourquoi

Parce que le droit qu'on aurait pu retirer ne coûte rien, et que ce qu'il achète n'est pas remplaçable.

L'article L221-28 13° du Code de la consommation éteint le droit de rétractation d'une fourniture de contenu numérique **dès que l'exécution a commencé**, à condition d'un accord préalable exprès et d'un renoncement exprès. ouvrance recueille les deux. Rien n'empêchait donc d'écrire que le droit meurt à l'encaissement, ni de le faire mourir à l'ouverture de la commande par l'atelier — le premier geste où ouvrance dépense sa ressource rare.

Le coût de ne pas le faire est mesuré, et il est ridicule. Une commande annulée avant livraison coûte **1,39 € de frais Stripe** non restitués (ADR-0009) et, au pire, **3,7 minutes de validation**, sur un trafic réel de **cinq commandes par mois** (ADR-0026). En face, le quatrième panneau de l'entonnoir doit faire accepter 69,99 € à quelqu'un qui n'a jamais entendu parler de la marque et qui arrive de TikTok : « annulable sans motif jusqu'à la livraison » est la seule réassurance forte qui reste une fois l'ancre haute perdue avec les formules Extra et Ultime.

La raison décisive est ailleurs, et elle est de cohérence. L'ADR-0026 fait partir un email le lendemain d'une date promise manquée, qui **propose le remboursement intégral**. Si le droit de rétractation mourait au paiement, cette proposition serait une faveur — révocable, et révocable exactement au moment où quelqu'un vient de rater son occasion. En le laissant vivre jusqu'à la livraison, le remboursement de retard **est la loi** : le cadeau n'étant pas livré, le droit n'est pas éteint. On ne promet pas deux fois la même chose par deux mécanismes dont l'un peut être retiré.

## Conséquences

- **Le libellé de la case reste celui écrit pour le ticket RGPD, mot pour mot.** Il disait déjà « une fois le cadeau livré je ne pourrai plus exercer mon droit de rétractation » — plus généreux que la loi, et c'est désormais délibéré au lieu d'être un heureux hasard. Il ne se réécrit pas sans réécrire cet ADR.
- **La clause est rédigée au régime le plus exigeant, sans nommer lequel s'applique.** La qualification « contenu numérique » ou « prestation de service » reste l'un des points renvoyés à une relecture juridique. Une clause calée sur la pleine exécution (L221-28 1°) satisfait mécaniquement le 13° ; l'inverse est faux. On écrit donc la plus stricte et on cesse d'attendre l'avocat pour vendre.
- **Livraison et validation sont le même instant.** Rien ne s'intercale : le lien naît de la validation, l'email qui le porte part du même événement. Le contrat dit « livraison » là où l'atelier dit « validation », et il n'existe aucune fenêtre entre les deux où le droit serait dans un état indéterminé.
- **La rétractation n'est pas l'extinction, et les CGV ne doivent jamais laisser les confondre.** La rétractation annule une commande avant livraison et rend tout. L'extinction détruit un cadeau déjà vécu à la demande d'une personne représentée et ne rend qu'au prorata sur vingt-quatre mois (ADR-0009, ADR-0019). Deux clauses, deux articles, deux formules de remboursement.
- **Ce qu'on accepte, nommé.** Un offrant peut laisser produire son cadeau entier et l'annuler une minute avant la livraison, ayant coûté quelques minutes de validation et les frais bancaires. À cinq commandes par mois, c'est indolore ; au-delà de deux cents, la fenêtre se rediscute — et pas avant, parce qu'un droit annoncé se retire beaucoup plus mal qu'il ne s'accorde.
- **Les frais bancaires ne reviennent jamais**, ni sur une rétractation ni sur un prorata. Le remboursement porte sur les sommes versées, et le processeur garde les siennes.
