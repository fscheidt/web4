import requests # pip install requests
from rich import print  # pip install rich
"""
   ENDPOINT: /breeds/list/all
"""
url = "https://dog.ceo/api/breeds/list/all"

# cabeçalho da requisição HTTP
headers = { "accept": "application/json" }
# realiza a requisição HTTP (GET) para o endpoint
response = requests.get(url, headers=headers)
# response é a resposta retornada pelo servidor
print(response.json())

# python3 dogs.py