# Aula 22 de Python

# Operadores Lógicos

"""
and (e) or (ou) not (não)

Or - Qualquer condição verdadeira avalia toda a condição com verdadeira. Ou seja,
caso só será falso se todas as condições forem falsas.

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

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrando...') # Só será executado se as duas condições se confirmarem
else:
    print('Saindo...')

# Avaliação de curto circuito!
print(True or 0 or True or 'abc')

senha = input('Senha:') or 'Sem senha.'
print(senha) # Caso não insira nada e só aperte enter, será exibido: 'Sem senha.'