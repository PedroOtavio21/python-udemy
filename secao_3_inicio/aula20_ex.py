# Aula 20 de Python

# Exercício utilizando operadores condicionais

"""
1. Leia dois valores quaisquer
2. Mostre por print qual dos dois é o maior valor
"""

primeiro_valor = input('Insira um primeiro valor qualquer: ')
segundo_valor = input('Insira um segundo valor qualquer: ')

primeiro_valor_convertido = int(primeiro_valor)
segundo_valor_convertido = int(segundo_valor)

if primeiro_valor_convertido > segundo_valor_convertido:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(primeiro_valor_convertido, segundo_valor_convertido))
elif primeiro_valor_convertido < segundo_valor_convertido:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(segundo_valor_convertido, primeiro_valor_convertido))
else:
    print('Os dois valor inseridos ({} e {}) são iguais'.format(primeiro_valor_convertido, segundo_valor_convertido))