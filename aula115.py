from functools import partial
from types import GeneratorType

# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p,
#       'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

def muda_preco_de_produto(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }

# FUNÇÃO MAP
# convertendo aqui em list, eu nao terei mais um iterator, e assim poderei reutilizar essa lista onde eu quiser
novos_produtos = list(map(  
    muda_preco_de_produto,
    produtos
))

# novos_produtos = (x for x in produtos) # isso é um generator

print_iter(produtos)
print_iter(novos_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)

# print(list(novos_produtos)) # transformando o iterator em lista aqui, ele esgota o iterator

# print(novos_produtos) # pra saber que é map
# print(hasattr(novos_produtos, '__iter__')) # tem iter ?
# print(hasattr(novos_produtos, '__next__')) # tem next ?
# print(isinstance(novos_produtos, GeneratorType)) # para saber se é um generator ou nao