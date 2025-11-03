# biblioteca
import os

# função
# o return não fica entre parenteses pois não é uma função
def boas_vindas(nome):
    os.system("cls")
    return f"Seja bem vindo, {nome}! 🐍"

# algoritmo principal
os.system("cls")
nome = input("Informe seu nome: ").strip().title()
resultado = boas_vindas(nome)
print(resultado)