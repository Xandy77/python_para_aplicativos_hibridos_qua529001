import time
import os

# declaração de dicionário
veiculo = {
    'fabricante': "chevrolet",
    'modelo': "chevete",
    'ano': 1973,
    'cor': "branco",
    'placa': "df-1973"
}

os.system("cls")
# exibe dados
for chave in veiculo:
    time.sleep(2)
    print(f"\n{chave.capitalize()}: {veiculo[chave]}\n")


# usuario escolhe a campo que deseja mudar
while True:
    campo = input("Informe o nome do campo que deseja alterar ou digite 'sair' para  encerrar o programa: ").strip().lower()

    match campo:
        case "fabricante":
            veiculo['fabricante'] = input("Informe o novo valor de 'fabricante': ").strip()
        case "modelo":
            veiculo['modelo'] = input("Informe o novo valor de 'modelo': ").strip()
        case "ano":
            veiculo['ano'] = input("Informe o novo valor de 'ano': ").strip()
        case "cor":
            veiculo['cor'] = input("Informe o novo valor de 'cor': ").strip()
        case "placa":
            veiculo['placa'] = input("Informe o novo valor de 'placa': ").strip()
        case "sair":
            break
        case _:
            print("Valor inválido.")
            continue

# mostra na tela os novos valores
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

