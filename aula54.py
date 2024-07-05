"""
Faça uma lista de compras com listas.
O usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Nao permita que o programa quebre com erros de indices inexistentes na lista.
"""
import os 

lista_compras = []
while True:
    print('Selecione uma opçao')
    opcao = input('[i]nserir [a]pagar [l]istar [f]im: ')
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)
        
    elif opcao == 'l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('Nao ha nada para listar.')
            
        else:
            for item in enumerate(lista_compras):
                indice, nome = item
                print(indice, nome)
            
    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Digite o indice que quer apagar: ')

        try: 
            os.system('cls')
            indice = int(indice_str)
            print(f'Removendo indice {indice} que contem {lista_compras[indice]}')
            del lista_compras[indice]

        except TypeError:
            print('Por favor digite um numero inteiro.')
        
        except IndexError:
            print('Esse indice nao existe.')
    
    elif opcao == 'f':
        break

    else:
        os.system('cls')
        print('escolha uma opçao existente.')


     

