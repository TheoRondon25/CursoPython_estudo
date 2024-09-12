# Metodo especial __call__
# callable é algo que pode ser executado com parenteses
# Em classes normais, __call__ faz a instancia de uma classe "callable"
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'esta chamando', self.phone)
        return 1234


call1 = CallMe('14991044138')
retorno = call1('Theo Rondon')
print(retorno)