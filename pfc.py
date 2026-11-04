

import random
nombre = random.randint(1, 3)

if nombre == 1:
    ordinateur = "pierre"
elif nombre == 2:
    ordinateur = "feuille"
else:
    ordinateur = "ciseaux"


joueur = input("Choisis pierre, feuille ou ciseaux : ")


print("L'ordinateur :", ordinateur)
print("Le joueur :", joueur)

