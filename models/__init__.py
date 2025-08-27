from pydantic import BaseModel

class User(BaseModel):
   id: int
   name: str
   email: str
   # campo opcional:
   avatar: str | None = None

class Movie(BaseModel):
   id: int
   genre_ids: list | None = None
   original_title: str
   overview: str
   popularity: float
   poster_path: str | None = None
   release_date: str
   title: str
   vote_average: float
   vote_count: int
