import requests
import dotenv
import os
from pycine.models import Movie, MovieResults

dotenv.load_dotenv(".env") 
token = os.environ["API_TOKEN"] 

def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()

# url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"


def get_movie(id: int):
    """ Obtem o filme pelo ID """
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    data = get_json(url)
    movie = Movie.model_validate(data)
    return movie


def search_movies():
    """ Busca filmes usando filtros """
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "include_adult": False, 
        "include_video": False,
        "language": "en-US", 
        "page": 1,
        "sort_by": "popularity.desc"
    }
    search_result = get_json(url, params)
    return MovieResults.model_validate(search_result)
