#import random
#nombre = random.randint(1, 100)
secret = 42
proposition = 0
coups = 0


while proposition != secret:
    proposition = int(input("Entrez un nombre entre 1 et 100 : "))
    coups += 1
    if proposition > secret:
        print("c'est plus.")
    elif proposition < secret:
        print("c'est moins.")
    else:
        print("c'est gagné !")
print(f"Bravo, trouvé en {coups} coups !")
