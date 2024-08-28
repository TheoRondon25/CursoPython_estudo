# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# MINHA RESPOSTA
class Carro:
    def __init__(self, nomeCarro):
        self.nomeCarro = nomeCarro


class Motor:
    def __init__(self, nomeMotor):
        self.nomeMotor = nomeMotor
        self.carros_motor = []

    def insercao_Carro_Motor(self, nomeCarro):
        self.carros_motor.append(Carro(nomeCarro))

    def listar_carros_motor(self):
        for carro in self.carros_motor:
            print(self.nomeMotor, carro.nomeCarro)


class Fabricante:
    def __init__(self, nomeFabricante):
        self.nomeFabricante = nomeFabricante
        self.carros_fabricante = []
    
    def insercao_Carro_Fabricante(self, nomeCarro):
        self.carros_fabricante.append(Carro(nomeCarro))

    def listar_carros_fabricante(self):
        for carro in self.carros_fabricante:
            print(self.nomeFabricante, carro.nomeCarro)        

motor1 = Motor('V8')
fabricante1 = Fabricante('Porsche')
motor1.insercao_Carro_Motor('Panamera')
fabricante1.insercao_Carro_Fabricante('Panamera')

motor1.listar_carros_motor()
fabricante1.listar_carros_fabricante()

# RESPOSTA PROFESSOR 
# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
#         self._motor = None
#         self._fabricante = None

#     @property
#     def motor(self):
#         return self._motor

#     @motor.setter
#     def motor(self, valor):
#         self._motor = valor

#     @property
#     def fabricante(self):
#         return self._fabricante

#     @fabricante.setter
#     def fabricante(self, valor):
#         self._fabricante = valor


# class Motor:
#     def __init__(self, nome):
#         self.nome = nome


# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome


# fusca = Carro('Fusca')
# volkswagen = Fabricante('Volkswagen')
# motor_1_0 = Motor('1.0')
# fusca.fabricante = volkswagen
# fusca.motor = motor_1_0
# print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

# gol = Carro('Gol')
# gol.fabricante = volkswagen
# gol.motor = motor_1_0
# print(gol.nome, gol.fabricante.nome, gol.motor.nome)

# fiat_uno = Carro('Uno')
# fiat = Fabricante('Fiat')
# fiat_uno.fabricante = fiat
# fiat_uno.motor = motor_1_0
# print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

# focus = Carro('Focus Titanium')
# ford = Fabricante('Ford')
# motor_2_0 = Motor('2.0')
# focus.fabricante = ford
# focus.motor = motor_2_0
# print(focus.nome, focus.fabricante.nome, focus.motor.nome)