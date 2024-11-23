from fastapi import FastAPI
app = FastAPI()
import pycine.tmdb as tmdb
from fastapi.middleware.cors import CORSMiddleware
"""
# Iniciar fastapi (main.py) no servidor uvicorn:

source env/bin/activate
uvicorn main:app --reload
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
def hello():
    return {"status": "pycine is running"}

@app.get("/movie/{id}")
def get_movie(id: int):
    return tmdb.get_movie(id)

@app.get("/search/movies")
def search_movies():
    """
    Filmes mais populares
    http :8000/search/movies
    """
    params = {
        "sort_by": "vote_count.desc"
    }
    # results = tmdb.search_movies() # shawshaw
    results = tmdb.search_movies(params) # inception
    return results

@app.get("/movies/top")
def search_movies():
    """
    # Retorna os 20 filmes mais populares
    """
    results = tmdb.search_movies()
    return results