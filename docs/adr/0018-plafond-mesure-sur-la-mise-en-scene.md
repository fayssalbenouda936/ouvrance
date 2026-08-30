# Le plafond d'une formule est ce que sa mise en scène supporte

> ⚠️ **La mesure de cet ADR est remplacée par l'ADR-0025.** Les six places étaient comptées sur les
> bandes de décor qu'une feuille au rapport 1,16 laissait libres ; la feuille livrée est à 0,89 et il n'y
> a pas de bande (ADR-0024). Les Souvenirs de la carte vivent sur la page de droite, en quinconce, et le
> plafond de la Carte Animée est à re-mesurer. **Le mécanisme ci-dessous — le plafond est le minimum des
> capacités mesurées, la capacité est déclarée par l'expérience, la porte de publication la vérifie —
> reste en vigueur.**

Le quota vit toujours sur la formule — c'est une promesse commerciale et elle n'a qu'un endroit. Mais sa valeur ne se choisit plus au tableau puis s'impose aux expériences : elle est **mesurée sur la mise en scène**, et deux formules n'ont aucune raison de porter le même plafond. La Carte Animée plafonne à **six** Souvenirs, le Jeu Premium à **dix**.

## Pourquoi

L'ADR-0002 faisait courir la flèche dans l'autre sens : la formule fixe un plafond, et « toute expérience publiée sous une formule doit pouvoir absorber le plafond de cette formule ». Il ajoutait que la contrainte serait faible en pratique, parce que chaque emplacement porte un contenu par défaut et qu'« ajouter des emplacements substituables coûte donc peu ». C'est vrai d'un musée : dix murs au lieu de six, c'est six œuvres de plus à générer une fois. Ce n'est pas vrai d'une carte.

La carte honore l'ADR-0003 par **omission** (ADR-0005) : il n'y a pas de contenu par défaut à ajouter, il y a une place physique à trouver sur un écran 9:16 qui ne s'agrandit pas. Mesuré sur un écran de 390 px, avec le cadrage où le film de dépliage laisse la feuille (rapport 1,16) : la table offre deux bandes de décor d'un rang chacune, trois polaroïds par rang, **six places**. Poser le septième, c'est le poser en travers de la lettre. Et forcer les dix sur la feuille fait passer celle-ci à 550 px sur un écran de 693, ce qui fait sortir la Récompense — donc le lien de virement — du cadre.

Deux plafonds, c'est donc la seule façon de garder la promesse vraie. Un plafond de dix vendu sur la carte aurait été une promesse que la mise en scène ne pouvait pas tenir, et le client l'aurait découverte après avoir payé 21 € de Supplément.

La contrepartie est réelle et elle porte sur la grille tarifaire : deux formules aux plafonds différents sont deux choses à expliquer au lieu d'une. On l'accepte parce que le rapport reste le même — trois inclus sur six pour la carte, cinq sur dix pour le braquage, les deux formules doublent — et parce que le plafond uniforme n'achetait sa simplicité qu'en mentant sur l'une des deux.

## Conséquences

- **La flèche de l'ADR-0002 s'inverse.** Le plafond d'une formule est le **minimum** des capacités mesurées de ses expériences. La contrainte « l'expérience doit absorber le plafond » reste vraie, mais elle est désormais satisfaite par construction plutôt que vérifiée après coup.
- **Publier une expérience sous une formule peut abaisser un plafond déjà vendu.** C'est le vrai danger de cette inversion, et il tombe sur la porte de publication au catalogue, qui vérifie déjà qu'un schéma de personnalisation est enregistré (ADR-0005) : elle vérifie en plus la capacité, et refuse une expérience dont la capacité est inférieure au plafond annoncé de la formule. Baisser un plafond est une décision tarifaire, jamais un effet de bord d'une publication.
- **La capacité est déclarée par l'expérience**, au même endroit que son schéma et la forme de sa greffe — pas déduite du code de mise en page.
- **Elle se mesure, elle ne s'estime pas.** La capacité de la carte a été relevée sur un prototype, à la largeur d'écran réelle et avec la police réelle. Le legacy avait relevé ses chiffres sur une fenêtre de 540 px et bridé son code à quatre photos sans que personne ne s'en aperçoive.
- **Carte Animée : 14,99 €, trois Souvenirs inclus, six au plafond, +3 € l'unité — 23,99 € au maximum.** Jeu Premium : inchangé, cinq inclus, dix au plafond.
