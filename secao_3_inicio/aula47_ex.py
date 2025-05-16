# Aula 47 de Python - Exercício

"""
Faça um jogo para o usuário adivinhar qual a palavra secreta
- Você irá propor uma palavra secreta qualquer e vai dar a possibilidade do usuário digitar apenas uma letra.
- Quando o usuário inserir uma letra, você irá conferir se a letra digitada está na palavra secreta
    - Se a letra estiver na palavra secreta, exiba a letra
    - Se a letra não estiver na palavra secreta, exiba *

Faça uma contagem de tentativas do usuário
"""

"""
1. Pegar letra letra do usuário (Ex.: e)
2. Comparar com palavra especial escolhia anteriormente
    2.1. Se for igual, exibe a letra na palavra especial
    2.2. Se não, exibe o '*'
    Ex.: 'e' está contido em 'alegre'? -> Sim
    print('**e**e')
"""

palavra_secreta = 'Teste'.lower()

letras_acertadas = ''
tentativas = 0
while True:
    letra_usuario = input('Insira uma letra qualquer: ').lower()

    if len(letra_usuario) > 1:
        print('Você deverá inserir apenas uma letra.')
        continue

    if letra_usuario.isdigit():
        print('Você deverá inserir uma letra, não um número')
        continue

    tentativas += 1
    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palavra_construida = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_construida += letra
        else:
            palavra_construida += '*'
    
    if palavra_construida == palavra_secreta:
        print(f'Parabêns! Você encontrou a palavra escolhida em {tentativas} tentativas!')
        print(palavra_construida)
        break
    else:
        print(palavra_construida)
        print(f'Quantidade de tentativas: {tentativas}')