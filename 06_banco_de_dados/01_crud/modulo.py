import os
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o gênero: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa):").strip()
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        email = input("Informe o E-mail: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all() # p minusculo é objeto ou atributos, P maiusculo nome de Classes ou Constancia

        if email in [pessoa.email for pessoa in pessoas]:
            return "E-mail já cadastrado."
        else:
            nova_pessoa = Pessoa(
                nome=nome,
                nascimento=nascimento,
                email=email,
                genero=genero                            
            ) # Não se usa aspas pois o atributo esta recebendo o valor da variavel

            # insert into pessoa
            session.add(nova_pessoa) # inserindo a consulta
            session.commit() # executando, confirmando o objeto inserido na consulta

            return f"Pessoa {nova_pessoa.nome} cadastrado com sucesso."

    except Exception as e:
        print(f"Não foi possível cadastrar. {e}.")