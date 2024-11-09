from fastapi import FastAPI
app = FastAPI()
import pycine.tmdb as tmdb

@app.get("/")
def hello():
    return {"status": "pycine is running"}

@app.get("/movie/{id}")
def get_movie(id: int):
    return tmdb.get_movie(id)

@app.get("/search/movies")
def search_movies():
    params = {
        "sort_by": "vote_count.desc"
    }
    # results = tmdb.search_movies() # shawshaw
    results = tmdb.search_movies(params) # inception
    return results
