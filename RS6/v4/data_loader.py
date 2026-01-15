import json
from typing import List
from models.film import Film

def load_movies(path: str = "data/film.json") -> List[Film]:
    with open(path, encoding="utf-8") as f:
        movies = json.load(f)
    return [Film(**m) for m in movies]