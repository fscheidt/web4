from pydantic import BaseModel

class User(BaseModel):
   id: int
   name: str
   email: str
   # campo opcional:
   avatar: str | None = None

class Movie(BaseModel):
   id: int
   original_title: str
   genre_ids: list
   overview: str
   popularity: float
   poster_path: str | None = None
   title: str
   release_date: str
   vote_average: float
   vote_count: int
