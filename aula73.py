"""
Higher Order Functions
Funçoes de primeira classe
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Theo')
)
print(
    executa(saudacao, 'Boa noite', 'meu consagrado')
)