# Aula 54 de Python - Exercício

# Exiba os itens de uma lista em sua iteração

lista = ['Pedro', 'Beatriz', 'Luciana']

# Com while
i = 0
while i < len(lista):
    print(i, lista[i])
    i += 1

# Com for
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])