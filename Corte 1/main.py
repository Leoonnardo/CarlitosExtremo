from generacion import *

resolucion = 0.005
x = [-0.4,0.4]
y = [-0.4,0.4]

RX = x[1] - x[0]
RXnew = abs(RX)
RY = y[1] - y[0]
RYnew = abs(RY)

valoresX = RXnew / resolucion + 1
valoresY = RYnew / resolucion + 1 

aX = x[0]
aY = y[0]
tam_pob_incial = 4
prob_muta_individual = 0.1
prob_mut_gen = 0.05
tam_pob_max = 8

# Bits de valores
def num_Bits(valor):
    aux=0
    i=1
    bits=0
    while aux <= valor:
        aux=pow(2, i)
        bits=i
        i=i+1
    return bits

# Binario a Decimal
def binario_to_Decimal(binario):
    decimal = 0
    i = 0
    while (binario>0):
        digito  = binario%10
        binario = int(binario//10)
        decimal = decimal+digito*(2**i)
        i = i+1
    # SALIDA
    return decimal