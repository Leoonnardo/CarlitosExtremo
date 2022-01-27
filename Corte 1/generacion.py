#enconding: utf-8
from cmath import cos
import math
from numpy import euler_gamma, mat
import random

individuos = []

resolucion = 0.005
x = [-0.4, 0.4]
y = [-0.4, 0.4]

RX = abs(x[1] - x[0])
RY = abs(y[1] - y[0])

limSup = 160
limInf = 0

aX = x[0]
aY = y[0]
numBits = 9
tam_pob_incial = 6
prob_muta_individual = 0.1
prob_mut_gen = 0.05
tam_pob_max = 8
delta = RX/256

id = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def generarPoblacionInicial():
    for i in range(tam_pob_incial):
        individuo = generarIndividuo(i)
        #breakpoint()
        individuos.append(individuo)

def generarIndividuo(iteracion):
    nombre = id[iteracion]

    terminadoX = False
    terminadoY = False
    grupoGenetico = [[],[]]
    iteraciones = [[],[]]
    #breakpoint()
    while((not terminadoX)):
        if(not terminadoX):
            genesX = generarGen()
            iteracionX = binarioToDecimal(genesX)
            if (iteracionX <= 160 and iteracionX >= 0):
                terminadoX = True
                grupoGenetico[0] = genesX
                iteraciones[0] = iteracionX
    while(not terminadoY):
        if (not terminadoY):
            genesY = generarGen()
            iteracionY = binarioToDecimal(genesY)
            if (iteracionY <= 160 and iteracionY >= 0):
                terminadoY = True
                grupoGenetico[1] = genesY
                iteraciones[1] = iteracionY
    fenotipo = [definirFenotipoX(iteraciones[0]),definirFenotipoY(iteraciones[1])]
    aptitud = definirAptitud(fenotipo[0],fenotipo[1])
    individuo = [nombre,grupoGenetico,iteraciones,fenotipo,aptitud]
    return individuo

def definirFenotipoX(i):
    return round(aX + i * delta, 4)

def definirFenotipoY(i):
    return round(aY + i * delta, 4)

def definirAptitud(x,y):
    return round((cos(cos(x)).real * cos(cos(y)).real * (2.718281828459045 ** (-((x) ** 2) - ((y) ** 2)))), 4)

def generarGen():
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