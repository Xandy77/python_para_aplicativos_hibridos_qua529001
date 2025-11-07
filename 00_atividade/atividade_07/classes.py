class Conta:
    def __init__(self, nome, cpf, numero_agencia, numero_conta, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero_agencia = numero_agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def consultar_dados(self):
        print(f"Titular da Conta: {self.nome}")
        print(f"CPF do Titular: {self.cpf}")
        print(f"Agência: {self.numero_agencia}")
        print(f"Conta: {self.numero_conta}")
        print(f"Saldo: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")