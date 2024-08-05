from aula103_package.modulo_b import fala_oi

# isso faz com que eu limite a importaçao, se em outro modulo, eu importar all (*), 
# só vou ter acesso a o que eu deixar aqui na lista
__all__ = [ 
    'variavel',
    'soma_do_modulo',
]

variavel = 'Alguma coisa'

def soma_do_modulo(x, y):
    return x + y

# fala_oi()