from fastapi import FastAPI
app = FastAPI()
import pycine.tmdb as tmdb
@app.get("/")
def hello():
    return {"status": "pycine is running"}

@app.get("/movie/{id}")
def get_movie(id: int):
    return tmdb.get_movie(id)
