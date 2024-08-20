import json
from aula132_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])

    print(p1.nome, p1.idade, p1.sobrenome)
    print(p2.nome, p2.idade, p2.sobrenome)

# print(__name__)