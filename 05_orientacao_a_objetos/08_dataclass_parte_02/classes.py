from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str

def __str__(self):
        return f"E-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"

# para cada nova classe cria-se um @dataclass
@dataclass
class PessoaFisica(Pessoa):
    nome: str
    idade: int
    cpf: str
    profissao: str

def __str__(self):
        return f"\nDADOS DO USUÁRIO:\nNome: {self.nome}\nIdade {len(self)}\nCPF: {self.cpf}\nProfissão: {self.profissao}\n{super().__str__()}"

def __len__(self):
        return self.idade
    
@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str

    # o super serve pra herdar da super classe
def __str__(self):
        return f"\nDADOS DA EMPRESA:\nNome Fantasia: {self.nome_fantasia}\nCNPJ: {self.cnpj}\nWebsite: {self.website}\n{super().__str__()}"