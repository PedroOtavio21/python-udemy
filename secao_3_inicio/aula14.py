# Aula 14 de Python

# Formatação de strings com método format()

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos' # 23 tem Luiz anos
print(formato.format(nome, idade))
print(formato)

# formato = '{n} tem {i} anos'
# print(formato.format(n=nome, i=idade))

# Outra coisa interessante de entender, é que format é uma espécie de tupla
# ou seja, contém seus próprios indices
# string = 'Valor de a = {0} Valor de b = {1} Valor de c = {2:.2f}'

# É possível passar os parâmetros em format como parâmetros nomeados!
# OBS: Tudo que vier em seguida de um parâmetro nomeado, também deverá ser nomeado
# string = 'Valor de a = {} Valor de b = {} Valor de c = {nome3:.2f}'
# string.format(a, b, nome3=c)