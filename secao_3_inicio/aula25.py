# Aula 25 de Python

# Interpolação básica de strings

"""
    s - string
d e i - int
    f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total foi de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))