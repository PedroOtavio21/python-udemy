# Aula 45 de Python

# O loop For por debaixo dos panos

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

numeros = range(0, 100, 5)

for numero in numeros:
    print(numero)