from utils import is_valid

def verification(formula):
    # Vérifier la validité de la formule
    valid, error = is_valid(formula)
    # Afficher le résultat
    if valid:
        print(f"La formule  propositionnelle  :'{formula}' est valide.")
    else:
        print(f"La formule propositionnelle  :'{formula}' n'est pas valide. Erreur : {error}")


formula = input("Veuillez entrer une formule propositionnelle : ")
verification(formula)
# verification('p and (q or not r)')  # Doit imprimer: True
# verification('p and q')  # Doit imprimer: True
# verification('(p and q))')  # Doit imprimer: False
# verification('p and q')  # Doit imprimer: True
# verification('p if q iff r')  # Doit imprimer: True
# verification('(p if q ) iff r')  # Doit imprimer: True
# verification('q iff r')  # Doit imprimer: True
# verification('not p iff r')  # Doit imprimer: True