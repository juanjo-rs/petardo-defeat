from grafo import Grafo
from vertice import Vertice


class GrafoGM(Grafo):
    def __init__(self, dirigido=False, vertice_entrada: Vertice = None, vertice_salida: Vertice = None):
        super().__init__(dirigido)
        self.vertice_entrada = vertice_entrada
        self.vertice_salida = vertice_salida
