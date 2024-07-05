"""
enumerate - enumera iteraveis (indices)
"""
lista = ['Theo', 'Taina', 'Rondon']
lista.append('Joao')

# lista_enumerada = list(enumerate(lista))
# print(next(lista_enumerada)) # se estiver apenas enumerate(lista)
# print(lista_enumerada)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
# OU
"""
for indice, nome in enumerate(lista):
    print(indice, nome)
"""
""" 
for tupla_enumerada in enumerate(lista):
    print('FOR DA TUPLA: ')
    for valor in tupla_enumerada:
        print(f'{valor}')
"""


