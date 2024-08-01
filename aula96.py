# Introduçao às generator functions em python
# generator = (n for n in range(1000000))

# def generator(n=0):
#     yield 1 # Pausar
#     print('Continuando...')
#     yield 2
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'ACABOU'

def generator(n=0, maximium=10):
    while True:
        yield n
        n += 1

        if n > maximium:
            return

gen = generator(maximium=8)
for n in gen: 
    print(n)
