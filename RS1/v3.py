#pogadanje broja

import random
broj = random.randint(1, 100)
pokusaji = 0
broj_je_pogoden = False

while not broj_je_pogoden:
    pokusaj = int(input("Pogodi broj: "))
    pokusaji += 1
    if pokusaj < broj:
        print("broj je veci")
    elif pokusaj > broj:
        print("broj je manji")
    else:
        broj_je_pogoden = True
        print(f"Bravo, Pogodio si u {pokusaji} pokusaja.")