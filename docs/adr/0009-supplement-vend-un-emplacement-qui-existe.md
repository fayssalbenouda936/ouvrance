# Un Supplément vend un Emplacement qui existe

Le plafond du Quota d'une Formule est une **borne dure**, jamais un palier tarifaire. Il ne peut pas dépasser le nombre d'Emplacements substituables que la mise en scène de l'Expérience porte réellement : le braquage en porte dix, donc le Jeu Premium plafonne à dix Souvenirs et une Commande ne peut pas coûter plus de 84,99 €.

Aucun Supplément ne se vend au-delà, à aucun prix.

## Pourquoi

Parce que **vendre un onzième Souvenir serait vendre une place qui n'existe pas**. Le Souvenir serait payé et jamais rencontré — l'ADR-0003 interdit le trou dans la mise en scène ; ceci en est le retournement, un contenu payé sans mise en scène pour le porter.

Le palier tarifaire était le choix concurrent, et il était tentant pour une raison précise : le périmètre à deux Formules a fait disparaître Extra et Ultime, donc **le plafond chargé est le seul endroit du catalogue où un chiffre supérieur à 69,99 € peut encore s'afficher**. Il est écarté parce qu'il ferait dépendre le prix de ce que le décor peut tenir : la mise en scène de la prochaine Expérience deviendrait alors une décision tarifaire, ce qu'ADR-0002 a construit le catalogue pour éviter en séparant le Quota, commercial et porté par la Formule, de l'Emplacement, scénique et porté par l'Expérience.

La séparation d'ADR-0002 tient donc, mais elle prend ici une contrainte d'ordre : le Quota est libre **sous** le nombre d'Emplacements, jamais au-dessus.

## Conséquences

- **Toute Expérience publiée sous une Formule porte au moins autant d'Emplacements substituables que le plafond de cette Formule.** La porte de publication au catalogue le vérifie ; une Expérience qui n'en porte pas assez ne se publie pas sous cette Formule.
- **Le montant d'une Commande est borné par construction.** Le nombre de Souvenirs est plafonné au schéma Zod et le montant est revérifié contre le plafond de la Formule côté serveur : aucune Commande ne peut être forgée au-dessus du prix maximum de sa Formule.
- **Relever un plafond est une décision de conception avant d'être une décision de prix.** On ne vend pas onze Souvenirs sans avoir d'abord accroché un onzième cadre.
- **L'ancre haute du catalogue est perdue et ne revient pas par ce chemin.** Le prix maximum n'apparaît que dans le formulaire, après la décision d'achat. C'est la contrepartie assumée du périmètre à deux Formules.
- **Baisser le nombre d'Emplacements d'une Expérience déjà publiée casse le Quota vendu.** Le tracé du niveau est, sur ce point précis, un engagement commercial.
