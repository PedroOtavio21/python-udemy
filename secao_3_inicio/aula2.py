# Aula 2 de Python

# Função "print"

"""
- Faz parte das chamadas funções, existentes em várias linguagens de programação
- Tem como papel exibir um texto ou variável qualquer na saída do terminal
- Podem ser passados mais de um argumento em seus trechos de código.
"""

print("Este é o hello world em python.") # O argumento passado é um argumento nomeado!

""" Argumento "sep"
- Esse argumento é responsável para utilizar um determinado valor entre os argumentos passados no print
- Ex.: print("Guarda","Chuva", sep="-")
- Saída: Guarda-Chuva
"""

print("O meu nome é", "Pedro", sep=': ')

""" Argumento "end"
- É um argumento que passará algum valor após o final da linha do trecho de código
- Por padrão, ele realiza uma quebra de linha, com "\n" (Caractere especial que realiza a quebra de linha)
- Ex.: print("O meu nome é:", "Pedro\n", sep=" ", end="\n") + print("Olá", "Pedro!", sep=", ")
"""

print("Eu estou confuso ", end="...")