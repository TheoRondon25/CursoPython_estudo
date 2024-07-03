""" 
Repetiçoes 
whle (enquanto)
Executa uma açao enquanto uma condiçao for verdadeira 
"""
condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')    

    if nome == 'sair':
        break
    
print('Acabou')