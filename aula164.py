# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field, fields

# frozen=True -> CONGELANDO O DATACLASS PARA NAO SER ADICIONADO NADA NELE 
# order=True, repr=False, etc
@dataclass()  # TEMOS CONFIGURAÇOES QUE PODEM SER PASSADAS AQUI
class Pessoa: 
    nome: str = field(default='Missing')
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)

if __name__ == '__main__':
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)
    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.nome)
    # print(ordenadas)

