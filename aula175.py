# os.listdir para navegar em caminhos 
# C:\Users\theop\OneDrive\Pictures\Saved Pictures
# caminho = r'C:\\Users\\theop\\OneDrive\\Pictures\\Saved Pictures'
import os 
caminho = os.path.join('\\Users', 'theop', 'OneDrive', 'Pictures', 'Saved Pictures' )
# print(caminho)
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue 

    for imagem in os.listdir(caminho_completo_pasta):
        print(' ', imagem)