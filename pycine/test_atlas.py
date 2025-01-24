import dotenv
import os
from pprint import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from models import Movie

dotenv.load_dotenv(".env") 
db_url = os.environ["MONGODB_URL"] 

# Create a new client and connect to the server
client = MongoClient(db_url, server_api=ServerApi('1'))

print("="*40)

print("bases de dados encontradas:")
print(client.list_database_names())

print("="*40)

new_movie = {
  "id": 218,
  "title": "The Terminator",
  "genres": [
    { "id": 28, "name": "Action" },
    { "id": 53, "name": "Thriller" },
    { "id": 878,"name": "Science Fiction"}
  ],
  "is_fav": True,
  "original_language": "en",
  "overview": "In the post-apocalyptic future, reigning tyrannical supercomputers teleport a cyborg assassin known as the \"Terminator\" back to 1984 to kill Sarah Connor, whose unborn son is destined to lead insurgents against 21st century mechanical hegemony. Meanwhile, the human-resistance movement dispatches a lone warrior to safeguard Sarah. Can he stop the virtually indestructible killing machine?",
  "popularity": 74.305,
  "poster_path": "/qvktm0BHcnmDpul4Hz01GIazWPr.jpg",
  "release_date": "1984-10-26",
  "vote_count": 13194
}
# 1 define a base de dados
db = client.get_database('pycine')

# 2 obtem a collection (tabela) movies
movies_collection = db.get_collection('movies')

########
# CRUD
########

# DELETE ALL - faz drop de toda a tabela:
movies_collection.drop()

# DELETE - remove todos filmes com id 218
# res = movies_collection.delete_many({'id': 218})
# print(f"total deleted: {res.deleted_count}")

print("="*40)

# CREATE 
# equivalente ao sql INSERT INTO ...
# res = movies_collection.insert_one(new_movie)
print("saving movie")
# gera um objeto movie a partir de um dicionario python
movie = Movie.model_validate(new_movie)
res = movies_collection.insert_one(
    movie.model_dump(by_alias=False)
)
print(f"inserted id: {res.inserted_id}") # verifica o id gerado pelo banco
print(movie.model_dump())
print("="*40)

# READ (find) 
# equivalente ao SELECT * FROM ... WHERE 
resultado = movies_collection.find_one({'id': 218})
pprint(resultado)
