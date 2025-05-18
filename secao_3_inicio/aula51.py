# Aula 51 de Python

# Concatenando e Extendendo listas

lista_a = [1,2,3]
lista_b = [4,5,6]

lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # junta 2 listas em uma

print(lista_a)
print(lista_b)
print(lista_c)
print(lista_d) # Retornará None, com a alteração feita na lista_a