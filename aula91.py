# Dictionary Comprehension e set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
# for chave, valor in produto.items():
#     print(chave, valor)

dc = { 
    chave : valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}
# print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]
# dc = {
#     chave: valor 
#     for chave, valor in lista
# }

# print(dict(lista))

# set comprehension
s1 = {i for i in range(10)}
print(s1) 