from main import *
import random

tablaGeneralY = []
id_Y = []
genotipoY = []
iY = []
fenotipoY = []

id = ["A","B","C","D","E","F","G","H", "I", "J"]
def creacionTabla():


    print('valores X: ',valoresX)
    print('valores Y: ',valoresY)

    print('bits valores x: ',2**num_Bits(valoresX))
    print('bits valores y: ',2**num_Bits(valoresY))


    resolucion_deltaX = RXnew / 2**num_Bits(valoresX)
    resolucion_deltaY = RYnew / 2**num_Bits(valoresY)

    print(resolucion_deltaX)
    print(resolucion_deltaY)


def creacionTablaX():
    tablaGeneralX = []
    id_X = []
    genotipoX = []
    iX = []
    fenotipoX = []
    contadorID = 0 
    listaAux = []
    contadorBits = ''

    #Nombre al individuo
    for i in range(0,tam_pob_incial):

        id_X.append(id[i])



    tablaGeneralX.append(id_X)


    #Generar Genotipo y generar i
    for x  in range(0,tam_pob_incial):
        for j in range(0, num_Bits(valoresX)):
            randomBits = random.choices((1,0))
            contadorBits = contadorBits + str(randomBits[0])
            listaAux.append(randomBits[0])

        genotipoX.append(listaAux)
        iX.append(binario_to_Decimal(int(contadorBits)))
        contadorBits = ''
        listaAux = []


    tablaGeneralX.append(genotipoX)
    tablaGeneralX.append(iX)


    for x in range(0, tam_pob_incial):
        fenotipoX.append(aX + iX[x] * resolucion)

    tablaGeneralX.append(fenotipoX)
    print(tablaGeneralX)

def creacionTablaY():
    tablaGeneralY = []
    id_Y = []
    genotipoY = []
    iY = []
    fenotipoY = [] 
    listaAux = []
    contadorBits = ''

    #Nombre al individuo
    for i in range(0,tam_pob_incial):

        id_Y.append(id[i])



    tablaGeneralY.append(id_Y)


    #Generar Genotipo y generar i
    for x  in range(0,tam_pob_incial):
        for j in range(0, num_Bits(valoresX)):
            randomBits = random.choices((1,0))
            contadorBits = contadorBits + str(randomBits[0])
            listaAux.append(randomBits[0])

        genotipoY.append(listaAux)
        iY.append(binario_to_Decimal(int(contadorBits)))
        contadorBits = ''
        listaAux = []


    tablaGeneralY.append(genotipoY)
    tablaGeneralY.append(iY)


    for x in range(0, tam_pob_incial):
        fenotipoY.append(aX + iY[x] * resolucion)

    tablaGeneralY.append(fenotipoY)
    print(tablaGeneralY)
    



creacionTablaX()
creacionTablaY()