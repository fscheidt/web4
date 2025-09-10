from pydantic import BaseModel, computed_field

class User(BaseModel):
   id: int
   name: str
   email: str
   # campo opcional:
   avatar: str | None = None


class Movie(BaseModel):
   id: int
   title: str
   genre_ids: list | None = None
   genres: list | None = None
   original_title: str
   original_language: str | None = None
   overview: str
   popularity: float
   poster_path: str | None = None
   release_date: str
   vote_average: float
   vote_count: int

   @computed_field
   @property
   def poster_url(self) -> str:
      return f"https://image.tmdb.org/t/p/w185{self.poster_path}"


class Genre(BaseModel):
   id: int
   name: str
   @computed_field
   @property
   def label(self) -> str:
      return self.name.replace(" ","-").lower()
