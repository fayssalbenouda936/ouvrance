# Le film ne cale plus la feuille

La feuille de la carte animée est **centrée dans son écran**, sa **hauteur est libre**, et son corps de texte descend jusqu'à un plancher qui suit la largeur : `max(9, min(11, largeur × 0,026))`. Elle ne vise plus le cadrage où le film de dépliage la laisse. `RAPPORT_FILM` disparaît, et avec lui l'idée qu'une forme couchée s'achetait par un raccord.

## Pourquoi

Parce que ce raccord n'a jamais existé. Le legacy s'en réclamait dans ses commentaires — *« relevé sur l'image : x de 7 % à 93 %, y de 27 % à 69 % »* — et l'ADR-0018 a construit sur cette phrase. Elle décrit une mécanique que le code ne contient pas.

`ajusterAuFilm()` emprunte au film son **rapport**, et rien d'autre. La **position**, personne ne la calcule : `.cl-papier-couche` est un flex, la feuille est centrée par `margin:auto`. Mesuré sur la commande livrée le 29/08 à Sirine, à 390 × 844 : le film laisse son papier à l'écran entre y 303 et y 556, la feuille arrive à y 206 et finit à y 623. **97 px trop haut, 67 px trop bas.** Personne ne l'a jamais vu parce que `film.remove()` précède le fondu `cl-poser` : la dernière image du film n'est jamais tenue sous le papier, il n'y a rien à quoi comparer.

Le rapport lui-même n'est pas atteint non plus. `ajusterAuFilm()` réduit le texte jusqu'à retrouver le rapport visé, mais s'arrête au plancher de lisibilité — et ce plancher n'est pas une constante de 11 px, il suit la largeur et tombe à **9 px sur un téléphone**. Sur une vraie lettre il est atteint bien avant le rapport : la carte de Sirine sort à **0,89**, debout, quand la constante visait 1,16. **La carte animée ship debout depuis toujours, et personne ne l'a décidé.**

Enfin le chiffre écrit était faux, et il ne pouvait pas être juste : trois films de dépliage existent et laissent leur papier à trois cadrages différents — **1,16 écrit, 1,35 et 1,562 mesurés**. Un rapport relevé une fois à la main sur une image ne survit pas à la régénération d'un film, et le commentaire qui l'accompagnait le disait déjà (*« ⚠️ Si le film est régénéré, ce chiffre est à relever à nouveau »*). Un raccord qui exige qu'une constante soit re-relevée à chaque rendu maître est un raccord qu'on ne tiendra pas.

L'alternative sérieuse était de le construire pour de vrai : caler la feuille sur les quatre bords décodés sur la dernière image, et tenir cette image sous elle pendant le fondu. Elle est écartée parce que la carte livrée est belle sans, et que le fondu de 0,55 s suffit à faire la passe. On ne paie pas une contrainte de forme — une lettre couchée, illisible sans descendre à 9 px — pour un effet que personne n'a jamais vu manquer.

## Conséquences

- **La hauteur de la feuille est libre, et c'est la longueur de la lettre qui la fixe.** Le corps de texte ne se réduit plus pour atteindre une cible : il se réduit pour tenir dans l'écran, et le plancher est le seul garde-fou.
- **Le plancher de lisibilité dépend de la largeur, jamais d'une constante.** `max(9, min(11, largeur × 0,026))`. Un plancher fixe à 11 px produit sur un écran de 390 px une feuille en bande — rapport 0,53, 228 px de papier vide — ou, si on l'y force, un budget de message de 32 caractères. C'est ce dernier chiffre qui a fait croire à un plafond de 200 caractères ; la lettre livrée en porte **584**.
- **Toute mesure de la carte se relève sur le build livré, à 390 px, en `defaultViewport`.** Jamais `--window-size` : Chrome refuse de descendre sous ~500 px et rend 500 en silence. C'est cette taille qui a produit tous les chiffres faux du dépôt, celui de l'ADR-0018 compris.
- **Le raccord d'entrée est conservé et n'est pas concerné.** L'affiche du cadeau est la **première image** du film : au tap, l'écran ne change pas. Il est acquis, il marche, et il est indépendant de ce qui est abandonné ici. Sa seule dette : régénérer le film oblige à réextraire l'affiche.
- **« La feuille est couchée pour le raccord » sort du vocabulaire d'ouvrance.** La double page reste — son pli central est ce qui fait une carte plutôt qu'une page — mais elle ne se justifie plus par le film.
