from sqlalchemy import Column, String, Integer, Date

# função que cria o banco de dados e as entidades
def criar_tb_pessoa(engine, Base):
    # tratamento de exceção
    try:
        # Base vai herdar a classe que existe dentro do sqlalchemy
        class Pessoa(Base):
            __tablename__= "pessoa" # pessoa é o nome da entidade

            # atributos (classe)
            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            nascimento = Column(Date, nullable=False)
            email = Column(String, nullable=False, unique=True)
            genero = Column(String, nullable=True) # nullable não é unico, então não é obrigatório informar

        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print(f"Não foi possível conectar com o banco de dados. {e}.")






# Entidades: Uma tabela no banco de dados é uma entidade, a tabela é dividida entre colunas e linhas. Cada uma dessas entidades possui atributos.
# Atributos definem a Entidade. O arquivo entidade é onde define as classes.
# Classes é uma representação de uma entidade.
# Crud é o nome do sistema mais basico que existe no Banco de Dados. Creat Read Update Delete = crud
# SQ light = ele usa a própria aplicação.
# Apasta datebase é aonde irá ficar armazenado o banco de dados.
# Persistência de dados: são dados que  não se perdem quando se fecha a aplicação, usar a biblioteca sqlalchem 
# O que uma classe e uma entidade tem em comum: atributos.