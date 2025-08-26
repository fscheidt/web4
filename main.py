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


@app.get("/movies/top")
def get_top_ranked_movies():
    from tmdb.service import MovieService
    movies = MovieService.get_top_rated()
    # movies = MovieService.get_top_rated(page=2)
    return movies

# Documentação dos endpoints:
# localhost:8000/docs

# iniciar o servidor pelo terminal:
# uvicorn main:app --reload
