# Aula 52 de Python

# Cuidados com dados Mutáveis

"""
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
"""

# Ocorre apenas uma cópia (imutáveis)

# nome = 'Pedro'
# nome_outra_variavel = nome
# nome = 'João'

# print(nome)
# print(nome_outra_variavel)

# Aponta para o mesmo endereço (mutáveis)
# lista_a = ['João', 'Maria']
# lista_b = lista_a

# lista_a[0] = 'Qualquer coisa'
# print(lista_b) # ocorre uma alteração na lista b, sem que tenha ocorrida uma mudança nela em expecífico

# Caso queira fazer algo similar ao primeiro caso, faça:
lista_a = ['João', None, 1.25, 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b) # Diferente de antes, lista b não foi alterada