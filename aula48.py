"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo 
Conhecimentos reutilizaveis - indices e fatiamento 
Metodos uteis: 
    append - Adiciona um item ao final 
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

"""
#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
# print(lista, type(lista))

#        0    1     2              3    4
#       -5   -4    -3             -2   -1
lista = [123, True, 'Theo Rondon', 1.2, []]
lista[2] = 'Neymar'
print(lista)
print(lista[2].upper(), type(lista[2]))
"""

"""
# CRUD - APPEND - POP - DEL - CLEAR - INSERT
#         0   1   2   3   4   5
lista2 = [10, 20, 30, 40, 50, 60] # criar
ler = lista2[2] # ler
lista2[3] = 400 # alterar
del lista2[5] # deletar

lista2.append(70) # adicionando item ao final da lista 
ultimo_valor = lista2.pop() # remove o ultimo item da lista 
print('Removemos:', ultimo_valor)
del lista2[-1] # removendo o ultimo indice
lista2.insert(0, 'Theo') # adiciona um item na posiçao que eu quiser
print(lista2)
"""

# EXTEND - + 
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # concatena a lista A com a lista B
# print(lista_c)
lista_a.extend(lista_b) # estende a lista A com a lista B
print(lista_a)