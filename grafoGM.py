from grafo import Grafo
from vertice import Vertice

class GrafoGM(Grafo):
    
    def __init__(self, dirigido, vertices, lista_adyacencia, matriz_adyacencia, indices,vertice_entrada:Vertice, vertice_salida:Vertice):
        super().__init__(dirigido, vertices, lista_adyacencia, matriz_adyacencia, indices)
        self.vertice_entrada = vertice_entrada
        self.vertice_salida = vertice_salida
        
    
    