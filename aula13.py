nome = 'Theo Rondon'
altura = 1.75
peso = 84.5
imc = peso / (altura * 2)

linha_1 = f'{nome} tem {altura:.2f} de altura' # :.2f -> representa duas casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)