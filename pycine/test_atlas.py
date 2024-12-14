import pymongo
import dotenv
import os
dotenv.load_dotenv(".env") 
db_url = os.environ["MONGODB_URL"] 

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
client = MongoClient(db_url, server_api=ServerApi('1'))
print(client.list_database_names())

movie = {
    'id': 218,
    'title': 'Terminator',
    'genres': ['Action', 'Sci-fi'],
    'original_language': 'en-US'
}
# 1 define a base de dados
db = client.get_database('pycine')
# 2 obtem a collection (tabela) movies
movies_collection = db.get_collection('movies')
# CRUD
# CREATE 
# equivalente ao sql INSERT INTO ...
movies_collection.insert_one(movie)

# READ (find) 
# equivalente ao SELECT * FROM ... WHERE 
resultado = movies_collection.find_one({'id': 218})
from pprint import pprint
pprint(resultado)
