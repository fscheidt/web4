from fastapi import FastAPI, status, Body  # <=
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# -------------------------------------
import motor
from motor import motor_asyncio
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(".env"))
# carrega credenciais de acesso ao cloud atlas:
db_url = os.environ["MONGODB_URL"] 
client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
# db => objeto representa a base de dados:
db = client.sample_mflix  # <= nome do database
# -------------------------------------

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


@app.get("/mflix/users/find")
async def mflix_list_users():
    """ base de dados: sample_mflix | collection: users """
    collection = db.get_collection("users")
    results = await collection.find().to_list(20)
    results = [user['name'] for user in results]
    return results


@app.get("/mflix/movies/find")
async def mflix_find_movies(max_rows: int=5):
    """ base de dados: sample_mflix | colection: movies """
    collection = db.get_collection("movies")
    # Seleciona apenas os campos: title e year
    # results = await collection.find({}, {"title": 1, "year": 1, "_id": 0}).to_list(max_rows)
    # Todos os campos (exceto _id)
    # SELECT * from movies LIMIT 5
    results = await collection.find({}, {"_id": 0}).to_list(max_rows)
    # TODO: "$gt"
    # SELECT * from movies LIMIT 5 WHERE year > 1910
    return results

@app.post("/mflix/users/save",
    status_code=status.HTTP_201_CREATED,
)
async def save_user(user: dict = Body(...)):
    """ adiciona um novo usuario na collection users """
    collection = db.get_collection("users")
    # INSERT INTO users values...
    created_user = await collection.insert_one(user)
    print("result %s" % repr(created_user.inserted_id)) # printa o id gerado
    # faz uma consulta para obter o usuario adicionado
    user_added = await collection.find_one({"_id": created_user.inserted_id}, {"_id": 0})
    return user_added  # <= retorna o novo usuario 


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

# ---------------------------
# Documentação dos endpoints:
# ---------------------------
# localhost:8000/docs

# ---------------------------------
# iniciar o servidor pelo terminal:
# ---------------------------------
# uvicorn main:app --reload
