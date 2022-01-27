from generacion import *

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
        #breakpoint()
        auxC.append(aux.pop(posicion))
        contador += 1

    return auxC

def salaApareamiento(lista,numBits):
    individuoApto = lista[0]
    nuevos = []
    for i in range(len(lista)):
        if(i != 0):
            nuevo = cruza(individuoApto, lista[i], numBits)
            breakpoint()
            if((nuevo[2][0] >= 0 and nuevo[2][0] <= 160) and (nuevo[2][1] >= 0 and nuevo[2][1] <= 160)):
                nuevos.append(nuevo)
            nuevo2 = cruza(lista[i], individuoApto, numBits)
            breakpoint()
            if ((nuevo2[2][0] >= 0 and nuevo2[2][0] <= 160) and (nuevo2[2][1] >= 0 and nuevo2[2][1] <= 160)):
                nuevos.append(nuevo2)
    lista.extend(nuevos)
    nuevos = ordenar(lista)
    listar(nuevos)




def cruza(indA,indB,numBits):
    nombre = indA[0]+indB[0]
    puntoCruzaX = random.randint(0, numBits)
    genesXResultado = cruzarGenes(indA[1][0],indB[1][0],puntoCruzaX,numBits)
    iteracionX = binarioToDecimal(genesXResultado)
    puntoCruzaY = random.randint(0, numBits)
    genesYResultado = cruzarGenes(indA[1][1], indB[1][1], puntoCruzaY,numBits)
    iteracionY = binarioToDecimal(genesYResultado)
    fenotipoX = definirFenotipoX(iteracionX)
    fenotipoY = definirFenotipoY(iteracionY)
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