"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Theo Rondon'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC' # nao funciona nesse caso, pois string é imutavel
print(string)
print(outra_variavel)
print(string.zfill(30)) 