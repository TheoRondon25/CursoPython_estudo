"""
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""
lista_a = ['Theo', 'Rondon', 1, True, 1.2]
lista_b = lista_a
lista_c = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b, lista_c)

 