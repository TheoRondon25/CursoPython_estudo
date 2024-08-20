# EXERCICIO - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instancias da classe com os arquivos salvos
# Faça em arquivos separados
import json 

CAMINHO_ARQUIVO = 'aula132.json'

class Pessoa:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

p1 = Pessoa('Theo', 20, 'Rondon')
p2 = Pessoa('Taina', 19, 'Libanori')
bd = [p1.__dict__, p2.__dict__]

print()
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()

