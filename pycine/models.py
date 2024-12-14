from pydantic import BaseModel
from typing import Optional
from bson import ObjectId
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
PyObjectId = Annotated[str, BeforeValidator(str)]

class Movie(BaseModel):
    # id: int
    # (id) é um alias para (_id) para manter o estado do objeto sincronizado com o database
    # No entento (id) no python por convenção
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    genres: Optional[list] = None
    original_language: str
    overview: str
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    release_date: str
    vote_count: Optional[int] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

# Classe para armazenar o resultado do find()
class MovieCollection(BaseModel):
    movies: list[Movie]


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
