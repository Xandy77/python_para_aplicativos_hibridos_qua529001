# tratamento de exceção
try:
    # entrada de dados
    numero = int(input("Informe um número inteiro: ").strip())

    # laço de repetição
    while numero >= 0:
        print(numero)
        numero -= 1
except:
    print("Não foi possível executar o contador.")