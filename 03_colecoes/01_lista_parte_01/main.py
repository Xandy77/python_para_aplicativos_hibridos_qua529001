# declaração de lista
nomes = [
    "Fulano", 
    "Beltrano", 
    "Cicrano", 
    "João", 
    "Maria", 
    "José"
    ]

# exibe o primeiro nome
#print(nomes[0])
#print(nomes[1])

# print(f"{nomes[0]} e {nomes[1]})

# exibe toda a lista
for nome in nomes:
    print(nome)

# ordena a lista em ordem alfabética
nomes.sort()

# re-exibe a lista em ordem alfabética
print("\nOrdem Alfabética:\n")
for nome in nomes:
    print(nome)

# reverte a ordem da lista
nomes.sort(reverse=True)

print("\nOrdem alfabética reversa:\n")
for nome in nomes:
    print(nome)
