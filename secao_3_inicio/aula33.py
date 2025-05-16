# Aula 33 de Python

# Tipos built-in em Python

"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis vistos até aqui: str, int, float, bool
"""

# Em python, eu não posso mudar o valor de variáveis imutáveis
string = 'Pedro Otávio'
print(string)
# string[3] = 't' # Esse código gerará um erro

outra_string = f'{string[:2]}t{string[3:9]}r{string[10:]}'
print(outra_string)