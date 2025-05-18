# Aula 50 de Python

# Outros métodos úteis em listas

"""
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove um item no final ou no índice escolhido
    del - Apaga um indice
    clear - Limpa a lista
    extend - Aumenta/estende o tamanho da lista
    + - Concatena strings
"""

lista = [10, 20, 30, 40, 50]
lista.append('Pedro')

nome = lista.pop()

print(lista, f'Elemento removido: {nome}')

lista.append(1453)
del lista[-1]

# Adiciona um elemento no índice desejado 
lista.insert(0, 5) # insert(indice, elemento)

# Limpa a lista, removendo todos os elementos
# lista.clear() 

print(lista)