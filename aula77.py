# Manipulando chaves e valores em dicionarios
pessoa = {}

# adicionando valor a um dicionario
chave = 'nome_completo'
pessoa[chave] = 'Luiz Otavio'
pessoa['sobrenome'] = 'Miranda'

# verificando um unico valor do dicionario
print(pessoa[chave])

# alterando valor do dicionario
pessoa[chave] = 'Theo'
print(pessoa)

# deletando valor do dicionario
del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('NAO EXISTE')
else:
    print(pessoa['sobrenome'])

