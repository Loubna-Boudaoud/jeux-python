import random
secret = random.randint(2, 10)
a = random.randint(2, 10)
b = random.randint(2, 10)
question = int(input(f"{a} x {b} = "))
if question == a * b:
    print("Bravo !")
else:
    print(f"Perdu ! La bonne réponse était {a * b}")