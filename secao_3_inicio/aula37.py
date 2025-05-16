# Aula 37 de Python

# Uso do while + continue

"""
- Assim como o break, o continue é usado em conjunto com o while mais próximo de seu contexto
- No entanto, o continue serve para "ignorar" um determinado trecho de código
"""

contador = 0
while contador < 10:
    contador += 1

    if contador > 5 and contador < 8: # serão pulados o 6 e 7
        continue
    
    print(contador)

print('Fim de execução.')