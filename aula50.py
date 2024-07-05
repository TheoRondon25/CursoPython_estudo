"""
Exercicio
Exiba os indices da lista

"""
lista = ['Theo', 'Taina', 'Rondon']
lista.append('Joao')
# MINHA SOLUÇAO
indice = 0
for nome in lista:
    print(indice, nome)
    indice += 1

# PROF
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])

