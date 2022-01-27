#enconding: utf-8
from math import cos, e
import math
from numpy import euler_gamma, mat
import random

def definirBits(numero):
    #breakpoint()
    modulos = []
    while numero != 0:
        modulo = numero % 2
        cociente = numero // 2
        modulos.append(modulo)
        numero = cociente
    return len(modulos)


id = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def generarPoblacionInicial(limSupX, limSupY, aX, aY, deltaX, deltaY, poblacionInicial, numBitsX, numBitsY):
    individuos = []

    for i in range(poblacionInicial):
        individuo = generarIndividuo(limSupX, limSupY, aX, aY, deltaX, deltaY, i, numBitsX, numBitsY)
        #breakpoint()
        individuos.append(individuo)

    return individuos

def generarIndividuo(limSupX, limSupY, aX, aY, deltaX, deltaY, iteracion, numBitsX, numBitsY):
    nombre = id[iteracion]

    terminadoX = False
    terminadoY = False
    grupoGenetico = [[],[]]
    iteraciones = [[],[]]
    #breakpoint()
    while((not terminadoX)):
        if(not terminadoX):
            genesX = generarGen(numBitsX)
            iteracionX = binarioToDecimal(genesX)
            if (iteracionX <= limSupX and iteracionX >= 0):
                terminadoX = True
                grupoGenetico[0] = genesX
                iteraciones[0] = iteracionX
    while(not terminadoY):
        if (not terminadoY):
            genesY = generarGen(numBitsY)
            iteracionY = binarioToDecimal(genesY)
            if (iteracionY <= limSupY and iteracionY >= 0):
                terminadoY = True
                grupoGenetico[1] = genesY
                iteraciones[1] = iteracionY
    fenotipo = [definirFenotipo(aX,iteraciones[0],deltaX),definirFenotipo(aY,iteraciones[1],deltaY)]
    aptitud = definirAptitud(fenotipo[0],fenotipo[1])
    individuo = [nombre,grupoGenetico,iteraciones,fenotipo,aptitud]
    return individuo

def definirFenotipo(a,i,delta):
    return a + i * delta

def definirAptitud(x,y):
    breakpoint()
    return cos(x) * cos(y) * (e ** ( ((x*-1)**2) * ((y*-1)**2) ))

def generarGen(numBits):
    #breakpoint()
    grupoGen = []
    for i in range(numBits):
        gen = random.randint(0,1)
        grupoGen.append(gen)
    return grupoGen

def binarioToDecimal(binario):
    #breakpoint()
    contador = 0
    potencia = len(binario) - 1
    for i in range(len(binario)):
        contador = contador + ((2**potencia)*binario[i])
        potencia -= 1
    return contador

def listar(lista):
    for i in lista:
        print("Individuo: ", i[0])
        print("Genes: ", i[1])
        print("Iteraciones: ", i[2])
        print("Fenotipos: ", i[3])
        print("Aptitudes: ", i[4])
        print("------------------------------------------")