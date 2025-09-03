import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(".env"))
TOKEN = os.environ["TMDB_TOKEN"]
import requests
from models import Movie, Genre
import json

def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()


class MovieService:

    @staticmethod
    def get_genres() -> list[Genre]:
        filepath = "data/genres.json"
        with open(filepath) as f:
            data = json.load(f)
        data = data['genres']
        genres = [Genre.model_validate(g) for g in data]
        return genres
    

    @staticmethod
    def find_by_id(id: int) -> Movie:
        """ 
        Obtem os dados de um filme pelo id 
            endpoint: /movie/{id}
        """
        url = f"https://api.themoviedb.org/3/movie/{id}"
        params = {
            "language": "en-US",
        }
        movie = get_json(url, params)
        movie = Movie.model_validate(movie)
        return movie
    
    
    @staticmethod
    def get_top_rated(page:int = 1) -> list[Movie]:
        """
        Obtem a lista de filmes melhores rankeados
            endpoint: /movie/top_rated
        """
        url = "https://api.themoviedb.org/3/movie/top_rated"
        params = {
            "language": "en-US",
            "page": page
        }
        data = get_json(url, params)
        results = data['results']
        movies = [Movie.model_validate(m) for m in results ]
        return movies
