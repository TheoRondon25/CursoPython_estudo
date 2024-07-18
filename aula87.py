# Empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a
# print(a, b)

# a, b = pessoa.values()
# a, b = pessoa.items()
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (ja vimos)
# kwargs - kayword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NAO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4,
}
mostro_argumentos_nomeados(**configuracoes)