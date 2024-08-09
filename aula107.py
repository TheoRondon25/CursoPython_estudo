# Funcoes decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funcoes decoradoras sao funcoes que decoram outras funcoes 
# Decoradoras sao usados para fazer o Python usar as funcoes decoradoras em outras funcoes
# Decoradores sao "Syntax Sugar" (Açucar sintático)

# funçao decoradora
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('OK, Agora voce foi decorado')
        return resultado
    return interna

@criar_funcao # faz com que seja usado a funçao aqui
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser string')

# inverte_string_checando_parametro = criar_funcao(inverte_funcoes)
invertida = inverte_string('123')
print(invertida)