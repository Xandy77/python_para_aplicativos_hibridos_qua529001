# biblioteca
import os


# declaração de lista
nomes = []

# limpa console
os.system("cls")

# loop
while True:
    # menu
    print("1 - Inserir novo nome")
    print("2 - Exibir lista de nomes")
    print("3 - Excluir nome na lista")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    match opcao:
        case "1":
            os.system("cls")
            novo_nome = input("Informe um novo nome: ").strip().title()
            nomes.append(novo_nome) # insere novo nome na lista
            os.system("cls")
            print(f"{novo_nome} cadastrado com sucesso")
        case "2":
            os.system("cls")
            print("Lista de nomes:\n")
            for i in range(len(nomes)): # FIXME 
                print(f"{i} - {nomes[i]}") # estudar mais sobre essa linha
            print(f"\n{'-'*40}\n")
            continue
        case "3":
            os.system("cls")
            try:
                posicao = int(input("Informe a posição a ser excluída: ").strip())
                if posicao >= 0 and posicao < len(nomes):
                    del(nomes[posicao])
                    print("Nome excluído com sucesso.")
                else:
                    print("Posição inexistente.")
            except Exception as e:
                print(f"Posição inválida. {e}.")
            continue
        case "4":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
