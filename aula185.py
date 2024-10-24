# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionario
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula185.csv'

lista_clientes = [
    {'Nome': 'Luiz Otavio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'Theo Rondon', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Dudu Santos', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)

# lista_clientes = [
#     {'Luiz Otavio','Av 1, 22'},
#     {'Theo Rondon','R. 2, "1"'},
#     {'Dudu Santos','Av B, 3A'},
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)
