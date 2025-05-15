# Aula 32 de Python - Exercício

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input('Insira um número inteiro qualquer: ')
numero_inteiro_convertido = ...

if numero_inteiro.isdigit():
    numero_inteiro_convertido = int(numero_inteiro)

    if numero_inteiro_convertido % 2 == 0:
        print(f'O número inteiro inserido ({numero_inteiro_convertido}) é par!')
    else:
        print(f'O número inteiro inserido ({numero_inteiro_convertido}) é impar!')

else:
    print('O valor que você inseriu não é numérico!')
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Insira o seu horário atual (em horas): ')
horas_convertidas = int(horas)

if horas_convertidas >= 0 and horas_convertidas < 12:
    print('Bom dia!')
elif horas_convertidas < 18:
    print('Boa tarde!')
elif horas_convertidas < 24:
    print('Boa noite!')
else:
    print('Valor inserido é incorreto.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

user_name = input('Insira o seu nome: ')
user_name = user_name.strip() # retorna a variável sem espaços

if user_name and not user_name.isdigit():
    if len(user_name) <= 4:
        print('O seu nome é curto')
    elif len(user_name) <= 6:
        print('Seu nome é normal')
    elif len(user_name) > 6:
        print('Seu nome é muito grande')
else:
    print('Valor inválido. Insira um nome válido, contendo apenas letras.')