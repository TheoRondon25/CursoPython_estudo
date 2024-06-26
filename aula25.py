"""
interpolaçao basica de strings
s - string
d e i - int
f - float
x e x - hexadecimal (ABCDEF0123456789)
"""
nome = 'Theo'
preco = 1000.9123123
variavel = '%s, o preço total foi R$%f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 1500))