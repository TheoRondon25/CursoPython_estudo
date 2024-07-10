# Desempacotamento em chamadas de metodos e funcoes 

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [ 
    # 0       1
    ['Theo', 'Taina', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'Joao', 'Eduarda', ], # 2
]

# a, b, c, *_, ap, u = lista # ap - antepenultimo item da lista
# print(a, u, ap)

#print(*lista) # <- isso 
#print('Maria', 'Helena', 1, 2, 3, 'Eduarda') # <- é o mesmo que isso
#print(*string)
#print(*tupla)

#for nome in lista:
#    print(nome, end=' ')

print(*salas, sep='\n')