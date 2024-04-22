import re
from sympy import symbols, sympify

# def Verifie_parentheses(formula):
#
def is_valid(formula):
    # Vérifier les parenthèses
    stack = []
    for char in formula:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False, "Parenthèses déséquilibrées"
    if stack:
        return False, "Parenthèses déséquilibrées"
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
        return True, None
    except Exception as e:
        return False, str(e)


