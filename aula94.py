# dir, hasattr e getattr em Python
string = 'Theo'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('existe upper')
    print(string.upper())
# mesma coisa, mas de forma dinamica:
if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('Nao existe o metodo', metodo)


# iniciar com o debug e ir em debug console para utilizar o "dir" por exemplo e etc