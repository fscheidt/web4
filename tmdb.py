import requests
"""
ENDPOINT:
https://api.themoviedb.org/3/discover/movie
"""
# (1) Define o EndPoint da requisição
url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

TMDB_TOKEN = "eyJhbGciOiJIUzI1NiJ9.blahblhba"
# (2) cabeçalho da requisição HTTP onde é passado parâmetros de configuração para a API
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_TOKEN}" # define o token da autorização
}
# (3) realiza a requisição HTTP (GET) para o endpoint
response = requests.get(url, headers=headers)
# (4) response é a resposta retornada pelo servidor armazenada no objeto response
print(response.text)

# Executar o script:
# python3 tmdb.py
