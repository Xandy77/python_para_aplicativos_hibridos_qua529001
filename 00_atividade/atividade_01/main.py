# TODO: atividade
"""
Crie um programa que receba do usuário o nome, e-mail, cpf e telefone, limpe o console, e em seguida, exiba as informações do usuário na tela.
"""

# biblioteca
import os

# entrada de dados
nome = input("Informe seu nome: ").strip().title() # string
email = input("Informe seu email: ").strip().lower() # string
cpf = input("Informe seu CPF: ").strip() # string
telefone = input("Informe seu telefone: ").strip() # string

#limpa console
os.system("cls")

# saída de dados
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")