from generacion import *

auxC = [[],[],[]]


def ordenar():
    aux = individuos

    contador = 0

    poblacion = len(individuos[2])

    while contador < poblacion:
        i = 0
        mayor = 0
        posicion = 0
        guardarX = []
        guardarY = []
        while i < len(aux[2]):
            if mayor < aux[2][i]:
                mayor = aux[2][i]
                posicion = i
            i += 1
            #breakpoint()

        for fst in range(len(aux[0])):
            guardarX.append(aux[0][fst].pop(posicion))
        for snd in range(len(aux[1])):
            guardarY.append(aux[1][snd].pop(posicion))

        auxC[0].append(guardarX)
        auxC[1].append(guardarY)
        auxC[2].append(aux[2].pop(posicion))

        contador += 1
        #breakpoint()


def reemplazar():

    aux1 = [[],[],[],[]]
    aux2 = [[],[],[],[]]
    aux3 = []

    contador = 0

    for ind in auxC:
        for i in ind:
            if contador != 2:
                for j in range(len(i)):
                    if contador == 0:
                        aux1[j].append(i[j])
                    else:
                        aux2[j].append(i[j])
            else:
                aux3.append(i)

        contador += 1
    individuos[0] = aux1
    individuos[1] = aux2
    individuos[2] = aux3
    #breakpoint()

def sacarIndividuo(posicion):
    indi = [[],[],[]]
    contador = 0
    for i in individuos:
        for j in range(len(i)):
            if contador <= 1:
                indi[contador].append(i[j][posicion])
            else:
                indi[contador].append(i[posicion])
                break
        contador += 1
    return indi

def salaApareamiento():
    fstInd = sacarIndividuo(0)
    print("Primer individuo: ", fstInd)

    #generacion mas apto
    for i in range(1,len(individuos[2])):
        cruzaInd = sacarIndividuo(i)
        resultado1 = cruza(fstInd,cruzaInd)
        resultado2 = cruza(cruzaInd,fstInd)
        print(resultado1,resultado2)


def cruza(indA,indB):
    nombre = indA[0][0]+indB[0][0]
    puntoCruzaX = random.randint(0,7)
    puntoCruzaY = random.randint(0, 7)
    #breakpoint()
    genes1stInd = [indA[0][1],indA[1][1]]
    genes2ndInd = [indB[0][1],indB[1][1]]
    genesXResultado = cruzarGenes(genes1stInd[0],genes2ndInd[0],puntoCruzaX)
    genesYResultado = cruzarGenes(genes1stInd[1],genes2ndInd[1],puntoCruzaY)
    iteracionX = binarioToDecimal(genesXResultado)
    iteracionY = binarioToDecimal(genesYResultado)
    fenotipoX = definirFenotipoX(iteracionX)
    fenotipoY = definirFenotipoY(iteracionY)
    aptitud = definirAptitud(fenotipoX,fenotipoY)
    individuo = [nombre,[genesXResultado,genesYResultado],[iteracionX,iteracionY],[fenotipoX,fenotipoY],aptitud]
    return individuo

def cruzarGenes(genesA,genesB,puntoCruza):
    #breakpoint()
    if(puntoCruza == 7):
        genesB[puntoCruza] = genesA[puntoCruza]
    else:
        for i in range(puntoCruza,7):
            genesB[puntoCruza] = genesA[puntoCruza]
    return genesB



ordenar()
reemplazar()
print("Fenotipos de X: ", individuos[0])
print("Fenotipos de Y: ", individuos[1])
print("Aptitudes: ", individuos[2])

salaApareamiento()