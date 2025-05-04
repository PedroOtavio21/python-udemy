# Aula 4 de Python

# Tipos int e float (Number)

""" int -> Número inteiro
- O tipo int representa qualquer número inteiro positivo/negativo
- O int sem sinal é considerado positivo
"""
print("Números inteiros:")
print(2025)
print(-145)

""" float -> Número com ponto flutuante
- O tipo float representa qualquer número de ponto flutuante positivo/negativo
- O float sem sinal é considerado positivo
"""
print('Número de ponto flutuante')
print(1.74)
print(-213.7)

# Função type()

# A função (método na verdade!) type mostra o tipo em que o Python inferiu o valor
# Entenda o seguinte: Tudo em python é dado como um Objeto!
print(type(1.74))
print(type("Olá mundo!"))
print(type(False)) # Será visto mais para frente