import os
import dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio
import pycine.tmdb as tmdb
from pycine import models

dotenv.load_dotenv(".env") 
db_url = os.environ["MONGODB_URL"] 

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
db = client.pycine  # banco de dados


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


@app.get("/find/",
    response_description="List all movies",
    response_model=models.MovieCollection,
    response_model_by_alias=False,
)
async def list_movies():
    movies_collection = db.get_collection("movies")
    return models.MovieCollection(
        movies=await movies_collection.find().to_list(20)
    )


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
