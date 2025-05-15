# Aula 28 de Python - Exercício 3

"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Se o nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira palavra do seu nome é {primeira_letra}
        A última palavra do seu nome é {ultima_letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você digitou campos vazios"
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome contém espaços? {'Sim' if (' ' in nome) else 'Não'}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'Primeira letra do seu nome: {nome[0]}')
    print(f'Última letra do seu nome: {nome[-1]}')
else:
    print('Desculpe, você digitou campos vazios') 