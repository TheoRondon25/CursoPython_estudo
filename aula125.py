# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# Positional-only Parameters (/)
def soma(a, b, /, x, y):
    print(a + b + x + y)

soma(1, 2, 3, y=3)

# Keyword-Only Arguments (*)
def soma(a, b, *, c, **kwargs): # tudo que vier antes do * é argumento posicional, tudo que vem depois é argumento nomeado
    print(kwargs)
    print(a + b + c) 

# nada impede de que na chamada, eu coloque argumento nomeado para o que vem antes do *
soma(1, 2, c=3, nome='teste') 