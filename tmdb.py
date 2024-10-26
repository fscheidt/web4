import requests
from fastapi import FastAPI
app = FastAPI()
token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MzY1M2RlMjY0M2Y1NTFhMWVkZDM5NzdkMGJiYzFmMSIsIm5iZiI6MTcyOTg5NTA2My44NTc2MTMsInN1YiI6IjY3MWMxOTRlNWQwZGU4OTA0MmQ5MjMxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AvFqk2ZVFqzZHjD1wAdsh-H3v8m1QlyfwgfgGqQXpTc"
@app.get("/movies") # localhost:8000/movies
def get_movies():
    """ faz requests para a API TMDB e obtem lista de filmes """
    # url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    # menos populares:
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.asc"
    # mais votados:
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=vote_count.desc&primary_release_year=2010"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    # Faz a requisição GET
    data = requests.get(url, headers=headers)
    data = data.json()
    # extrai o array "results" do json
    results = data['results']
    # extrai o primeiro filme do array
    # movie = results[0]
    titles = []  # inicializa a lista
    for m in results:
        # adiciona o titulo + release do filme
        titles.append(
            m['title'] + " - " + m['release_date']
        )  
    return titles

def get_artista(nome: str): # (1)
    """ procura um artista pelo nome """
    # https://api.themoviedb.org/3/search/person
    # nome = "Arnold"
    # fazer request
    ...
def get_movie(title: str): # (2)
    """ procura um filme pelo titulo """
    ...
def get_genres():  # (3)
    """ lista todos os generos disponíveis no tmdb """
    ...
def get_elenco(title: str): # (4)
    """ retorna o nome de todos os artistas de um filme """
    ...
