# Aula 27 de Python

# Fatiamento de strings

"""
 012345678
 Olá Mundo
-987654321

A prática abaixo é ótima para iteração de elementos, "recortando" a variável
Fatiamento [inicio:final:passo] [::]

Obs.: a função len retorna a quantidade de caracteres da string
"""

variavel = 'Olá Mundo'
print(variavel[4:]) # Realiza a iteração a partir do elemento 4
print(variavel[0:len(variavel):1]) # Realiza a iteração, de 0 ao final do elemento, de 1 em 1
print(variavel[::-1]) # Realiza a iteração invertida