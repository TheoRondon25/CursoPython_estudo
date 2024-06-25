# and (e) or (ou) not (nao)
# Se qualquer valor for considerado falso, a expressao inteira sera avaliada naquele valor.
# Sao considerados falsy: 0 0.0 '' False

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')

senha = print(0 or False or 0.0 or 'abc' or True)
print(senha)