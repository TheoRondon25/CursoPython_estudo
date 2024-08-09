# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iteravel + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores unicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'joão', 'Joana', 'luiz', 'Leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G'],
    ['MASCULINO', 'FEMININO', 'UNISEX'],
    ['algodão', 'poliester']
]

#print_iter(combinations(pessoas, 2))
#print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))