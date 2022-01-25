from generacion import *

individuos = unirFenotipos(creacionTablaX(), creacionTablaY())

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



ordenar()
reemplazar()
print("Fenotipos de X: ", individuos[0])
print("Fenotipos de Y: ", individuos[1])
print("Aptitudes: ", individuos[2])