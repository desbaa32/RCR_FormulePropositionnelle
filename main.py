from utils import is_valid, is_satisfiable, is_entailed

kb = ["p and (q or not r)", "p and q", "p if q iff r", "a and b", "a and not p"]

# Définir la formule alpha à vérifier
alpha = "p and not q"

def verif_deduction(alpha):
    # Vérifier si KB entraîne alpha
    result = is_entailed(kb, alpha)
    # Afficher le résultat
    if result:
        print(f" \n KB |= {alpha}")
    else:
        print(f"\n KB ne entraîne pas {alpha}")



print("Par defaut voici notre Base de connaissance : \n ['p and (q or not r)', 'p and q'', 'p if q iff r', 'a and b'', 'a and not p'] \n")
print("----_____Verification:une formule α découle de l' ensemble KB----_______")
alpha = input("Veuillez entrer une formule propositionnelle: ")

verif_deduction(alpha)
