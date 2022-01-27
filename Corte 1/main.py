#enconding: utf-8
from generacion import *
from cruza import *
generarPoblacionInicial()
individuos = ordenar(individuos)
salaApareamiento(individuos,numBits)
