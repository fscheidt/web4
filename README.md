# Desenvolvimento Web IV

<details>
<summary>INFO DA DISCIPLINA</summary>

- **[AVA](https://ava.ifpr.edu.br/course/view.php?id=14063)**
- Curso: TADS
- Período: 4°
- Horário: terça, 19:00 às 22:20 (Lab 2)
- Período letivo: **2025/2**
- Aulas: 05/08/25 à dez/25
- **[Repositório](https://github.com/fscheidt/web4)**

</details>

## AULA 06 - FRONT
- 09/09
- [Svelte front-end](https://github.com/fscheidt/front)

## AULA 05 - TMDB
- 02/09

endpoint: `https://api.themoviedb.org/3/movie/{id}`
- [movie.json](/data/movie.json)

## AULA 04 - pydantic
- 26/08

### dotenv

### pydantic

```python
class MovieService:
    
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
```

```python
@app.get("/movie/{id}")
def get_movie(id: int):
    from tmdb.service import MovieService
    movie = MovieService.find_by_id(id)
    return movie
```


## AULA 03 - Requisições para APIs
- 19/08
- **requests:** biblioteca pythonb para fazer requisições HTTP
- exemplo de requisição para [api dog.ceo](aulas/aula3-requests/dogs.py)


Criar o ambiente virtual

```bash
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```


## AULA 02 - Endpoints

- 12/08
- exemplos de **endpoints:** [main.py](aulas/aula2-endpoints/main.py)


### Partes da URL

```
url:      https://zenquotes.io/api/today
domínio:  zenquotes.io
endpoint: api
resource: today
```

### fastapi

- https://github.com/fscheidt/fast
- SLIDES no AVA

Opções para iniciar o fastapi:

1) linha de comando:

```bash
uvicorn main:app --reload
```

2) no arquivo main.py

```python
# main.py - adicionar no final
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
```

## AULA 01 - JSON
- 05/08

Introdução à disciplina.

Foco da disciplina é o estudo de aplicações que usam a **arquitetura** baseada em Microserviços.

- Web IV: sistemas baseados na arquitetura de **Microserviços** 
- Web II e III: sistemas de arquitetura *Monolíticas*

### Atividade

- Modelagem de dados (JSON): [Ver no AVA](https://ava.ifpr.edu.br/course/view.php?id=14063)


### JSON

JSON (Javascript Object Notation)

JSON é uma notação (formato) para representar e transmitir informações entre cliente e servidor. 

- Exemplo: Suponha a classe model Pessoa:


```python
class Pessoa:
   id: int
   nome: str
   peso: float
   altura: float or None
   renda: float
   filhos: list
   endereco: Endereco
   enderecos: list[Endereco]
```

As informações de uma pessoa poderiam ser representadas no JSON abaixo:

```js
{
    "id": 101,
    "nome": "Maria",
    "peso": 72.4,
    "renda": 33500,
    "altura": null,
    "nome_completo": "Maria Aparecida",
    "filhos": ["João", "Roberta", "Luzia"],
    "endereco": {
        "id": 100101,
        "cep": "85850-000",
        "logradouro": "Av. Brasil",
        "numero": 444,
        "municipio": "Foz do Iguaçu"
    },
    "enderecos": [
        {
            "cep": "85850-000",
            "numero": 444,
            "municipio": "Foz do Iguaçu"
        },
        {
            "cep": "65850-000",
            "numero": 666,
            "municipio": "Curitiba"
        }
    ]
}

```

Agora podemos enviar os dados da pessoa para outro computador (cliente) pois JSON é uma linguagem universal.

### Ferramentas

- Validação do json: https://jsonlint.com/
- extensão chrome: [JSON Formatter](https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa)
- thunder client


### APIs

Abrir a seguinte url no navegador: 
- https://zenquotes.io/api/today




<br>
<br>

---

## Material complementar
- [(video) Configuração Ambiente dev Python](https://youtu.be/rqIrIfuyRmc)

