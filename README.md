# Inicialização do back e front

## Run
Para iniciar os serviços do back e front, executar os comandos abaixo para iniciar cada aplicação. 

backend (fastapi):
```bash
cd web4
uvicorn main:app --reload
```

frontend (svelte):
```bash
cd web4/front
npm run dev -- --open
```

## Install

**Atenção**: se você fez git clone ou download desse projeto, o ambiente virtual precisa ser gerado na sua máquina. Executar os comandos abaixo para criar cada ambiente:

(1) Abrir o terminal, usar o git para baixar uma cópia desse projeto:

```bash
git clone https://github.com/fscheidt/web4
```

(2) Gerar ambiente virtual do **backend (python):**

```bash
cd web4
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Resultado: a pasta `env` é criada no projeto:

```
├── /env            <--
├── /front
├── /json
├── /pycine
├── main.py
├── README.md
└── requirements.txt
```

(3) Instalar dependências do **frontend (nodejs):**

```bash
cd front
npm install
```

Resultado: a pasta `node_modules` e `.svelte-kit` são geradas:

```
├── /env
├── /front
│   ├── /node_modules        <--
│   ├── /.svelte-kit         <--
├── /json
├── /pycine
├── main.py
├── README.md
└── requirements.txt
```

# Modelo de dados

Pydantic é uma biblioteca que facilita a serialização e deserialização de objetos em json e vice-versa. Além disso, pode-se usar o esquema de validação do pydantic para verificar se o json retornado possui os valores obrigatórios.

## pydantic

Instalação:

```bash
pip install pydantic
```


## Congelar o ambiente virtual

Gera um arquivo contendo todas as dependências do projeto:

```bash
source env/bin/activate
pip freeze > requirements.txt
```

Restaura o ambiente virtual
```bash
python3 -m venv env
pip install -r requirements.txt
```

# Credenciais
Credenciais devem ser armazenadas em um arquivo de configuração,
que não está rastreado pelo controle de versão ou seja compartilhado.

## Instalar biblioteca dotenv
Permite a leitura do arquivo .env de configuração

```bash
pip install python-dotenv
```


## Arquivo `.env` 
Na pasta raiz do projeto, criar um arquivo chamado `.env` com o conteúdo:

```
API_TOKEN = "COLOCAR_AQUI_O_TOKEN_DO_TMDB"
```

## Importar token do ambiente 

```python
import os
import dotenv
dotenv.load_dotenv(".env")
token = os.environ["API_TOKEN"]
```

## Formato de URLs

### Query parameter
https://api.themoviedb.org/3/search/person?id=2000

### Url parameter 
https://api.themoviedb.org/3/search/person/2000

----

# API TMDB
- Cadastro no site para gerar a chave da API:
- https://www.themoviedb.org/settings/api

## Documentação
- https://developer.themoviedb.org/reference/intro/getting-started

# Criação do ambiente virtual Python
## cria a pasta env (somente uma vez)
```bash
python3 -m venv env
```

## Ativar o ambiente
Ativa o ambiente para usar no projeto.

```bash
source env/bin/activate

# windows
.\env\scripts\activate
```

### verifica qual o python esta sendo usado no terminal
```
which python
```

## Instalar biblioteca requests
```bash
pip install requests
```

# Servidor Web (FastAPI)

Instalar o fastapi e o servidor uvicorn

```bash
pip install "fastapi[standard]" uvicorn
```

## Inicia o servidor 
```bash
uvicorn main:app --reload
uvicorn main:app --reload --port=5000 # opcional se a port 8000 estiver em uso
```

## Verificar todos os endpoints
- http://127.0.0.1:8000/docs


---
---


# Desenvolvimento Web IV
- https://github.com/fscheidt/web4
- https://ava.ifpr.edu.br/course/view.php?id=12869


## Sobre a disciplina
- JSON (serialização de dados)
- API (application program interface)
- REST 

## Ambiente de desenvolvimento

Testar no terminal:

```bash
python3 --version
pip -V
```

extensão do vscode:
- thunder client



## JSON (formato)

Notação para representar dados, usando chave-valor

```json

{
  "id": 13491,
  "disciplina": "DESENVOLVIMENTO WEB IV",
  "curso": {
    "nome": "tads",
    "turma": 2023
  },
  "professores": ["Felippe"],
  "alunos": 14,
  "turno": "noturno",
  "ativa": true,
  "ava": null,
  "percentual": 5.5
}

```

Validação do json: 
- https://jsonlint.com/


## Atividade 1

Estruturar numa representação json informações sobre filmes e series

- https://filmow.com/pearl-t343849/ficha-tecnica/

Proponha um JSON que represente os dados contidos na página "ficha técnica".


## Atividade 2

Estruturar JSON para representar dados sobre a capital até Internet TLD do país Chile. Ver dados na página:
- https://en.wikipedia.org/wiki/Chile

