from fastapi import APIRouter, HTTPException, Query
from models.film import Film
from typing import List, Optional
from data_loader import load_movies

router = APIRouter(prefix="/movies")

movies: List[Film] = load_movies()

@router.get("/", response_model=List[Film])
def get_movies(
    min_year: Optional[int] = Query(None, ge=1900),
    max_year: Optional[int] = Query(None, ge=1900),
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[str] = Query(None, regex="^(movie|series)$")
):
    result = movies

    if min_year is not None:
        result = [m for m in result if m.Year >= min_year]
    if max_year is not None:
        result = [m for m in result if m.Year <= max_year]
    if min_rating is not None:
        result = [m for m in result if m.imdbRating >= min_rating]
    if max_rating is not None:
        result = [m for m in result if m.imdbRating <= max_rating]
    if type is not None:
        result = [m for m in result if m.Type == type]

    return result

@router.get("/{imdb_id}", response_model=Film)
def get_movie_by_id(imdb_id: str):
    for movie in movies:
        if movie.imdbID == imdb_id:
            return movie
    raise HTTPException(status_code=404, detail="movie not found")

@router.get("/title/{title}", response_model=Film)
def get_movie_by_title(title: str):
    for movie in movies:
        if movie.Title.lower() == title.lower():
            return movie
    raise HTTPException(status_code=404, detail="movie not found")
