# Try, except, else e finally
# a= 18
# b = 0
# c = a / b

try:
    a= 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)

except NameError:
    print('Nome b nao esta definido.')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Nome:', error.__class__.__name__)

except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUAR')

# PARTE COM ELSE 

# try: 
#     print('ABRIR ARQUIVO')
#     8/0
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
#     print('DIVIDIU ZERO')
# else: 
#     print('Nao deu erro')
# finally:
#     print('FECHAR ARQUIVO')