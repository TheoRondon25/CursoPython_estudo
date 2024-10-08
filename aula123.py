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
import os

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


tarefas = []
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

    # if entrada.lower() == 'listar':
    #     listar(tarefas)
    #     continue
    # elif entrada.lower() == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     continue
    # elif entrada.lower() == 'refazer':
    #     refazer(tarefas, tarefas_refazer)  
    #     continue
    # elif entrada == 'cls':
    #     os.system('cls')
    #     continue
    # else:
    #     adicionar(entrada, tarefas)
    #     continue



