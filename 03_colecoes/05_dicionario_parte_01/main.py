# Dicionário: É uma lista de dados, que aceita qualquer tipo de dado. Os dados são separados por chaves.
import time
import os

# Declaração de dicionario
usuario = {
    'nome' : 'Valdomiro Pereira',
    'idade' : 40,
    'peso' : 64.2,
    'altura' : 1.65,
    'email' : "xandnho2017@gmail.com"
}

os.system("cls")

# saída de dados
print(f"nome: {usuario['nome']}")
time.sleep(2)
print(f"\nidade: {usuario['idade']}")
time.sleep(1)
print(f"\npeso: {usuario['peso']}")
time.sleep(1)
print(f"\naltura: {usuario['altura']}")
time.sleep(1)
print(f"\nemail: {usuario['email']}\n")