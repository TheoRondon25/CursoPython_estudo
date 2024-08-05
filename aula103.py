# from sys import path

# import aula103_package.modulo
# from aula103_package import modulo
# from aula103_package.modulo import *
# # from aula103_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula103_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)

from aula103_package.modulo import soma_do_modulo, fala_oi
print(__name__)
fala_oi()