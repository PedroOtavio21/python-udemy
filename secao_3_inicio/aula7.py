# Aula 7 de Python

# Introdução às variáveis

"""
- As variáveis são usadas para salvar um dado qualquer na memória de seu computador
- Segundo a PEP8 (Guia de estilo de código Python): 
    1. inicie variáveis com letras minúsculas
    2. Podem ser usados números e underline (Ex.: nome_aluno, nota3, etc)
    3. Em Python, é comum o uso de Snake Case em nomenclatura de variáveis!

- O sinal "=" é um operador de atribuição. Ou seja, ele serve para atribuir um valor qualquer a uma variável
    Uso: nome_variavel = valor_dado
    Ex.: nome = 'Pedro'; nota = 7.5
"""

full_name = 'Pedro Otávio de Sousa Bezerra'
print('Seu nome é', full_name, sep=' ')

dois_vezes_cinco = 2 * 5
print('2 x 5 = ', str(dois_vezes_cinco), sep='')

idade = 22
maior_idade = 'Sim' if idade >= 18 else 'Não' # Operador ternário
print('É maior de idade? ', maior_idade, sep='')