"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print('------- Exercicio 1 -------')

numero = input('Digite um numero inteiro: ')
try:
    numero_float = float(numero)
    if numero_float % 2 == 0:
        print('O numero é par!')
    else:
        print('O numero é impar!')

    if numero.isdigit():
        print('É um numero inteiro')
    else: 
        print('O Numero não é um inteiro!')
except:
    print('O que digitou nao é um numero')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('------- Exercicio 2 -------')

hora = input('Digite a hora de agora: ')
hora_agora = int(hora[:2])
if hora_agora <= 11:
    print('Bom dia')
elif hora_agora > 11 and hora_agora <= 17:
    print('Boa tarde')
else:
    print('Boa noite')

# professor:
#entrada = input('Digite a hora em números inteiros: ')

#try:
#    hora = int(entrada)

#    if hora >= 0 and hora <= 11:
#        print('Bom dia')
#    elif hora >= 12 and hora <= 17:
#        print('Bom tarde')
#    elif hora >= 18 and hora <= 23:
#        print('Bom noite')
#    else:
#        print('Não conheço essa hora')
#except:
#    print('Por favor, digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('------- Exercicio 3 -------')

nome = input('Escreva seu nome: ')
qnt_letras = len(nome)

if qnt_letras <= 4:
    print(f'{nome}, Seu nome é muito curto')
elif qnt_letras >= 5 and qnt_letras <= 6:
    print(f'{nome}, Seu nome é normal')
else: 
    print(f'{nome}, Seu nome é muito grande')