# Aula 48 de Python

# Listas em Python

"""
- Tipo List -> Mutável
- Suporta vários valores de qualquer tipo
- Conhecimento reutilizáveis - índices e fatiamento
- Métodos úteis: append, insert, pop, del, clear, extend, etc
"""

# Strings - Cadeia de Caracteres

"""
- Possui geralmente as mesmas características de uma lista 
- Porém cada posição contém apenas 1 caractere
- Ela é imutável!!!
"""
string = 'ABCDE'

# Formas de se iniciar uma lista:
lista_1 = list() # ''
lista_2 = [] # ''

print(lista_1, type(lista_1))
print(lista_2, type(lista_2))

# permique uma lista de valores diferentes
lista_2 = [14, 1.25, 'Pedro Otávio', False, [2,4,6,8,10]] 
lista_2[2] = 'João Guilherme'
print(lista_2)

# Você pode acessar os elementos por indices, como nas strings, porém você acessa todo o item da posição!
print(lista_2[2])
print(lista_2[4])