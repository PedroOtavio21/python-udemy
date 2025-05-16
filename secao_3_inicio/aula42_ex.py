# Aula 42 de Python - Exercício

"""
Exercício:
- Contar quantas vezes uma palavra dentro de uma frase se repetiu

OBS.: Verifique a questão dos espaços em frase
Método count() -> retorna a quantidade de vezes que se uma palavra se repetiu dentro de uma frase.
"""

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'.strip()

apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

i = 0
while i < len(frase):
    letra_atual = frase[i]

    # Garante que a letra lida não será um espaço
    if letra_atual == ' ':
        i += 1
        continue

    qtd_aparicoes_letra_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < qtd_aparicoes_letra_atual:
        apareceu_mais_vezes = qtd_aparicoes_letra_atual
        letra_apareceu_mais_vezes = letra_atual
    
    print(letra_atual, qtd_aparicoes_letra_atual)
    i += 1

print(f'letra que mais se repetiu: "{letra_apareceu_mais_vezes}", quantidade = {apareceu_mais_vezes}')