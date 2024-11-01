import requests
from fastapi import FastAPI
import dotenv
import os

# carrega o arquivo .env
dotenv.load_dotenv(".env") 
# busca pela variavel de ambiente
token = os.environ["API_TOKEN"] 

def get_json(url: str) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = requests.get(url, headers=headers)
    return data.json()

app = FastAPI()

@app.get("/movies") # http :8000/movies
def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=vote_count.desc&primary_release_year=2010"
    data = get_json(url)
    results = data['results']
    titles = []  # inicializa a lista
    for mov in results:
        titles.append(
            { 
                'title': mov['title'], 
                'release': mov['release_date'] 
            }
        )  
    return titles

@app.get("/generos")
def get_genres():  # (3)
    """ 
    endpoint: https://api.themoviedb.org/3/genre/movie/list
    lista todos os generos (tipos de filmes) disponíveis no tmdb 
    """
    url = "https://api.themoviedb.org/3/genre/movie/list"
    return get_json(url)

# (1) localhost:8000/artista/arnold
# (2) localhost:8000/artista?nome=arnold
@app.get("/artista/{nome}") # (1)
def get_artista(nome: str):
    """ 
    Procura um artista pelo nome. Retornar os seguintes campos:
        "gender"
        "id"
        "name"
        "popularity"
        "profile_path"
    
    https://api.themoviedb.org/3/search/person
    """
    url = ""
    data = get_json(url)
    # ... extrai os campos
    person = {}
    return person

def get_movie(title: str): # (2)
    """ procura um filme pelo titulo """
    ...

def get_elenco(title: str): # (4)
    """ retorna o nome de todos os artistas de um filme """
    ...
