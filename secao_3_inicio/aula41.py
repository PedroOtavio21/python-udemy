# Aula 41 de Python

# while/else

"""
- Funciona como um trecho de código "default"
- Ou seja, será executado sempre ao final do bloco while, 
a não ser que seja interrompido por um break, por exemplo
"""

string = 'Valor'

i = 0
while i < len(string):
    letra = string[i]
    print(letra, end=' ')
    i += 1
else:
    print('Fim da execução.')
print('Fora do while.')