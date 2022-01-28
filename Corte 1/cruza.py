import random

from mutacion import *
def ordenar(individuos):
    auxC = []
    aux = individuos
    poblacion = len(individuos)

    contador = 0

    while contador < poblacion:
        #breakpoint()
        mayor = 0
        posicion = 0
        for i in aux:
            if i[4] > mayor:
                mayor = i[4]
                posicion = individuos.index(i)
        auxC.append(aux.pop(posicion))
        contador += 1

    return auxC

def salaApareamiento(limSupX, limSupY, aX, aY, deltaX, deltaY, lista,numBitsX,numBitsY, probMutaInd, probMutaGen):
    individuoApto = lista[0]
    nuevos = []
    for i in range(len(lista)):
        if(i != 0):
            nuevo = cruza(aX, aY, deltaX, deltaY, individuoApto, lista[i], numBitsX, numBitsY)

            #breakpoint()
            if((nuevo[2][0] <= limSupX) and (nuevo[2][1] <= limSupY)):
                nuevos.append(nuevo)
            nuevo2 = cruza(aX, aY, deltaX, deltaY, individuoApto, lista[i], numBitsX, numBitsY)
            #breakpoint()
            if ((nuevo2[2][0] <= limSupX) and (nuevo2[2][1] <= limSupY)):
                nuevos.append(nuevo2)


    nuevos = salaSeguimientoMutacion(aX, aY, deltaX, deltaY, limSupX, limSupY, probMutaInd, probMutaGen, nuevos)

    lista.extend(nuevos)
    nuevos = ordenar(lista)

    return nuevos




def cruza(aX, aY, deltaX, deltaY, indA,indB,numBitsX, numBitsY):
    nombre = indA[0]+indB[0]
    if(len(nombre) > 10):
        lista = list(nombre)

        new = []
        while len(new) < 10:
            i = random.randint(0, len(lista) - 1)

            new.append(lista.pop(i))

        str = ''

        for i in new:

            str = str + i
        nombre = str


    puntoCruzaX = random.randint(0, numBitsX)
    genesXResultado = cruzarGenes(indA[1][0],indB[1][0],puntoCruzaX,numBitsX)
    iteracionX = binarioToDecimal(genesXResultado)
    puntoCruzaY = random.randint(0, numBitsY)
    genesYResultado = cruzarGenes(indA[1][1], indB[1][1], puntoCruzaY,numBitsY)
    iteracionY = binarioToDecimal(genesYResultado)
    fenotipoX = definirFenotipo(aX, iteracionX, deltaX)
    fenotipoY = definirFenotipo(aY, iteracionY, deltaY)
    aptitud = definirAptitud(fenotipoX,fenotipoY)
    individuo = [nombre,[genesXResultado,genesYResultado],[iteracionX,iteracionY],[fenotipoX,fenotipoY],aptitud]
    return individuo

def cruzarGenes(genesA, genesB, puntoCruza, numBits):
    #breakpoint()
    if(puntoCruza == numBits - 1):
        genesB[puntoCruza] = genesA[puntoCruza]
    else:
        for i in range(puntoCruza, numBits - 1):
            genesB[puntoCruza] = genesA[puntoCruza]
    return genesB