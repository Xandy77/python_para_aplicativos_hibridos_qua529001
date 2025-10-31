# declaração de coleções
# a lista tem colchetes, no caso abaixo estou colocando varios dicionarios dentro de uma lista
# Uma lista são sequência de dados

usuarios = [
    {
        'nome': "fulano",
        'idade': 20,
        'email': "fulano@gmail.com"
    },

    {
        'nome': "Cicrano",
        'idade': 25,
        'email': "cicrano@gmail.com"
    },

    {
        'nome': "Beltrano",
        'idade': 30,
        'email': "beltrano@gmail.com"
    }

]

# exibindo os dados dos usuários
for usuario in usuarios:
    print(f"\n{'-'*40}\n")
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario[chave]}")