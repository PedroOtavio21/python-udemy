# Aula 46 de Python

# Similaridades do for com while

for i in range(10):
    # O valor 2 não será exibido na iteração
    if i == 2:
        print('i é 2, pulando ...')
        continue

    # O código será interrompido ao chegar no 8
    if i == 8:
        print('i é 8, seu else não executará')
        break

    # O código irá executar um segundo loop de iteração, de 1 a 3, em cada elemento do primeiro loop
    for j in range(1, 3):
        print(i, j)
else:
    # Execução "garantida" ao final do loop
    print('For finalizado com sucesso')