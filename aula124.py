# EXERCICIO - LISTA DE TAREFAS COM OPÇOES DE DESFAZER E REFAZER
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
# EXERCICIO DE AGORA -> SALVAR OS DADOS EM UM JSON
import os
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for entrada in tarefas:
        print(f'\t{entrada}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    entrada = tarefas.pop()
    print(f'{entrada=} removida da lista de tarefas')
    tarefas_refazer.append(entrada)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    entrada = tarefas_refazer.pop()
    tarefas.append(entrada)

    print()
    print(f'{entrada=} adicionada na lista de tarefas')
    print()
    listar(tarefas)


def adicionar(entrada, tarefas):
    print()
    entrada = entrada.strip()
    if not entrada:
        print('Voce nao digitou uma tarefa')
        return
    
    print(f'{entrada=} adicionada na lista de tarefas')
    tarefas.append(entrada)
    print()
    listar(tarefas)

# LENDO JSON (SE NAO TIVER NENHUM, CRIA O ARQUIVO PUXANDO A FUNÇAO SALVAR)
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados

# CRIANDO E SALVANDO JSON
def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula124.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer, refazer')
    entrada = input('Digite uma tarefa ou um comando: ')

    comandos = { 
        'listar': lambda: listar(tarefas), # atrasando a execuçao da funçao com outra funçao (lambda)
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'cls': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(entrada, tarefas),
    }
    comando = comandos.get(entrada) if comandos.get(entrada) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)




