# Encapsulamento: Tecnica de esconder no programa determinados elementos(deixar dados invisivel, protegidos).
# Todos os atributos da classe devem ser encapsulados.
class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    # métodos get
    @property
    def nome(self):
        return self.__nome
    
    # método set(atribui valor)
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf