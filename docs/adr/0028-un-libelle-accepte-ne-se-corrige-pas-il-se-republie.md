# Un libellé accepté ne se corrige pas, il se republie

Les conditions générales, la politique de confidentialité et les trois libellés de cases forment **un seul jeu, publié d'un bloc et daté**. Chaque version publiée garde une adresse figée que rien ne réécrit ; la commande stocke l'identifiant de cette version et l'horodatage de l'acceptation — un identifiant, pas trois.

## Pourquoi

Parce qu'un horodatage qui pointe vers une page modifiable ne prouve rien du tout.

L'ADR-0009 exige que chaque case soit horodatée « avec la version exacte du libellé », faute de quoi le renoncement à la rétractation est invérifiable. L'ADR-0010 fait de l'email de confirmation le **support durable** sans lequel ce renoncement n'est pas opposable — et cet email cite les libellés verbatim. Les pièces comptables, elles, vivent dix ans. Un identifiant écrit en 2026 doit donc se résoudre en un texte lisible en 2036, sinon toute la chaîne se contente de dire qu'un client a accepté quelque chose.

**Un identifiant et non trois**, parce que trois autoriseraient une commande acceptant des CGV de septembre avec des libellés de case d'août. Ce n'est pas une combinaison qu'on veut pouvoir décrire, encore moins défendre : les trois textes se lisent ensemble, la case renvoie aux pages et les pages expliquent la case. Ils se publient donc ensemble ou pas du tout.

Ces textes sont du **catalogue** au sens de l'ADR-0026 — ils ne varient pas par commande — donc ils vivent en code et se déploient. C'est le calendrier de disponibilité qui vit en D1 parce qu'il change sans déploiement ; des CGV qui changeraient sans déploiement seraient exactement le problème.

## Conséquences

- **On ne corrige plus une coquille en place.** Toute retouche, si mince soit-elle, produit une nouvelle version datée. C'est le coût, et c'est aussi le mécanisme : un texte qui peut bouger en silence ne peut pas servir de preuve.
- **Chaque version reste servie à son adresse propre**, l'adresse nue renvoyant à la dernière. Une commande de 2026 se relit à sa version de 2026, y compris longtemps après que le cadeau a été éteint et ses dérivés détruits (ADR-0019).
- **La commande porte deux champs de plus** : l'identifiant de version et l'horodatage. Ils rejoignent les trois entiers de prix que l'ADR-0009 y fait figer, et pour la même raison — une pièce se recalcule depuis la commande, jamais depuis ce qui est en vigueur le jour où on la relit.
- **La version en vigueur régit la commande jusqu'au bout.** Une mise à jour publiée après un paiement ne s'applique pas à ce paiement, et les CGV le disent elles-mêmes. Sans cette phrase, republier reviendrait à modifier rétroactivement des contrats en cours.
- **Les mentions légales ne sont pas dans le jeu.** Personne ne les accepte ; elles se corrigent en place, et elles doivent l'être vite quand l'hébergeur change de nom.
