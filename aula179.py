# os + shutil - Copiando arquivos com python 
# 1 - Vamos copiar arquivos de uma pasta para outra
# Copiar -> shutil.copy
# Copiar Arvore recursivamente -> shutil.copytree
# Apagar Arvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.join(os.path.expanduser('~'), 'OneDrive') # pois a minha pasta esta dentro do onedrive, se nao era apenas o expanduser
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)