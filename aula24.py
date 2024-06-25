# operadores in e not in
# Strings sao iteraveis
#  0 1 2 3 
#  T h e o
# -4-3-2-1
nome = 'Theo'
print(nome[2])
print(nome[-4])
print('T' in nome)
print('á' in nome)

######

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')