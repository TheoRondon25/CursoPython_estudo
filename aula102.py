import importlib

import aula102_m

print('puxando a variavel - ',aula102_m.variavel)

for i in range(10):
    importlib.reload(aula102_m) 
    print(i)
     

print('Fim')