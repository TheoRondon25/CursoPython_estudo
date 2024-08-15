import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# caminho_arquivo = 'C:\\Users\\theop\\OneDrive\\Documents\\curso_python\\'
caminho_arquivo = 'aula120.txt'

# arquivo = open(caminho_arquivo, 'w') # modo que quero utilziar
#
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo: # abre e fecha o arquivo
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0) # move o cursor para o topo
#     print(arquivo.read()) # podemos ler aqui se estiver no modo com + (possibilitando leitra e escrita)
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('------------------')

# # fora dessa abertura, o arquivo esta fechado
# # entao para ler, devemos abrir novamente com o modo de leitura
# with open(caminho_arquivo, 'r') as arquivo: 
#     print(arquivo.read())

# with open(caminho_arquivo, 'a+') as arquivo: # a - nao apaga e insere a informaçao com o que ja tem
# with open(caminho_arquivo, 'b') as arquivo: # b - abre o arquivo em modo binario, nao sendo muito util quando se trata de texto
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo: # w - apaga o que tinha e escreve o novo
    arquivo.write('Atenção\n') 
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo) # remove o arquivo
# os.remove(caminho_arquivo) # faz o mesmo que o unlink
# os.rename(caminho_arquivo, 'aula120-2.txt') # renomeia o arquivo ou move o arquivo
