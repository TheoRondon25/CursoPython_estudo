""" while / else """
string = input('Digite um valor qualquer: ')
i = 0 
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('nao encontrei um espaço na string')
print('Fora do while.')