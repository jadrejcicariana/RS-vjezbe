from pydantic import BaseModel, Field, HttpUrl, field_validator
from typing import List, Literal, Optional
from models.actor import Actor
from models.writer import Writer
import re

class Film(BaseModel):
    ComingSoon: Optional[bool] = False
    Title: str
    Year: int = Field(ge=1900)
    Rated: str
    Released: Optional[str] = None
    Runtime: int = Field(ge=0)
    Genre: str
    Director: Optional[str] = None
    Writer: List[Writer]
    Actors: List[Actor]
    Plot: str
    Language: str
    Country: str
    Awards: Optional[str] = None
    Poster: Optional[HttpUrl] = None
    Metascore: Optional[int] = None
    imdbRating: float = Field(0.0, ge=0, le=10)
    imdbVotes: int = Field(1, ge=0)
    imdbID: Optional[str] = None
    Type: Literal["movie", "series"]
    Response: Optional[bool] = True
    Images: List[HttpUrl] = []

    @field_validator("Year", mode="before")
    def parse_year(cls, v):
        if isinstance(v, int):
            return v

        match = re.findall(r"\d{4}", v)
        if match:
            return int(match[0])
        
    @field_validator("Runtime", mode="before")
    def parse_runtime(cls, v):
        if v == "N/A":
            return 0
        return int(re.findall(r"\d+", v)[0])
    
    @field_validator("imdbRating", mode="before")
    def parse_rating(cls, v):
        if v == "N/A":
            return 0.0
        return float(v)
    
    @field_validator("imdbVotes", mode="before")
    def parse_votes(cls, v):
        if v == "N/A":
            return 1
        return int(v.replace(",", ""))
    
    @field_validator("Metascore", mode="before")
    def parse_metascore(cls, v):
        if v == "N/A":
            return None
        return int(v)
    
    @field_validator("Actors", mode="before")
    def parse_actors(cls, v):
        return [
            Actor(
                name = a.strip().split(" ", 1)[0],
                surname = a.strip().split(" ", 1)[1]
            )
            for a in v.split(",")
        ]
    
    @field_validator("Writer", mode="before")
    def parse_writers(cls, v):
        writers = []
        for w in v.split(","):
            name = w.split("(")[0].strip()
            parts = name.split(" ", 1)
            writers.append(
                Writer(
                    name = parts[0],
                    surname = parts[1]
                )
            )
        return writers
