"""
Exercicio
Peça ao usuario para digitar seu nome, sua idade
Se o nome e a idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se o nome contem (ou nao) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios"
"""
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

# resoluçao minha
if nome != '' and idade != '' :
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[:1]}')
    print(f'A ultioma letra do seu nome é {nome[-1:-1]}') # ERRO
else: 
    print('Desculpe, voce deixou campos vazios')
    
# resoluçao professor 
if nome and idade: # se for vazio fica False
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome: 
        print('Seu nome contem espaços')
    else:
        print('Seu nome nao contem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultioma letra do seu nome é {nome[-1]}')
else: 
    print('Desculpe, voce deixou campos vazios')