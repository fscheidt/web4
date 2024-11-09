from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: int
    title: str
    genres: Optional[list] = None
    original_language: str
    overview: str
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    release_date: str
    vote_count: Optional[int] = None

class MovieResults(BaseModel):
    """ usar quando o endpoint retorna uma lista de filmes """
    page: int
    results: list[Movie]
    total_pages: int
    total_results: int

class Person(BaseModel):
    """ atributos para mapear do json:
    id
    name
    biography
    birthday
    deathday
    gender
    known_for_department
    place_of_birth
    popularity
    profile_path
    """
    ...
