#funkcije

#fja koja vraca ntorku s privm i zadnjim elementom liste u jednoj liniji koda
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

print(prvi_i_zadnji(lista))

#fja koja vraca ntorku s maksimalnim i minimalnim elementom liste, bez koristenja min i max
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
def min_i_max(lista):
    najmanji = lista[0]
    najveci = lista[0]
    
    for broj in lista:
        if broj < najmanji:
            najmanji = broj
        if broj > najveci:
            najveci = broj
    
    return (najveci, najmanji)

print(min_i_max(lista))

#fja presjek koja prima dva skupa i vraca novi skup s elementima koji se nalaze u oba skupa
skup1 = {1, 2, 3, 4, 5}
skup2 = {4, 5, 6, 7, 8}

def presjek(skup1, skup2):

    novi_skup = skup1.intersection(skup2)
    
    return novi_skup

print(presjek(skup1, skup2))
