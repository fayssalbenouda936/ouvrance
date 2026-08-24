# La personnalisation est une liste ordonnée de Souvenirs

L'unité que l'offrant dépose n'est pas un fichier, c'est un **Souvenir** : un support — une photo **ou** une phrase, jamais les deux — auquel un vocal peut se greffer. Un vocal n'existe jamais seul. La personnalisation d'une expérience est la **liste ordonnée** de ces Souvenirs, et cet ordre est celui dans lequel le destinataire les rencontre.

## Pourquoi

Parce que le modèle concurrent — trois familles indépendantes, tant de photos, tant d'audios, tant de phrases — comptait des fichiers là où le destinataire vit des rencontres. Neuf médias éparpillés produisent neuf effleurements ; cinq Souvenirs produisent cinq arrêts. Une photo seule est une image ; la même photo avec la voix de la personne et l'anecdote qui va avec est le moment où le destinataire s'arrête.

La règle du support unique n'est pas une restriction arbitraire : elle est diégétique. Une toile montre une chose. Elle porte une photo ou elle porte une phrase écrite ; elle ne fait pas les deux sans cesser d'être crédible comme œuvre. Le vocal, lui, n'est pas sur la toile — il se déclenche à l'approche, donc il se greffe sans contradiction.

L'ordre a été ajouté pour une raison distincte, née du chiffrage de la durée. Le braquage dure six à huit minutes réparties sur cinq salles. Un garnissage qui remplit d'abord les meilleurs emplacements tasse tous les Souvenirs d'un cadeau modeste dans les deux premières salles, et le destinataire joue la seconde moitié — celle qui monte en tension — dans un musée entièrement impersonnel. L'ordre existe pour que la courbe soit la même quel que soit le quota : un début, un milieu, une fin.

## Conséquences

- **Le quota compte des Souvenirs**, plus des fichiers par type. La grille tarifaire change de dénomination : cinq Souvenirs inclus, dix au plafond.
- **Une expérience doit porter autant d'emplacements de Souvenir que le plafond de sa formule**, conformément à l'ADR-0002. Le braquage en porte dix, répartis deux par salle — cinq Souvenirs, c'est un par salle ; dix, c'est deux.
- **Le garnissage étale avant de densifier.** Le premier Souvenir de la liste tombe dans la première salle, et ainsi de suite. Ce n'est pas un algorithme de placement : c'est une contrainte de conception de niveau, et elle se vérifie à la publication au catalogue.
- **Le formulaire doit être réordonnable**, et dire à l'offrant ce que l'ordre signifie. « Le premier est celui qu'on découvre en entrant. »
- **Le plus fort se met en premier.** Le destinataire a une minute pour comprendre que ce musée parle de lui ; passé ce délai il joue à un jeu d'infiltration quelconque.
- **Les emplacements non garnis portent leur contenu par défaut**, sans exception — l'ADR-0003 est intact, et le musée ne change ni de taille ni de durée selon le quota.
- Le schéma de personnalisation reste **propre à chaque expérience** et validé par Zod. Le Souvenir est la forme qu'il prend pour le braquage ; une carte animée n'a aucune raison de l'adopter.
