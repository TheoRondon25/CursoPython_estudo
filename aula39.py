"""
iterando strings com while
"""
#       012345678910      
nome = 'Theo Rondon' # Iteraveis

"""
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*T*h*e*o* *R*o*n*d*o*n' """

indice = 0 
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{letra}*'
    indice += 1

print(novo_nome)