"""
Flag (bandeira) - Marcar um local
None = Não valor
is e is not = é ou nao é (tipo, valor, identidade)
id = identidade
"""
# v2 = 'a'
# print(id(v1))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faáa algo')
else:
    print('nao faça nada')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Nao passou no if')
else: 
    print('Passou no if')