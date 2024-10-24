# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from pathlib import Path
from datetime import datetime

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula187.txt'

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='Joao',
    valor=converte_para_brl(1_234_567),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# class MyTemplate(string.Template):
#     delimiter = '%'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read() 
    template = string.Template(texto) # MyTemplate(texto) 
    print(template.substitute(dados))   