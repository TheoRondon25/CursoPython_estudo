"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento  [i:f:p] [::]
obs.: a funcao len retorna a quantidade de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) # vai ate o final
print(variavel[4:8]) # vai ate o 7 (um a menos)
print(variavel[:5]) # vai começar do começo (omitindo o numero inicial)
print((variavel[0:9:1])) # começa do 0 e vai ate o 9 de 1 em 1
print((variavel[-1:-10:-1]))

print(len(variavel)) # quantidade de caracteres 
print(len(variavel[3:])) 
