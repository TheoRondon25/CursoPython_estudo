"""
Valores padrao para parametros.
Ao definir uma funçao, os parametros podem ter valores padrao. Caso o valor nao seja enviado 
para o parametro, o valor padrao sera usado.
Refatorar: editar o seu codigo.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=7, z=9, x=0)