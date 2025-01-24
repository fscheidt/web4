import os
import dotenv
from fastapi import FastAPI, status, Body
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
    response_description="List all movies stored in atlas cloud",
    response_model=models.MovieCollection,
    # response_model_by_alias=True,
    response_model_by_alias=False,
)
async def list_movies():
    movies_collection = db.get_collection("movies")
    result = models.MovieCollection(
        movies=await movies_collection.find().to_list(20)
    )
    print(result)
    return result


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


# SAVE Movie no banco de dados (collection: pycine.movies)
@app.post("/save/",
    response_model=models.Movie,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def save_movie(movie: models.Movie = Body(...)):
    movies_collection = db.get_collection("movies")
    movie.is_fav = True
    # TODO: fazer validação para evitar dupla inserção do mesmo movie
    new_movie = await movies_collection.insert_one(
        movie.model_dump(by_alias=False, exclude=["id"])
    )
    created_movie = await movies_collection.find_one(
        {"_id": new_movie.inserted_id}
    )
    return created_movie


# DELETE Movie de pycine.movies
@app.get("/remove/",
    response_description="Remove movie by id",
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def remove_movie(id: str):
    movies_collection = db.get_collection("movies")
    deleted_id = await movies_collection.delete_one({'_id': id})
    return deleted_id