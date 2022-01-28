import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from main import *

class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("vista_general.ui", self)
        self.botonIngresar.clicked.connect(self.ingresarDatos)

    def ingresarDatos(self):
        intervaloX1 = self.intervaloX1.text()
        intervaloX2 = self.intervaloX2.text()
        intervaloY1 = self.intervaloY1.text()
        intervaloY2 = self.intervaloY2.text()
        resolucion = self.resolucion.text()
        pInicial = self.poblacionInicial.text()
        pMax = self.poblacionMax.text()
        pMGenetica = self.pMutacionGenetica.text()
        pMIndividual = self.pMutacionIndividual.text()
        numGeneraciones = self.numGeneraciones.text()
        iniciarGenes(intervaloX1, intervaloX2, intervaloY1, intervaloY2, resolucion, pInicial, pMax, pMGenetica, pMIndividual, numGeneraciones)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())
