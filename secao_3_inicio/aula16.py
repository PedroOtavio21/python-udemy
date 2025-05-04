# Aula 16 de Python

# Introdução às operações condicionais

""" Como seriam feitos os trechos de código para resolver as seguintes situações?

entrada = input('Você gostaria de "entrar" ou "sair"? ')

print('Você escolheu "entrar" no sistema') # Caso seja entrar
print('Você escolheu "sair" do sistema') # Caso seja sair
"""

""" Solução
- Utilização de condicionais if / else
- Em python, funcionam da seguinte forma:
    if | elif (0 ou mais vezes) | else
"""

entrada = input('Você gostaria de "entrar" ou "sair"? ')
entrada_convertida = entrada.lower()

if entrada_convertida == 'entrar':
    print('Você escolheu "entrar" no sistema') # Caso seja entrar
elif entrada_convertida == 'sair':
    print('Você escolheu "sair" do sistema') # Caso seja sair
else:
    print('Você não digitou nem "entrar" ou "sair".')