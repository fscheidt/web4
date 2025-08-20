from fastapi import FastAPI
app = FastAPI()

"""
BACKEND (SERVIDOR)
"""

data = {
    55: "Brazil",
    20: "Egito",
    54: "Argentina"
}

# /country/55
@app.get("/country/{area}")
def country_area(area: int):
    if area in data:
        return {
            "area": area,
            "name": data[area]
        }

@app.get("/users")
def list_users():
    import json
    with open("users.json") as f:
        return json.load(f)


# /sortear/6/60
@app.get("/sortear/{quant}/{max}")
def sortear():
    # TODO :)
    pass

# DEFINIR O ENDPOINT
# http://localhost:8000/

@app.get("/")
def hello() -> dict:
    return { "mensagem": "Hello World" }


# http://localhost:8000/now
@app.get("/now")
def datetime_now():
    from datetime import datetime
    return {
        "datahora": datetime.now(),
        "pais": "BR"
    }


# uvicorn main:app --reload



