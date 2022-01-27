#enconding: utf-8
from cruza import *
from mutacion import *
from poda import *

resolucion = 0.001
x = [5, 7]
y = [0, 0.5]

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

individuos = generarPoblacionInicial(limSupX, limSupY, aX, aY, deltaX, deltaY, tam_pob_incial, numBitsX, numBitsY)

individuos = ordenar(individuos)

print("Generación inicial")
print("Mejor: ", individuos[0])
print("Peor: ", individuos[len(individuos)-1])
print("-----------------------------------\n")

for i in range(1, 100):
    print("Generación ", i)
    individuos = salaApareamiento(limSupX, limSupY, aX, aY, deltaX, deltaY, individuos, numBitsX, numBitsY, prob_muta_individual,prob_mut_gen)
    individuos = salaSeguimientoMutacion(aX, aY, deltaX, deltaY, limSupX, limSupY, prob_muta_individual, prob_mut_gen, individuos)
    individuos = ordenar(individuos)
    poblacionActual = len(individuos)
    if poblacionActual > tam_pob_max:
        print("Cantidad de individuos antes de poda: ", poblacionActual)
        individuos = podar(individuos, tam_pob_max)
        print("Se eliminaron: ", (poblacionActual - len(individuos)), " individuos")
    else:
        print("Sin poda: ", len(individuos))
    print("Mejor: ", individuos[0])
    print("Peor: ", individuos[len(individuos) - 1])
    print("-----------------------------------\n")
