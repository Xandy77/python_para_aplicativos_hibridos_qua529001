# TODO: atividade 07

# bibliotecas
import os
from classes import Conta

# Função para limpar a tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Função para exibir o menu e gerenciar as operações
def menu_conta():
    print("\n===== Banco Python =====")
    nome = input("Informe o nome do titular da conta: ").strip().title()
    cpf = input("Informe o CPF do titular da conta: ").strip()
    numero_agencia = input("Informe o número da agência: ")
    numero_conta = input("Informe o número da conta: ")

    conta = Conta(nome, cpf, numero_agencia, numero_conta)

    while True:
        # Limpar a tela antes de mostrar o menu novamente
        limpar()

        # Exibir o menu de opções
        print("\nEscolha uma opção:")
        print("1. Consultar dados da conta")
        print("2. Depositar valor")
        print("3. Sacar valor")
        print("4. Sair do programa")

        opcao = input("Opção: ")

        if opcao == "1":
            conta.consultar_dados()
        elif opcao == "2":
            try:
                valor_deposito = float(input("Informe o valor para depósito: R$ "))
                conta.depositar(valor_deposito)
            except ValueError:
                print("Por favor, informe um valor numérico válido.")
        elif opcao == "3":
            try:
                valor_saque = float(input("Informe o valor para saque: R$ "))
                conta.sacar(valor_saque)
            except ValueError:
                print("Por favor, informe um valor numérico válido.")
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        # Pausar a execução para o usuário ver o resultado da operação antes de limpar a tela
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu_conta()
"""
Crie um app de banco. O programa deverá ter a classe Conta, com os atributos:
- Titular da conta(nome)
- CPF do titular
- Número da agência
- Número da conta
- Saldo
- O usuário irá inserir os dados "Titular da conta" e "CPF", e poderá escplher entre as seguintes opções:
- Consultar dados da conta
- Depositar valor
- Secar valor
- Sair do programa
"""