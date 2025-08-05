# Desenvolvimento Web IV

## Aula 1 
- 05/08/25

Foco da disciplina é o estudo de aplicações que usam a **arquitetura** baseada em Microserviços.

- Web IV: sistemas baseados na arquitetura de **Microserviços** 
- Web II e III: sistemas de arquitetura *Monolíticas*

### Serialização de dados com JSON

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

- Validação do json: https://jsonlint.com/
- extensão chrome: [JSON Formatter](https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa)

### APIs

Abrir a seguinte url no navegador: https://zenquotes.io/api/today


### Material

- [Material](https://drive.google.com/drive/folders/1xsq_DNEq8DBFviDl0x2B5C89xBazAE-l?usp=sharing)
- [Configuração ambiente dev](https://youtu.be/rqIrIfuyRmc)

