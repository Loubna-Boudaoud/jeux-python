#import random
#nombre = random.randint(1, 100)
secret = 42

nombre = int(input("Entrez un nombre entre 1 et 100 : "))

if nombre > secret:
    print("c'est plus.")
elif nombre < secret:
    print("c'est moins.")
else:
    print("c'est gagné !")