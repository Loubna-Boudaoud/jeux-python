
import random

score_joueur = 0
score_ordi = 0

while score_joueur != 3 and score_ordi != 3:
    nombre = random.randint(1, 3)

    if nombre == 1:
        ordinateur = "pierre"
    elif nombre == 2:
        ordinateur = "feuille"
    else:
        ordinateur = "ciseaux"

    joueur = input("Choisis pierre, feuille ou ciseaux : ")

    print("L'ordinateur :", ordinateur)

    if ordinateur == joueur:
        print("Égalité !")

    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "feuille" and ordinateur == "pierre") or \
         (joueur == "ciseaux" and ordinateur == "feuille"):
        print("Vous avez gagné !")
        score_joueur += 1

    else:
        print("L'ordinateur a gagné !")
        score_ordi += 1

    print("Score : vous", score_joueur, 
          ", Ordinateur :", score_ordi)

if score_joueur == 3:
    print("Bravo ! Vous avez gagné la partie !")
else:
    print("L'ordinateur a gagné la partie !")

