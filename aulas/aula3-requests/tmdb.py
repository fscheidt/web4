import requests
"""
ENDPOINT:
https://api.themoviedb.org/3/discover/movie
"""
# (1) Define o EndPoint da requisição
url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

# substituir este token:
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDg5OTAwYzE0M2M3ZWM2OTUyYzg2MTE0YzgzYTAzMSIsIm5iZiI6MTcyOTg5NDczNC43ODU5OTk4LCJzdWIiOiI2NzFjMTk0ZTVkMGRlODkwNDJkOTIzMTAiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.wgXsmVmwXALCOZEcSARO6rPUnarJgSN_IcWrN6pO0FE"
# (2) cabeçalho da requisição HTTP onde é passado parâmetros de configuração para a API
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}" # define o token da autorização
}
# (3) realiza a requisição HTTP (GET) para o endpoint
response = requests.get(url, headers=headers)
# (4) response é a resposta retornada pelo servidor armazenada no objeto response
print(response.json())

# Executar o script:
# python3 tmdb.py
