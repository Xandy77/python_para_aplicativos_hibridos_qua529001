# Cria o Banco e Entidade Pessoa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker # cria uma sessão para realizar operações inserir, atualizar, deletar) no banco de dados

from entidades import criar_tb_pessoa
from modulo import limpar, cadastrar

# cria a main ()
def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base) # engine cria o banco
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    while True:
        print(f"{'-'*20} 🐍CRUD DA COBRA🐍{'-'*20}\n")
        print("0 - Sair do programa")
        print("1 - Cadastrar nova pessoa: ")
        opcao = input("Opção desejada: ")
        match opcao:
            case "0":
                print("Programa encerrado.")
                break
            case "1":
                print(cadastrar(session, Pessoa))
                continue
            case _:
                print("Opção inválida.")
                continue

    
    session.close()

# chama a main ()
if __name__=="__main__":
    main()