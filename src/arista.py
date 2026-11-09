from vertice import Vertice


class Arista:
    def __init__(self, vertice_inicio: Vertice, vertice_fin: Vertice, habilitado=True):
        self.vertice_inicio = vertice_inicio
        self.vertice_fin = vertice_fin
        self.habilitado = habilitado
