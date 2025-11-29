from data.razredi_studenti import razredi_studenti

#1.2

def dohvati_studente_iz_razreda(razredi_studenti: list, naziv_razreda: str) -> list:
    for razred in razredi_studenti:
        if razred["razred"] == naziv_razreda:
            studenti = [student["ime_prezime"] for student in razred["studenti"]]
    return studenti
            
print(dohvati_studente_iz_razreda(razredi_studenti, "1B"))

#1.3

def prosjek_studenta(razredi_studenti: list, ime_prezime: str) -> float:
    for razred in razredi_studenti:
        for student in razred["studenti"]:
            if student["ime_prezime"] == ime_prezime:
                ocjene = [kolegij["ocjena"] for kolegij in student["kolegiji"]]
                return sum(ocjene)/len(ocjene)  
    
    return None

print(prosjek_studenta(razredi_studenti, "Ana Horvat")) 

#1.4

print([(razred["razred"], len(razred["studenti"])) for razred in razredi_studenti])

#1.5

lista = [student["ime_prezime"] for razred in razredi_studenti for student in razred["studenti"] if razred["razred"] == "1B"]
print(lista)