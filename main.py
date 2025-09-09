from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

"""
BACKEND (SERVIDOR)
"""
origins = [
   "http://localhost",
   "http://localhost:*",
   "http://localhost:5173",
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)


@app.get("/")
def hello() -> dict:
    return { "menssage": "Web IV backend" }


@app.get("/movies/top")
@app.get("/movies/top/{page}")
def get_top_ranked_movies(page: int = 1):
    from tmdb.service import MovieService
    movies = MovieService.get_top_rated(page)
    return movies


@app.get("/movie/{id}")
def get_movie(id: int):
    from tmdb.service import MovieService
    movie = MovieService.find_by_id(id)
    return movie


@app.get("/genres")
def get_genres():
    from tmdb.service import MovieService
    genres = MovieService.get_genres()
    return genres


# Documentação dos endpoints:
# localhost:8000/docs

# iniciar o servidor pelo terminal:
# uvicorn main:app --reload
