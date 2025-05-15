# Aula 23 de Python

# Operador lógico "not"

"""
Usado para inverter resultados de expressões lógicas
Ex.: 
- not True => False
- not False => True
"""

senha = input('Insira sua senha:')

if not senha:
    print('Senha digitada incorreta')
else:
    print('Entrando na sua conta!')