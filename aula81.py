# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
# RESOLUÇAO DO PROFESSOR
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()    

    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        qtd_acertos += 1
        print('Voce acertou!')
    else:
        print('Voce errou!')    
    print()

print(f'Voce acertou {qtd_acertos} de {len(perguntas)} perguntas')


# MINHA RESOLUÇAO
# resp = [2, 0, 1]
# num = 0
# acertos = 0
# for pergunta in perguntas:
#     print(f'Pergunta - {pergunta['Pergunta']}')
    
#     opcao1 = pergunta['Opções'][0]
#     opcao2 = pergunta['Opções'][1]
#     opcao3 = pergunta['Opções'][2]
#     opcao4 = pergunta['Opções'][3]

#     print('Opções: ')
#     print(f'0) {opcao1}')
#     print(f'1) {opcao2}')
#     print(f'2) {opcao3}')
#     print(f'3) {opcao4}')

#     resposta = input('Resposta:')
#     print()
#     if int(resposta) == resp[num]:
#         print('Voce acertou!')
#         acertos += 1
#     else:
#         print('Voce errou!')

#     num += 1
#     print()

# print(f'Voce acertou {acertos} de 3!')
    


