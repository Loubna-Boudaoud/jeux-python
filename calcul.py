
import random
score = 0


for i in range(10):
    a = random.randint(2, 10)
    b = random.randint(2, 10)

    reponse = int(input(f"Question {i + 1} : {a} x {b} = "))

    if reponse == a * b:
        print("Juste.")
        score += 1
    else:
        print(f"Faux ! La bonne réponse était {a * b}.")
        

print(f"Score : {score}/10.")
if score == 10:
    print("Parfait !")
elif score >= 7:
    print("Très bien !")
elif score >= 5:
    print("Pas mal !")
else:
    print("Révisez vos tables !")
    
