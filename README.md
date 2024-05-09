
# RCR_FormulePropositionnelle

## Description
Ce projet académique consiste en une vérification de la validité et  a la satisfiablite d'une formule propositionnel. Il permet de verifier si une formule  peut être déduite d'un ensemble de formules (base de connaissances) autrement dit si une formule α découle d'un ensemble de formules KB,où KB est une base de connaissances contenant un nombre fini de formules du langage sous-jacent.On a utilise la methode des table de verite.

## Fonctionnalités
- **Analyse Syntaxique :** 
- **Vérification de Validité :**
- **Satisfiabilité :** Il vérifie si la formule est satisfiable,
- **Déduction:**  Vérifie si une formule peut être déduite d'un ensemble de formules (base de connaissances) en utilisant la méthode des tables de vérité.
## Fichiers
- `utils.py : `Fichier contenant  l'ensemble des fonctions
- `main.py:` fichier principale a executer
## Bibliothèques Utilisées
- `re` : Pour utiliser des expressions régulières dans la détection des atomes.
- `sympy` : Pour créer et manipuler des expressions symboliques et effectuer des opérations logiques.
- `itertools `: Pour générer toutes les combinaisons possibles de valeurs de vérité pour les variables propositionnelles.

## Utilisation
Pour exécuter le programme, exécutez le fichier `main.py` en utilisant Python. Vous serez invité à entrer une formule propositionnelle.Il sagit la du formule α  a verifier si elle est deduit de KB. Le programme affichera ensuite si le resultat, le cas échéant, toute erreur détectée.

## Exemples
Vous pouvez utiliser les exemples fournis dans le fichier `main.py` pour tester le programme. Voici quelques exemples :
- `p and (q or not r)`
- `p if q iff r`
- `not p iff r`
- `Base de connaissances KB par defaut`: ['p and (q or not r)', 'p and q', 'p if q iff r', 'a and b', 'a and not p']
