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


## AULA 03 - Requisições para APIs
- **requests:** biblioteca pythonb para fazer requisições HTTP
- exemplo requisição para [api dog.ceo](dogs.py)


Criar o ambiente virtual

```bash
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```


## AULA 02 (12/08)

### fastapi

- [exemplos (fastapi)](https://github.com/fscheidt/fast)
- SLIDES no AVA

### vocabulário

```
url:      https://zenquotes.io/api/today
domínio:  zenquotes.io
endpoint: api
resource: today
```

## AULA 01 (05/08) 

Introdução à disciplina.

Foco da disciplina é o estudo de aplicações que usam a **arquitetura** baseada em Microserviços.

- Web IV: sistemas baseados na arquitetura de **Microserviços** 
- Web II e III: sistemas de arquitetura *Monolíticas*

### Atividade

- Atividade modelagem com json: [Ver no AVA](https://ava.ifpr.edu.br/course/view.php?id=14063)


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

## Complementar
- [(video) configuração ambiente python](https://youtu.be/rqIrIfuyRmc)

