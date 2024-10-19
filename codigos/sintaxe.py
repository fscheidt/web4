import datetime  # importa o pacote datetime

print("hello world")

# obtem a data atual
data = datetime.datetime.now()
dia = 4
print(data)
print(type(dia)) # obtem o tipo da variavel

# exemplo de if
if dia == 4:
    print("Aula de Web")
    print("Inicio 19h00")
else:
    print("Outra aula")

# exemplo de função
def get_time() -> str: 
    d = datetime.datetime.now() # obtem a datetime atual
    return f"{datetime.datetime.time(d)}"

# chama a função
time = get_time()
print(time)

# exemplo de lista
lista = ["segunda", "terca", "quarta"]
for d in lista:
    print(d)

# tamanho da lista
print(len(lista))

# exemplo de dicionário (objeto)
pessoa = {
    "nome": "Maria",
    "cpf": "10101010101",
    "idade": 33,
}
print(pessoa)
print(type(pessoa))
print(pessoa['nome'])
