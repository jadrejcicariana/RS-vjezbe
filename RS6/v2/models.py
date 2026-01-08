from pydantic import BaseModel
from datetime import datetime
from typing import List, Literal, TypedDict

#1
class Izdavac(BaseModel):
    naziv: str
    adresa: str
    
class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    god_izdavanja: int = 2026
    br_str: int
    izdavac: Izdavac

#2
class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Literal["dodavanje", "brisanje", "azuriranje", "citanje"]] = []

#3
class Stol_info(TypedDict):
    broj: int
    lokacija: str

class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float

class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: Stol_info
    lista_jela: list[Jelo]
    ukupna_cijena: float

#4
class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: tuple[float, float] = (0.0, 0.0)

