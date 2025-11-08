import proizvodi
import narudzbe

proizvodi_za_dodavanje = [
{"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
{"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for proizvod in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(proizvodi.Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"]))

for stavka in proizvodi.skladiste:
    stavka.ispis()

naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 1},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
    {"naziv": "Tipkovnica", "cijena": 200, "narucena_kolicina": 3}
]

narudzba = narudzbe.napravi_narudzbu(naruceni_proizvodi)
narudzba.ispis_narudzbe()