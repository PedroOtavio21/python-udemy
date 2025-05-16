# Aula 39 de Python - Exercício

# Iteração de strings com while

"""
1. Receber uma string qualquer
2. Realizar um loop while para iterar na string
3. A cada iteração, incluir o valor do elemento da string em 
uma nova string, no seguinte formato:
- '*' + string[indice]; Ex.: '*P' + '*e' + '*d' + '*r' + '*o'
"""

"""
Extra: Inclua um tratamento de erro condicional!
"""

nome = input('Insira um nome qualquer: ')
tamanho_nome = len(nome)

if nome and not nome.isdigit():
    novo_nome = ''
    indice = 0
    while indice < tamanho_nome:
        novo_nome += '*' + nome[indice]
        indice += 1

    print(nome)
    print(novo_nome)
else:
    print('Insira um nome não vazio, contendo apenas letras.')
