from proizvodi import skladiste

narudzbe = []

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi = ', '.join(f'{proizvod["naziv"]} x {proizvod["narucena_kolicina"]}' for proizvod in self.naruceni_proizvodi)
        print(f"Naruceni proizvodi: {proizvodi}, ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(naruceni_proizvodi):

    if not isinstance(naruceni_proizvodi, list) or not naruceni_proizvodi:
        return None

    for proizvod in naruceni_proizvodi:

        if not isinstance(proizvod, dict):
            return None
        
        if not all(key in proizvod for key in ("naziv", "cijena", "narucena_kolicina")):
            return None

        zaliha = next((x for x in skladiste if x.naziv == proizvod["naziv"]))

        if not zaliha or zaliha.dostupna_kolicina < proizvod["narucena_kolicina"]:
            print(f'{proizvod["naziv"]} nije dostupan')
            return None
        
    ukupna_cijena = sum(proizvod["cijena"] * proizvod["narucena_kolicina"] for proizvod in naruceni_proizvodi)

    naruceno = (Narudzba(naruceni_proizvodi, ukupna_cijena))
    narudzbe.append(naruceno)
    return naruceno

