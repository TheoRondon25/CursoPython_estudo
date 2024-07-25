lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

# fazendo em list comprehension
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# list comprehension dentro de um valor de list comprehension
lista = [
    [letra for letra in 'Luiz']
    for x in range(3)
]

print(lista)