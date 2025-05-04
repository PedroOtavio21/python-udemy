# Aula 15 de Python 

# Coleta dados do terminal com função input()

"""
- Toda linguagem de programação possui um método similar, onde realiza uma leitura de um dado no terminal
- OBS: Assim como em JavaScript, ele salva o dado, mas como String!
"""

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Insira um primeiro número: ')
numero_2 = input('Insira um segundo número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma de {int_numero_1} com {int_numero_2} é {int_numero_1 + int_numero_2}')