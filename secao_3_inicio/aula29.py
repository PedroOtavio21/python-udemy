# Aula 29 de Python

# Introdução ao Try/Except

"""
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Irei dobrar o número que você inserir a seguir: ')

try:
    print('STR:', numero)
    numero_convertido = float(numero)
    print('FLOAT:',numero_convertido)
    print(f'O dobro de {numero_convertido} é {numero_convertido * 2}')
except:
    print('O número que você inseriu não é um número')

# OBS: Esta é apenas uma introdução ao try/except. A parte mais elaborada virá mais tarde.