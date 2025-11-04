# função principal
def main():
    # entrada de dados
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())

    # operador ternário
    resultado = "é maior de idade." if idade >= 18 else "é menor de idade."

    # saída de dados
    print(f"{nome} {resultado}")

# protege algoritmo principal
if __name__ == "__main__":
    main()