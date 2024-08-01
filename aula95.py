import sys

# Generator expression, Iterables e Iterators em python
iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable)
lista = [n for n in range(100)]
generator = (n for n in range(100))

print('tamanho da lista -', sys.getsizeof(lista))
print('tamanho do generator -',sys.getsizeof(generator))

# for n in generator:
#     print(n)