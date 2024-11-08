import requests
import dotenv
import os
from pycine.models import Movie
dotenv.load_dotenv(".env") 
token = os.environ["API_TOKEN"] 

def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()

def get_movie(id: int):
    """ Obtem o filme pelo ID """
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    data = get_json(url)
    movie = Movie.model_validate(data)
    return movie
