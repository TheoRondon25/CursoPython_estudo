# os + shutil - Copiando arquivos com python 
# 1 - Vamos copiar arquivos de uma pasta para outra
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.join(os.path.expanduser('~'), 'OneDrive') # pois a minha pasta esta dentro do onedrive, se nao era apenas o expanduser
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
