# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import aula101_m
from aula101_m import soma, variavel_modulo
# criando outra aula para importar o modulo

# print('Este módulo se chama', __name__)

print(aula101_m.variavel_modulo)
print(variavel_modulo)

print(soma(2, 3))
print(aula101_m.soma(2, 3))