#obrnite rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivic", "dob": 25}

def obrni_rjecnik(rjecnik):
    obrnuti_rjecnik = {}
    for kljuc, vrijednost in rjecnik.items():
        obrnuti_rjecnik[vrijednost] = kljuc
    return obrnuti_rjecnik

print(obrni_rjecnik(rjecnik))