# Aula 30 de Python

# Introdução à boas práticas de código

"""
CONSTANTE = "Variáveis" que não irão mudar seu valor
Muitas condições em um mesmo if (ruim)
    <- contagem de complexiade (ruim)
"""

"""
A ideia desta aula é a seguinte:
- Se beneficie de variáveis para melhor entendimento do código
- Utilize de constantes para melhor visualização de código
- Comente o que for necessário para melhor entendimento
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima permitida do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

radar_range_minimo = LOCAL_1 - RADAR_RANGE
radar_range_maximo = LOCAL_1 + RADAR_RANGE

if velocidade > RADAR_1:
    print('O carro ultrapassou a máxima permitida no radar 1')

if local_carro >= radar_range_minimo and radar_range_maximo and velocidade > RADAR_1:
    print('Carro multado em radar 1')