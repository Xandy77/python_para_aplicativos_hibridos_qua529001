# Cria o Banco e Entidade Pessoa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker # cria uma sessão para realizar operações inserir, atualizar, deletar) no banco de dados

from entidades import criar_tb_pessoa
from modulo import limpar

# cria a main ()
def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base) # engine cria o banco
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    # TODO: fazer o CRUD
    
    session.close()

# chama a main ()
if __name__=="__main__":
    main()