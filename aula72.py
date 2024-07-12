# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.


def mutiplicar(*args):
    total = 1 
    for numero in args:
        total *= numero
        print(numero, '*')
    return total

conta = mutiplicar(2, 3, 4)
print('Resultado da conta:', conta)

# Crie uma funcao que fala se um numero é par ou impar
# Retorne se o numero é par ou impar

def par_impar(*args):
    for numero in args:
        if numero % 2 == 0:
            print(f'{numero} é PAR')
        else: 
            print(f'{numero} é IMPAR')  

par_impar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)     
