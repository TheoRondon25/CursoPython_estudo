# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de maneira recursiva. 
# Ela gera uma sequência de tuplas, onde cada tupla possui três elementos: o diretorio atual (root),
# umalista de subdiretórios (dirs) e uma lista dos arquivos do diretório atual (files)
import os 
from itertools import count 

caminho = os.path.join('\\Users', 'theop', 'OneDrive', 'Pictures', 'Saved Pictures' )
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual - ', root)

    for dir_ in dirs:
        print(' ', the_counter, 'Dir:', dir_)

    for file_ in files:
        # print(' ', the_counter, 'File:', file_)
        caminho_completo_arquivo = os.path.join(root, file_)
        print(' ', the_counter, 'File:', caminho_completo_arquivo)
        
        # NAO FAÇA ISSO, VAI APAGAR TUDO DA PASTA 
        # os.unlink(caminho_completo_arquivo)