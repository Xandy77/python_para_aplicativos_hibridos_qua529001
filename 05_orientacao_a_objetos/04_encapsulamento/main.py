import os
from classes import Pessoa

# limpa tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    usuario = Pessoa(nome="", cpf="")

    limpar()

    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu CPF: ").strip()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")

    

if __name__=="__main__":
    main()