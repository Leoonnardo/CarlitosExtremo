import random
from generacion import *

def salaSeguimientoMutacion(aX, aY, deltaX, deltaY, limSupX, limSupY, probMutaInd, probMutaGen, individuos):
    #breakpoint()
    for i in individuos:
        probMuta = random.random()

        if probMuta <= probMutaInd:
            posicion = individuos.index(i)
            i[1][0] = mutar(probMutaGen, i[1][0])
            i[1][1] = mutar(probMutaGen, i[1][1])

            i = medirMutacion(aX, aY, deltaX, deltaY, i)

            individuos[posicion] = i

    for i in individuos:
        if descartarIndividuo(i, limSupX, limSupY):
            indice = individuos.index(i)
            individuos.pop(indice)
    return individuos



def mutar(probMutaGen, genes):

    for i in range(len(genes)):
        prob = random.random()
        if prob <= probMutaGen:
            gen = genes[i]
            if gen:
                genes[i] = 0
            else:
                genes[i] = 1


    return genes

def medirMutacion(aX, aY, deltaX, deltaY, individuo):
    individuo[2][0] = binarioToDecimal(individuo[1][0])
    individuo[2][1] = binarioToDecimal(individuo[1][1])
    individuo[3][0] = definirFenotipo(aX, individuo[2][0], deltaX)
    individuo[3][1] = definirFenotipo(aY, individuo[2][1], deltaY)
    individuo[4] = definirAptitud(individuo[3][0],individuo[3][1])

    return individuo

def descartarIndividuo(individuo, limSupX, limSupY):
    if(individuo[2][0] <= limSupX) and (individuo[2][1] <= limSupY):
        return False

    return True