# Problema dos parametros mutaveis em funcoes Python
# se deixa uma lista vazia, ela sempre vai ser a mesma em qualquer hora que voce chame a funçao
def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_cliente('Luiz')
adiciona_cliente('Joana', cliente1)
adiciona_cliente('Fernando', cliente1)
cliente1.append('Edu')
print(cliente1)

cliente2 = adiciona_cliente('Theo')
adiciona_cliente('Taina', cliente2)
print(cliente2)
