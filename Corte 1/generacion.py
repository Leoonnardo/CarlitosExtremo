from cmath import cos
import math

from numpy import euler_gamma, mat
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
    poblacion = 0

    #Nombre al individuo
    for i in range(0,tam_pob_incial):

        id_X.append(id[i])



    tablaGeneralX.append(id_X)


    #Generar Genotipo y generar i
    while poblacion < tam_pob_incial:
        for j in range(0, num_Bits(valoresX)):
            randomBits = random.choices((1,0))
            contadorBits = contadorBits + str(randomBits[0])
            listaAux.append(randomBits[0])
        
        iXTemporal = binario_to_Decimal(int(contadorBits))
        if iXTemporal <= 160:
            poblacion=poblacion+1
            genotipoX.append(listaAux)
            iX.append(binario_to_Decimal(int(contadorBits)))

        contadorBits = ''
        listaAux = []


    tablaGeneralX.append(genotipoX)
    tablaGeneralX.append(iX)


    for x in range(0, tam_pob_incial):
        fenotipoX.append(round((aX + iX[x] * resolucion), 4))

    tablaGeneralX.append(fenotipoX)
    print(tablaGeneralX)

    return tablaGeneralX[3]

def creacionTablaY():
    tablaGeneralY = []
    id_Y = []
    genotipoY = []
    iY = []
    fenotipoY = [] 
    listaAux = []
    contadorBits = ''
    poblacion = 0

    #Nombre al individuo
    for i in range(0,tam_pob_incial):

        id_Y.append(id[i])



    tablaGeneralY.append(id_Y)


    #Generar Genotipo y generar i
    while poblacion < tam_pob_incial:
        for j in range(0, num_Bits(valoresY)):
            randomBits = random.choices((1,0))
            contadorBits = contadorBits + str(randomBits[0])
            listaAux.append(randomBits[0])
        
        iYTemporal = binario_to_Decimal(int(contadorBits))
        if iYTemporal <= 160:
            poblacion=poblacion+1
            genotipoY.append(listaAux)
            iY.append(binario_to_Decimal(int(contadorBits)))

        contadorBits = ''
        listaAux = []


    tablaGeneralY.append(genotipoY)
    tablaGeneralY.append(iY)


    for x in range(0, tam_pob_incial):
        fenotipoY.append(round((aX + iY[x] * resolucion), 4))

    tablaGeneralY.append(fenotipoY)
    print(tablaGeneralY)

    return tablaGeneralY[3]
    
def unirFenotipos(fenotipoX, fenotipoY):
    fenotipos = []
    aptitudes = []

    fenotipos.append(fenotipoX)
    fenotipos.append(fenotipoY)


    for i in range(0, tam_pob_incial):
        aptitudes.append(round((cos(cos(fenotipoX[i])).real*cos(cos(fenotipoY[i])).real*(2.718281828459045**(-((fenotipoX[i])**2)-((fenotipoY[i])**2)))),4))
    fenotipos.append(aptitudes)
    
    print("Fenotipos: ", fenotipos)

unirFenotipos(creacionTablaX(), creacionTablaY())