# Aula 34 de Python

# Repetições

"""
while (enquanto)
- Executa uma operação/bloco de código enquanto for verdadeiro
- Ótimo para realizar uma condição quando não se sabe onde irá terminar
"""

condicao = True
while condicao:
    nome = input('Qual é o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break # garante que não ocorra um loop infinito, encerrando o loop
