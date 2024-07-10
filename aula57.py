"""
Lista de listas e seus indices 
"""
salas = [ 
    # 0       1
    ['Theo', 'Taina', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'Joao', 'Eduarda', (0,1,2,3,4)], # 2
]

print(salas[0])
print(salas[2][2])
print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
