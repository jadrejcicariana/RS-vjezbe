#funkcije viseg reda

#koristeci funkciju map, kvadrirajte duljine svih nizova u listi
#map(function, iterables)
nizovi = ["jabuka", "kruska", "banana", "naranca"]
kvadrirane_duljine = list(map(lambda x : len(x) ** 2, nizovi))
print(kvadrirane_duljine)

#koristeci fju filter, filtrirajte samo brojeve koji su veci od 5
#filter(function, iterables)
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = (list(filter(lambda x : x > 5, brojevi)))
print(veci_od_5)

#rezultat kvadriranja svih brojeva u listi gdje rezultat mora biti rjecnik gdje su kljucevi
#originalni brojevi, a vrijednosti kvadrati tih brojeva
brojevi = [10, 5, 12, 15, 20]
transform = dict(zip(brojevi, list(map(lambda x : x**2, brojevi))))
print(transform)

#koristeci all i map, provjerite jesu li svi studenti punoljetni
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda x : x["godine"]>17, studenti))
print(svi_punoljetni)

#definirajte var min_duljina koja ce pohranjivati min duljinu rijeci int.
#pohranite u var duge_rijeci sve rijeci iz liste koje su dulje od min_duljina
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
min_duljina = input("Unesite minimalnu duljinu riječi: ")

duge_rijeci = list(filter(lambda x : len(x)>int(min_duljina), rijeci))
print(duge_rijeci)