# and (e) or (ou) not (nao)
# Se qualquer valor for considerado falso, a expressao inteira sera avaliada naquele valor.
# Sao considerados falsy: 0 0.0 '' False

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else: 
#     print('Sair')

# avaliaçao de curto circuito
print(True and False and True)
print(bool('')) # se tiver espaço entre as aspas será considerado True