#enconding: utf-8
from generacion import *
from cruza import *

resolucion = 0.005
x = [5, 8]
y = [0.4, 0]

RX = abs(x[1] - x[0])
RY = abs(y[1] - y[0])

limSupX = (RX/resolucion) + 1
limSupY = (RY/resolucion) + 1

aX = x[0]
aY = y[0]
numBitsX = definirBits(limSupX)
numBitsY = definirBits(limSupY)
tam_pob_incial = 6
prob_muta_individual = 0.1
prob_mut_gen = 0.05
tam_pob_max = 8
deltaX = RX/(2**numBitsX)
deltaY = RY/(2**numBitsY)

#breakpoint()
individuos = generarPoblacionInicial(limSupX, limSupY, aX, aY, deltaX, deltaY, tam_pob_incial, numBitsX, numBitsY)

individuos = ordenar(individuos)

salaApareamiento(limSupX, limSupY, aX, aY, deltaX, deltaY, individuos,numBitsX,numBitsY)
