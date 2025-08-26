import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(".env"))
TOKEN = os.environ["TMDB_TOKEN"]
import requests
from rich import print

def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()


class MovieService:
    @staticmethod
    def get_top_rated(page:int = 1):
        url = "https://api.themoviedb.org/3/movie/top_rated"
        params = {
            "language": "en-US",
            "page": page
        }
        data = get_json(url, params)
        return data
    
    @staticmethod
    def get_movie(id: int):
        """ dados do filme pelo id """
        # 218 
        pass
