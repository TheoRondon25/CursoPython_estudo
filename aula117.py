# reduce - faz a redução de um iteravel em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco'] 


total = reduce(
    # lambda ac, p: ac + p['preco'], # poderia ser feito desa forma ao inves da funcao abaixo
    funcao_do_reduce,
    produtos,
    0
)

print('o Total é', total)

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))