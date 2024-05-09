import itertools
import re

import sympy
from sympy import symbols, sympify, satisfiable


#Verification de la validite:parenthese et syntaxe
def is_valid(formula):
    # Vérifier les parenthèses
    stack = []
    for char in formula:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False, "Parenthèses déséquilibrées",None
    if stack:
        return False, "Parenthèses déséquilibrées",None
    # Extraire les atomes et les connecteurs logiques à l'aide d'expressions régulières
    atoms = set(re.findall(r'\b[a-zA-Z]\w*\b', formula))
    connectors = {
        'not': '~',
        'and': '&',
        'or': '|',
        'if': '>>' ,#->',
        'iff': '<<'#'^'
    }
    for connector in sorted(connectors, key=len, reverse=True):
        formula = formula.replace(connector, connectors[connector])

    # Créer des symboles pour chaque atome et les stocker dans un dictionnaire
    vars_dict = {atom: symbols(atom) for atom in atoms}

    # Essayer de convertir la formule en une expression sympy
    try:
        expr = sympify(formula, locals=vars_dict)
        return True, None,expr
    except Exception as e:
        return False, str(e),None

#Verification de la satistifiablite du formule
def is_satisfiable(expFormule):
    result=satisfiable(expFormule, all_models=False)
    if result:
        print("La formule  est satisfaisable.")
        print(f" Valeurs atomes pour la rendre vraie :{result}")
    else:
        print("La formule  n'est pas satisfaisable.")

#Verification de la validte et satistifiablite du formule
def verification_validte_satisfiablite(formula):
    # Vérifier la validité de la formule
    valid, error, formuleExp = is_valid(formula)
    # Afficher le résultat
    if valid:
        print(f"La formule  propositionnelle  :'{formula}' est valide.")
        # Vérifier la satisfiablite  de la formule
        is_satisfiable(formuleExp)
        return valid, error, formuleExp
    else:
        print(f"La formule propositionnelle  :'{formula}' n'est pas valide. Erreur : {error}")
        return None,None,None

# Base de connaissance KB :verification formule et  convertion en expression sympy
def is_kb_valid_expSympy(kb):
    atoms = set()
    formulKb = []
    for formula in kb:
        valid, error, expr = is_valid(formula)
        if not valid:
            raise ValueError(f"Formule invalide dans KB : {formula}")
        formulKb.append(expr)
        atoms.update(expr.atoms(sympy.Symbol))
    return formulKb, atoms
# formule aplha:verification formule et  convertion en expression sympy
def is_alpha_valid_expSympy(atoms,alpha):
    valid, error, alphaExp = verification_validte_satisfiablite(alpha)
    if(valid!=None and error !=None and alphaExp!=None ):
        alpha_atoms = alphaExp.atoms(sympy.Symbol)
        if not atoms.issuperset(alpha_atoms):
            print(f"La formule a des atomes qui ne sont pas dans la base de connaissance KB : {alpha_atoms - atoms}")
            return None
        return alphaExp
    else:
        return None

 #Vérifier si KB entraîne α en utilisant la méthode des tables de vérité"""
def is_entailed(kb, alpha):
    # Convertir les formules en expressions sympy
    kb_expr, atoms = is_kb_valid_expSympy(kb)
    alpha_expr = is_alpha_valid_expSympy(atoms,alpha)

    # Générer toutes les combinaisons possibles de valeurs de vérité pour les atomes
    truth_values = list(itertools.product([True, False], repeat=len(atoms)))

    # Évaluation formules de KB et alpha pour les combinaison de valeurs de vérité
    kb_true = []
    for values in truth_values:
        substitutions = dict(zip(atoms, values))
        kb_true.append(all(expr.subs(substitutions) for expr in kb_expr))
        if all(kb_true):
            if alpha_expr.subs(substitutions):
                return True

    return False