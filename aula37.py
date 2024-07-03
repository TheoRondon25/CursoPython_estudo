"""
Repetiçoes 
whle (enquanto)
Executa uma açao enquanto uma condiçao for verdadeira 
"""
contador = 0

while contador <= 10:
    contador += 1

    if contador == 6:
        print('Nao vou mostrar o 6')
        continue

    print(contador)
    if contador == 4:
        break

print('Acabou')