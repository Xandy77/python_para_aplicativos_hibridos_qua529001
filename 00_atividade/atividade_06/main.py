# TODO: atividade

'''
Crie um rpograma que receba do usuário os seguinte dados:

- Nome
- E-mail
- Telefone
- CPF
- Gênero

Após isso, o programa deve armazenar esses dados em um dicionário e exibir os dados desse dicionário na tela.

'''
import os
# declaração 
usuario = {
    'nome': input("Digite o seu nome: "), 
    'email': input("Digite o seu email: "), 
    'telefone': input("Digite o seu telefone: "),
    'cpf': input("Digite o seu cpf: "),
    'genero': input("Digite o seu genero: ") 
    
}

os.system("cls")

print("Dados do usuário: ")
for chave, valor in usuario.items():
    print(f"\n{chave.capitalize()}: {valor}")