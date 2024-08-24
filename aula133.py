# Metodos de classe + factories (fabricas)
# Sao metodos onde "self" será "cls", ou seja, ao inves de receber a instancia no primeiro parametro, recebemos a própria classe.
class Pessoa:
    ano = 2024 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('Joao', 34)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

p2 = Pessoa.criar_com_50_anos('Helena')
print(p2.nome, p2.idade)

p3 = Pessoa.criar_sem_nome(23)
print(p3.nome, p3.idade)
