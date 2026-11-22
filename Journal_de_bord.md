### Difficulté n°1 — Répartition des tâches et interdépendance des classes

L'une des premières difficultés rencontrées concerne l'organisation du travail au sein du groupe. En effet, bien que le projet puisse être décomposé en plusieurs parties (gestion des établissements, des joueurs, moteur de jeu, interface et intelligence artificielle), celles-ci ne sont pas totalement indépendantes.

Certaines fonctionnalités nécessitent l'utilisation de classes ou de méthodes développées par d'autres membres du groupe. Par exemple, la gestion des achats dépend des classes `Joueur`, `Ville` et `Reserve`, tandis que le moteur de jeu doit interagir avec les établissements pour appliquer leurs effets.

Ainsi, une répartition classique du travail, dans laquelle chaque membre développe entièrement une partie avant de réunir les différents codes, présente un risque de blocage : certains membres pourraient être contraints d'attendre que d'autres aient terminé leurs fonctionnalités pour pouvoir avancer.

Cette difficulté nous a amenés à réfléchir à une organisation permettant un développement en parallèle, tout en garantissant la cohérence et la compatibilité des différentes classes.

**Solution envisagée :** définir collectivement les responsabilités et les méthodes principales de chaque classe avant leur implémentation, puis organiser le développement de manière à limiter les dépendances bloquantes et faciliter l'intégration progressive du code.


Choix technique (Classe Partie) — Gestion de l'aléatoire et reproductibilité des tests

Problématique : Le moteur de Miniville repose notamment sur des lancers de dés aléatoires. Or, cette dimension aléatoire peut compliquer la vérification du bon fonctionnement des méthodes, puisqu'un même test peut produire des résultats différents selon les exécutions.

Solutions envisagées :Nous avons considéré deux approches :

random.seed() : fixer une graine pour rendre les résultats reproductibles. Cependant, cette méthode modifie l'état du générateur aléatoire global de Python.

random.Random(graine) : créer un générateur pseudo-aléatoire indépendant pour chaque instance de la classe Partie.
Choix retenu : Nous privilégions random.Random(graine), qui permet d'associer un générateur aléatoire indépendant à chaque partie, sans modifier celui utilisé globalement par Python.

Justification : Cette approche facilite la reproductibilité des tests et le débogage, tout en respectant les principes de la programmation orientée objet. Pour les situations précises, nous pourrons également imposer directement un résultat de dé lors des tests.
