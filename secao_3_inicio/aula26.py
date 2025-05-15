# Aula 26 de Python

# Formatação de strings

"""
     s - string
     d - int
     f - float
x ou X - Hexa decimal
     > - Esquerda
     < - Direita
     ^ - Centro
 Sinal - + ou -
.<número de dígitos>f
(Caractere)(><^)(quantidade)

Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:=^11}')

print(f'{1000.95347621:.1f}')