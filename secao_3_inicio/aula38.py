# Aula 38 de Python

# Whiles consecutivos


"""
O código abaixo seria como algo similar a leitura de elementos contidos dentro de matrizes.
A ideia é entender que sempre será executado o código mais intero, finalizando o externo.
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1

print('Acabou')