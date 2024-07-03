"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Theo' # __iter__()
iteratador = iter(texto)
# print(next(iteratador)) # mesmo que print(iteratador.__next__())

while True:
    try: 
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# É ASSIM QUE O FOR FUNCIONA
"""
entao, esse while acima funciona da mesma maneira que esse for:
for letra in texto:
    print(letra) 
"""


