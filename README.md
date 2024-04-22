
# RCR_FormulePropositionnelle

## Description
Ce projet académique consiste en un analyseur syntaxique pour un langage propositionnel. L'objectif est de vérifier si une formule propositionnelle donnée est valide ou non.

## Fonctionnalités
- **Analyse Syntaxique :** 
- **Vérification de Validité :**
- **Satisfiabilité :** Il vérifie si la formule est satisfiable,
## Bibliothèques Utilisées
- `re` : Pour utiliser des expressions régulières dans la détection des atomes.
- `sympy` : Pour créer et manipuler des expressions symboliques et effectuer des opérations logiques.

## Utilisation
Pour exécuter le programme, exécutez le fichier `main.py` en utilisant Python. Vous serez invité à entrer une formule propositionnelle à analyser. Le programme affichera ensuite si la formule est valide et, le cas échéant, toute erreur détectée.

## Exemples
Vous pouvez utiliser les exemples fournis dans le fichier `main.py` pour tester le programme. Voici quelques exemples :

- `p and (q or not r)`
- `p if q iff r`
- `not p iff r`
