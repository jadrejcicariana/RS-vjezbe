class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print({
            "naziv" : self.naziv, 
            "cijena" : self.cijena, 
            "dostupna kolicina" : self.dostupna_kolicina,
            })
        
    
skladiste = [Proizvod("mobitel", 800, 70), Proizvod("zvucnik", 60, 50)]

def dodaj_proizvod(proizvod):
    skladiste.append(proizvod)