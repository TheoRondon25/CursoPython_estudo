# Exercicios 
# Crie funçoes que duplicam, triplicam e quadruplicam o numero recebido como parametro

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# numero = int(input('Digite um numero inteiro: '))

# print(f'Duplicado: {duplicar(numero)} | Triplicado: {triplicar(numero)} |' \
#       f'Quadruplicado: {quadruplicar(numero)}')

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar   

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
