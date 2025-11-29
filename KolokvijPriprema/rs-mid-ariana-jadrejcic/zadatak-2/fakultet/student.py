from fakultet.podaci import razredi_studenti

class Student:
    def __init__(self, ime: str, prezime: str, razred: str, kolegij_ocjene: dict):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.kolegij_ocjene = kolegij_ocjene

    def prosjek_ocjena(self) -> float:
        ocjene = [x for x in self.kolegij_ocjene.values()]
        if len(ocjene) == 0:
            return 0.0
        return round(sum(ocjene)/len(ocjene), 1)
  
    def promjena_razreda(self, novi_razred: str) -> None:
        if any(x["razred"] == novi_razred for x in razredi_studenti):
            self.razred = novi_razred
        else:
            raise ValueError(f"Razred {novi_razred} nije dopusten")
            
