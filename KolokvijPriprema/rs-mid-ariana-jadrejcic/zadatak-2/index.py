from fakultet import podaci as p
from fakultet import student as s

lista_studenata = []

for razred in p.razredi_studenti:
    for student in razred["studenti"]:
        novi_student = s.Student(
            student["ime_prezime"].split(" ", 1)[0],         
            student["ime_prezime"].split(" ", 1)[1],
            razred["razred"],
            {kolegij["naziv"] : kolegij["ocjena"] for kolegij in student["kolegiji"]}
        )
        lista_studenata.append(novi_student)

for student in lista_studenata:
    print(f"Student:  {student.ime} {student.prezime}, Razred: {student.razred}, Kolegiji i ocjene: {student.kolegij_ocjene} ")
    print(f"Prosjek: {student.prosjek_ocjena()}")


lista_studenata[0].promjena_razreda("1B")
print(lista_studenata[0].razred)
lista_studenata[0].promjena_razreda("1C")