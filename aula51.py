"""
Introducao ao desempacotamento 
"""
nome1, nome2, nome3 = ['Theo', 'Taina', 'Rondon']
print(nome1, nome2, nome3)

nome1, *resto = ['Theo', 'Taina', 'Rondon']
print(nome1, resto)

_, nome, *_ = ['Theo', 'Taina', 'Rondon']
print(nome)