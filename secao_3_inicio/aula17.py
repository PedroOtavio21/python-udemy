# Aula 17 de Python

# Continuação com exemplos de aula anterior

condicao = True

if condicao:
    print('Este código será executado dentro do primeiro condicional. (IF)') # Será executado
else:
    print('Este código será executado dentro do primeiro condicional. (ELSE)')

if 10 != 10:
    print('Este código será executado dentro do segundo condicional. (IF)')
else:
    print('Este código será executado dentro do segundo condicional. (ELSE)') # Será executado

print('Este código estará fora do bloco condicional')

"""
Extra: caso você queira escrever um trecho de código, porém não tem uma lógica formulada na cabeça, 
utilize o seguinte

1. Palavra reservada pass
- Ela apenas pula para o trecho de código seguinte
- Ex.:

if condicao:
    pass 
    
2. Elipse (...)
- Funciona como uma espécie de placeholder, indicando que algo será implementado futuramente naquele trecho 
em específico
- Ex.:

if condicao:
    ... 
"""