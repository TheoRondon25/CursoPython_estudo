"""
Introduçao as funcoes (def) em Python.
Funçoes sao trechos de codigos usaddos para replicar determinada açao ao longo do seu codigo.
Elas podem receber valores para parametros (argumentos) e retornar um valor especifico.
Por padrao, funçoes Python retornam None (nada).
"""

# def Print(a, b, c):
#     print('varias1')
#     print('varias2')
#     print('varias3')
#     print('varias4')

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá {nome}!')

saudacao('Theo')
saudacao('Taina')
saudacao('Mundo')
saudacao()