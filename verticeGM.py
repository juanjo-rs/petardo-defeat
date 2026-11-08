from vertice import Vertice

class VerticeGM(Vertice):
    
    def __init__(self,id,coordenadas,es_entrada: bool , es_salida: bool ):
        super().__init__(id,coordenadas)
        self.es_entrada = es_entrada  
        self.es_salida = es_salida
        
        