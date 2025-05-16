# Aula 40 de Python - Exercício

# Cálculadora com While

while True:
    num_1 = input('Insira um primeiro número qualquer: ')
    num_2 = input('Insira um segundo número qualquer: ')
    operador = input('Insira a operação escolhida: (+), (-), (*), (/) ')

    # Flag para validar se elementos terão erro ou não
    numeros_validos = None

    # Variáveis de conversão
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    # Validação para verificação de Flag 
    if numeros_validos is None:
        print('Um dos elementos são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    # Validação para verificar se operação está contida em operadores_permitidos
    if operador not in operadores_permitidos:
        print('Operação inserida inválida.')
        continue

    # Validação para verificar se foi digitado mais de um elemento necessário
    if len(operador) > 1:
        print('Digite apenas 1 operador.')
        continue
    
    # Operações da calculadora
    if operador == '+':
        resultado = num_1_float + num_2_float
        print(f'{num_1_float} + {num_2_float} = ', resultado)
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(f'{num_1_float} - {num_2_float} = ', resultado)
    elif operador == '*':
        resultado = num_1_float * num_2_float
        print(f'{num_1_float} * {num_2_float} = ', resultado)
    elif operador == '/':
        resultado = num_1_float / num_2_float
        print(f'{num_1_float} / {num_2_float} = ', resultado)
    else:
        print('Se chegou até aqui, ocorreu algum erro misterioso :(')

    """
    O trecho abaixo deixa o conteúdo em minúsculo, além de verificar se o elemento começa com 's'
    """
    sair = input('Você deseja sair? Informe com [S]im ou [N]ão').lower().startswith('s') 
    if sair:
        print('Saindo da aplicação.')
        break