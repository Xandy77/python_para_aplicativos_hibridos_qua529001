# bibliotecas
import os

# declaração de lista
usuarios = []

# limpa console
os.system("cls")

while True:
    # menu
    print("1 - Cadastrar novo usuario")
    print("2 - Listar usuario")
    print("3 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    match opcao:
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe o nome do usuário: ").strip().title()
            usuario['idade'] = int(input("Informe a idade do usuário: ").strip())
            usuario['email'] = input("Informe o email do usuário: ").strip().lower()
            usuarios.append(usuario) # insere o usuario a lista
            os.system("cls")
            print("Novo usuário inserido com sucesso.")
            continue
        case "2":
            for usuario in usuarios: # percorre a linha
                for chave in usuario: # percorre a coluna
                    print(f"{chave.capitalize()}: {usuario[chave]}")
                print(f"{'-'*40}")
            continue
        case "3":
            break
        case _:
            print("Opção inválida.")
            continue