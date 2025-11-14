import os

from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main_passoa_fisica():
    # criar um objeto da Pessoa Fisica
    print("Cadastrar Pessoa Física:")

    nome = input("Informe o nome: ").strip().title()
    idade = int(input("Informe a idade: ").strip())
    cpf = input("Informe o CPF: ").strip()
    profissao = input("Informe a profissão: ").strip().title()
    email = input("Informe o e-mail: ").strip()
    telefone = input("Informe o telefone: ").strip()
    endereco = input("Informe o endereço: ").strip()
    
    
    
    usuario = PessoaFisica(nome="", idade=0, cpf="", profissao="", altura=0.0)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: ").strip())
    usuario.altura = float(input("Informe a altura em metros: ").strip().replace(",","."))

    limpar()
    print(usuario)
    print(f"{usuario.nome} {usuario.verificar_maioridade()}.")

if __name__ == "__main__":
        main()