# Les Souvenirs de la carte vivent sur la feuille

Les Emplacements de la carte animée sont sur la **page de droite de la feuille**, en **quinconce** : une colonne de polaroïds alternée gauche-droite, légèrement de travers, qui remplit la hauteur de la page. Leur taille est **dérivée** de la place réellement disponible, jamais écrite en pourcentage. Il n'y a pas de table, et il n'y a pas de bande de décor.

Cet ADR remplace la **mesure** de l'ADR-0018, dont il conserve entièrement le **mécanisme**.

## Pourquoi

L'ADR-0018 a compté six places sur *« deux bandes de décor d'un rang chacune, trois polaroïds par rang »*, relevées autour d'une feuille au rapport 1,16. Ces bandes n'existent pas : la feuille livrée est à **0,89** (ADR-0024) et elle occupe l'écran. Le décor sur lequel l'ADR-0018 posait ses polaroïds est ce que le film montre, pas ce que la lettre laisse libre.

Le défaut qu'il corrigeait, lui, était réel : les photos centrées verticalement sur la page de droite laissaient **21 % de blanc en haut et 32 % en bas**. Déménager sur la table était une façon de le résoudre. Le quinconce en est une autre, choisie sur planche comparative de cinq dispositions, et elle le résout sur la feuille : **0 % en haut, 10 % en bas**. Elle est en production depuis le 29/08 et elle est partie chez un client.

Le quinconce garde en plus ce que la table perdait. Un Souvenir posé sur la table est à côté de la lettre ; un polaroïd posé sur la page de droite est **dans** la lettre, avec sa légende sous lui, et c'est ce que l'ADR-0004 appelle une liste ordonnée de Souvenirs qu'on parcourt. La personnalisation diégétique du braquage a son équivalent ici : la carte ne pose pas des photos autour d'un texte, elle est un album ouvert.

## Conséquences

- **La taille d'un polaroïd est dérivée, jamais écrite.** Elle dépend de la hauteur de la page — donc de la longueur de la lettre — et du nombre de Souvenirs. Elle tombe à **73 px** sur la lettre de Sirine, quatre photos et 584 caractères. Un pourcentage en dur serait juste pour une lettre et faux pour la suivante.
- **Le plancher de 64 px tient**, et c'est ce qui survit de [#30](https://github.com/fayssalbenouda936/ouvrance/issues/30) : sous 64 px de côté, un visage n'en est plus un. Les 73 px livrés le respectent avec 9 px de marge.
- **La capacité de la carte n'est plus une constante : elle dépend du message.** C'est le fait neuf, et l'ADR-0018 ne l'avait pas — sur une table, six places sont six places quelle que soit la lettre. Une capacité qui bouge avec la longueur du texte ne se vend pas telle quelle : l'ADR-0009 exige qu'un Supplément vende un Emplacement qui existe. Le plafond de la Carte Animée est donc à re-mesurer **sur le pire cas**, ou à garantir par une borne sur le message. Ticket ouvert : [Le plafond de la Carte Animée, re-mesuré sur le quinconce](https://github.com/fayssalbenouda936/ouvrance/issues/47).
- **Le garde-fou de l'ADR-0018 reste le bon** : la Récompense — donc le lien de virement — doit rester dans le cadre. C'est lui qui borne le quinconce par le bas, comme il bornait la table.
- **Le mécanisme de l'ADR-0018 est intact.** Le plafond d'une formule reste le minimum des capacités mesurées de ses expériences, la capacité reste déclarée par l'expérience et non déduite du code de mise en page, et la porte de publication au catalogue continue de la vérifier. Seuls le chiffre et la mise en scène sur laquelle il a été relevé changent.
