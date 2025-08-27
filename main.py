from fastapi import FastAPI
app = FastAPI()

"""
BACKEND (SERVIDOR)
"""

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


# Documentação dos endpoints:
# localhost:8000/docs

# iniciar o servidor pelo terminal:
# uvicorn main:app --reload
