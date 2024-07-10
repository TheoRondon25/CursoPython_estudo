"""
Argumentos nomeados e nao nomeados em funçoes Python
Argumento nomeado tem nome com sinal de igual
Argumento nao nomeado recebe apenas o argumento (valor)
""" 

# Definição 
def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma # nome da funçao
soma(1, 2, 3) # execuçao da funcao
soma(y=1, z=3, x=2)
soma(1, 2, z=5)

print(1, 2, 3, sep='-')

