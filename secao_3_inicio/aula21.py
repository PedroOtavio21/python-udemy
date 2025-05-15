# Aula 21 de Python

# Operadores Lógicos

"""
and (e) or (ou) not (não)

And - Todas as condições precisam ser verdadeiras. Se qualquer valor for considerado falso, a expressão inteira 
será avaliada naquele valor.

São considerados valores falsy (que você já viu):
- 0 
- 0.0
- ''
- False

Também existe o tipo None, usado para representar um valor não nulo
"""

entrada = input('[E] entrar \n[S] sair\n')
senha_digitada = input('Senha:')
senha_permitida = 'teste'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrando...') # Só será executado se as duas condições se confirmarem
else:
    print('Saindo...')

# Avaliação de curto circuito!
print(True and 0 and True)