"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
============= resultado
lista_soma = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# 3° metodo de fazer:
# print(list(zip(lista_a, lista_b))) # desempacotando as listas
lista_soma = [x + y for x, y in zip(lista_a, lista_b)] # uniao das duas listas
print(lista_soma)


# Metodo que funciona em todas as linguagens:
#lista_soma = []
#for i in range(len(lista_b)): # pegando o tamanho da lista (ou seja, nao vai passar do tamanho da lista que eu colocar aqui)
#    lista_soma.append(lista_a[i] + lista_b[i]) # pegando o mesmo inidice de cada lista por vez
#print(lista_soma)


# Outro metodo (mais pythonico):
#lista_soma = []
#for i, _ in enumerate(lista_b):
#    lista_soma.append(lista_a[i] + lista_b[i])
#print(lista_soma)

