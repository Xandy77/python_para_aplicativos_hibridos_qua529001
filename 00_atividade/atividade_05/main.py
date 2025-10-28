# TODO: atividade

'''
Crie uma lista com os nomes de todos os estados brasileiros, e mostre na tela os estados em ordem alfabética
'''

# entrada de dados
nome = [
    "Goiás", 
    "Pará", 
    "Paraná", 
    "Distrito Federal", 
    "Mato Grosso", 
    "Mato Grosso do Sul", 
    "Alagoas", 
    "Bahia", 
    "Ceará", 
    "Maranhão", 
    "Paraíba", 
    "Pernambuco", 
    "Piauí", 
    "Rio Grande do Norte", 
    "Sergipe",
    "Acre",
    "Amapá",
    "Amazonas",
    "Pará",
    "Rondônia",
    "Roraima",
    "Tocantis",
    "Espírito Santo",
    "Minas Gerais",
    "Rio de Janeiro",
    "São Paulo",
    "Santa Catarina",
    "Rio Grande do Sul"    
    ]

# exibe a lista
for estado in nome:
    print(estado)

nome.sort()

print("\nOrdem Alfabética:\n")
for estado in nome:
    print(estado)

'''estados.sort()

print("\nEstados Brasileiros\n")
for estado in estados
    print(estado)
'''