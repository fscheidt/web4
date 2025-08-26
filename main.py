from fastapi import FastAPI
app = FastAPI()

"""
BACKEND (SERVIDOR)
"""

@app.get("/")
def hello() -> dict:
    return { "menssage": "Web IV backend" }


@app.get("/now")
def datetime_now():
    """
    request this endpoint: 
        http://localhost:8000/now
    """
    from datetime import datetime
    return {
        "datahora": datetime.now(),
        "pais": "BR"
    }

# comando para iniciar o servidor no terminal:
# uvicorn main:app --reload
