# Aula 49 de Python

# Alteração em listas

"""
CREATE READ UPDATE DELETE
Criar Ler Alterar Apagar = lista[i]  (CRUD)
"""

# Criação de lista
lista = [10, 20, 30, 40]

# Atualização de lista
lista[2] = 300

# Adicionar itens na lista
lista.append(50) # Adiciona um valor ao final da lista

# Remover elemento da lista
del lista[3] # Evite utilizar este comando com muitos elementos
ultimo_item = lista.pop() # Remove o último elemento da lista
# ultimo_item = lista.pop(2) # Também remove o item pelo índice que preferir, não sendo apenas pelo último

print(f'Último item da lista: {ultimo_item}')

print(lista)