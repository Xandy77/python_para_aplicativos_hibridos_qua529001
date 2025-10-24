# TODO: atividade
"""
Crie um programa que recebe do usuário o nome e a idade, e em seguida, exiba na tela uma lista de filmes, suas respectivas salas e classificações indicativas:
Sala 1 - A Roda Quadrada - Livre
Sala 2 - A Volta dos Que Não Foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As Tranças do Rei Careca - 16 anos
Sala 5 - A Vingança do Frango Assado - 18 anos
O usuário deverá escolher o filme, e caso ele tiver a idade mínima para ver o filme, imprime o ingresso e encerra o programa. Caso o usuário não tenha a idade mínima, o programa impede a entrada do usuário e re-exibe a lista de filmes para que o mesmo escolha outro filme.
"""

nome = input("Insira seu nome: ").strip().lower()
idade = int(input("Insira sua idade: ").strip())

print(f"Nome: {nome}")
print(f"Idade: {idade}")

# Lista de filmes e classificações
filmes = [
    {"sala": 1, "titulo": "A Roda Quadrada", "classificacao": "Livre", "idade_minima": 0},
    {"sala": 2, "titulo": "A Volta dos Que Não Foram", "classificacao": "12 anos", "idade_minima": 12},
    {"sala": 3, "titulo": "Poeira em Alto Mar", "classificacao": "14 anos", "idade_minima": 14},
    {"sala": 4, "titulo": "As Tranças do Rei Careca", "classificacao": "16 anos", "idade_minima": 16},
    {"sala": 5, "titulo": "A Vingança do Frango Assado", "classificacao": "18 anos", "idade_minima": 18}
]