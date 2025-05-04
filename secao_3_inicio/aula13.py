# Aula 13 de Python

# Introdução às 'f-strings' (Formatação de strings)

# Variáveis
nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / (altura ** 2)

"""
- Basicamente você salva uma string em uma variável, precedida de um 'f'
- Para inserir uma variável na string, você utiliza o nome da variável entre chaves '{}'
- Para formatar dados numéricos, você passa ':' após a variável, seguidos da quantidade de casas
"""

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

# Saída de código:
print(linha_1)
print(linha_2)
print(linha_3)
