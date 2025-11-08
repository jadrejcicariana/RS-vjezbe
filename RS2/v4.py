#klase i objekti
from datetime import datetime
import math

class Automobil:
    def __init__ (self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print({
            "marka" : self.marka, 
            "model" : self.model, 
            "godina proizvodnje" : self.godina_proizvodnje,
            "kilometraza" : self.kilometraza,
            "starost": self.starost()
            })
    
    def starost(self):
        return (datetime.now().year-int(self.godina_proizvodnje))
    
auto = Automobil("fiat", "punto", "1999", "300000")
auto.ispis()

class Kalkulator:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        return self.a / self.b
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        return (math.sqrt(self.a), math.sqrt(self.b))
    
calc = Kalkulator(16, 9)
print(calc.korijen())


class Student:
    def __init__ (self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene)/len(self.ocjene)

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [
    Student(
        student["ime"], 
        student["prezime"], 
        student["godine"], 
        student["ocjene"]
        ) for student in studenti]

najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())
print(najbolji_student.ime)

class Krug:
    def __init__ (self, r):
        self.r = r

    def opseg(self):
        return math.pi*2*self.r
    
    def povrsina(self):
        return math.pi*(self.r**2)
    
obj = Krug(3)
print(obj.opseg(), obj.povrsina())

class Radnik:
    def __init__ (self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__ (self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"radim na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje


rad = Radnik("ivo", "strojar", 1000)
rad.work()
man = Manager("luka", "menadzer", 2000, "proizvodnja")
man.work()

##radnik dobiva povisicu
print(f"stara placa: {rad.placa}")
man.give_raise(rad, 200)
print(f"nova placa: {rad.placa}")

