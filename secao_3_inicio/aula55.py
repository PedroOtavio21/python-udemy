# Aula 55 de Python

# Introdução ao desempacotamento

nome_1, nome_2, nome_3 = ['João', 'Luiz', 'Davi']

print(nome_1, nome_2, nome_3)

"""
Note que é necessário que a quantidade de variáveis corresponda ao número de elementos da lista

- nome1, nome2 = ['Pedro', 'Maria', 'Lucia'] -> Gerará erro
- nome1, nome2, nome3, nome4 = ['Pedro', 'Maria'] -> Gerará erro
"""

"""
Caso você precise desestruturar, porém só precise de 1 dos valores, é usada a seguinte convenção:
"""

valor, *_= [15, 33, 55]
print(valor, _) 