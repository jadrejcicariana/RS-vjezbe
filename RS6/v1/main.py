#uvicorn main:app --log-level info
#uvicorn main:app --reload
from fastapi import FastAPI
from models import Film, CreateFilm
from typing import List

filmovi = [
{"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
{"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
{"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
{"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

app = FastAPI()

@app.get("/filmovi", response_model=List[Film])
def dohvati_filmove(genre: str = None, min_godina: int = 2000):
    pronadeni = [
        film for film in filmovi 
        if (genre is None or film["genre"] == genre) 
        and (min_godina is None or film["godina"] >= min_godina)
        ]

    return pronadeni

@app.get("/filmovi/{id}", response_model=Film)
def dohvati_film(id: int):
    return next((film for film in filmovi if film["id"] == id), None)

@app.post("/filmovi", response_model=Film)
def dodaj_film(film: CreateFilm):
    new_id = max(film["id"] for film in filmovi) + 1 if filmovi else 1

    new_film = {
        "id": new_id,
        "naziv": film.naziv,
        "genre": film.genre,
        "godina": film.godina
    }

    filmovi.append(new_film)
    return new_film