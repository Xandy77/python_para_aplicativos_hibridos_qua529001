# importação de bibliotecas
import os

# loop
while True:
    
    # limpeza de console
    os.system("cls") # os.system é o nome de uma biblioteca
    
    # tratamento de exceção
    try:
        nome = input("Informe nome: ").strip().title()
        email = input("Informe o e-mail: ").strip().lower() # pega todas as letras maiusculas e transforma em minusculas
        cpf = input("Informe o CPF: ").strip() 

        # limpeza de console
        os.system("cls") # após fazer a limpeza do console irá exibir os dados na tela

        # saída de dados
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")  

        # menu
        print("1 - Inserir novos dados.")
        print("2 - Sair do programa.")

        opcao = input("Opção desejada: ").strip()    

        # varifica a opção escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break

    except:
        print("Não foi possível receber informações.")