# Aula 43 de Python 

# Introdução ao loop for

"""
Segue abaixo uma comparação entre os Loops While e For
1. O While geralmente é usado para loops onde não se sabe quando terminará
2. O For é mais usado para quando se sabe do limite de um loop.
"""
texto = 'Python'

# While

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print('O laço acima poderá ter repetições infinitas.')

# For

texto = 'Python'

novo_texto = ''
for letra in texto:
    print(letra, end=' ')
    novo_texto += f'*{letra}'

print(novo_texto)