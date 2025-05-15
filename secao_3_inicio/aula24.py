# Aula 24 de Python 

# Operadores "in" e "not in" -> "está entre" e "não está entre"

"""
Parta do pressuposto que: strings são iteráveis.

Entenda que paralavras em strings podem ser acessadas a partir de seu índice, indicando sua posição. 
No caso abaixo, a letra "t", no qual está na segunda posição, pode ser acessada pelo índice "1".
   0 1 2 3 4 5
   O t á v i o

Isso ocorre por que na programação, strings e vetores (visto mais afrente) são acessadas a partir do indice 0,
incrementando o seu valor quanto mais acesso os valores das variáveis.
"""
palavra = input('Digite uma palavra qualquer:')
teste_palavra = input('Digite uma outra palavra para verificação:')

if teste_palavra in palavra:
    print(f'{teste_palavra} está em {palavra}')
else:
    print(f'{teste_palavra} não está em {palavra}')