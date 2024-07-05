"""
Tipo tupla - uma lista imutavel 
"""
nomes = 'Theo', 'Taina', 'Rondon' # pode criar a tupla com parentes ou sem nada
print(nomes[1])

lista = [1, 2, 3]
nao_lista = tuple(lista) # tranformando a lista em tupla
lista_de_novo = list(nao_lista) # transformando em lista novamente
print(nao_lista, lista_de_novo)

