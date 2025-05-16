# Aula 35 de Python

# Continuação de aula 34:

"""
Formas de tratar o loop while:
- Trabalhe com uma variável que tenha seu valor alterado, até atingir a condição do loop
- Dessa forma, não entrará em loop infinito
Ex.:
variavel_contadora = 0
while variavel_contadora < 5:
    variavel_contadora = variavel_contadora + 1
    print(variavel_contadora)
"""

contador = 0 # variavel atrelada ao condicional
while contador <= 10:
    print('Código sendo executado.')
    print(contador)
    contador = contador + 1 # garante que não terá loop infinito

print('Acabou.')