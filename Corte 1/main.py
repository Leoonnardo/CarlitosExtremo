#enconding: utf-8
from mysqlx import View
from cruza import *
from mutacion import *
from poda import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def iniciarGenes(intervaloX1, intervaloX2, intervaloY1, intervaloY2, resolucion, pInicial, pMax, pMGenetica, pMIndividual, numGeneraciones):

    resolucion = float(resolucion)
    numGeneraciones = int(numGeneraciones)
    x1aux = float(intervaloX1)
    x2aux = float(intervaloX2)
    y1aux = float(intervaloY1)
    y2aux = float(intervaloY2)
    
    x = [x1aux, x2aux]
    y = [y1aux, y2aux]

    RX = abs(x[1] - x[0])
    RY = abs(y[1] - y[0])

    limSupX = (RX/resolucion) + 1
    limSupY = (RY/resolucion) + 1

    aX = x[0]
    aY = y[0]
    numBitsX = definirBits(limSupX)
    numBitsY = definirBits(limSupY)
    tam_pob_incial = int(pInicial)
    prob_muta_individual = float(pMIndividual)
    prob_mut_gen = float(pMGenetica)
    tam_pob_max = int(pMax)
    deltaX = RX/(2**numBitsX)
    deltaY = RY/(2**numBitsY)
    generaciones = []
    mejoresGeneracion = []
    peoresGeneracion = []
    promedioGeneracion = []

    individuos = generarPoblacionInicial(limSupX, limSupY, aX, aY, deltaX, deltaY, tam_pob_incial, numBitsX, numBitsY)

    individuos = ordenar(individuos)

    print("Generación inicial")
    print("Mejor: ", individuos[0])
    print("Peor: ", individuos[len(individuos)-1])
    print("-----------------------------------\n")

    for i in range(0, numGeneraciones):
        generaciones.append(i+1)
        print("Generación ", i+1)
        individuos = salaApareamiento(limSupX, limSupY, aX, aY, deltaX, deltaY, individuos, numBitsX, numBitsY, prob_muta_individual,prob_mut_gen)
        # individuos = salaSeguimientoMutacion(aX, aY, deltaX, deltaY, limSupX, limSupY, prob_muta_individual, prob_mut_gen, individuos)
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

        mejor = individuos[0][4]
        peor = individuos[-1][4]
        promedioAptitud = (mejor + peor)/2

        mejoresGeneracion.append(mejor)
        peoresGeneracion.append(peor)
        promedioGeneracion.append(promedioAptitud)
        print("Promedio: ", promedioAptitud)
        print("-----------------------------------\n")
    
    print("Generaciones: ", generaciones)
    print("Mejores generaciones: ", mejoresGeneracion)
    print("Peores generaciones: ", peoresGeneracion)
    print("Promedio: ", promedioGeneracion)
    
    figure = plt.figure(figsize=(15,10))
    ax = plt.subplot(1,1,1)
    ax.plot( generaciones, promedioGeneracion, label='Promedio',marker='.')  # Plot some data on the (implicit) axes.
    ax.plot( generaciones, peoresGeneracion, label='Peor',marker='.')  # etc.
    ax.plot( generaciones, mejoresGeneracion,label='Mejor',marker='.')

    blue_line = mlines.Line2D([], [], color='blue', 
                          markersize=15, label='Promedio')
    red = mlines.Line2D([], [], color='orange', 
                          markersize=15, label='Peor')
    yel = mlines.Line2D([], [], color='green', 
                          markersize=15, label='Mejor')
    ax.legend(handles=[blue_line,red,yel])

    plt.show() 
