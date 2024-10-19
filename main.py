from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"Hello": "World"}

# define o endpoint /horacerta que retorna a hora
@app.get("/horacerta")
def horacerta():
    from datetime import datetime
    d = datetime.now()
    return f"{datetime.time(d)}"

# banco de dados...
db = {
    "br": { "name": "Brasil", "capital": "Brasilia" },
    "ar": { "name": "Argentina", "capital": "Buenos Aires" }
}
# http :8000/pais/br -b
@app.get("/pais/{sigla}")
def get_pais(sigla: str):
    pais = db[sigla]
    return pais

# http :8000/frase -b
@app.get("/frase")
def get_quotes():
    import requests
    url = "https://zenquotes.io/api/today"
    response = requests.get(url) # retornar apenas a chave "q"
    return response.json()

# uvicorn main:app --reload
# uvicorn main:app --reload --port=5000