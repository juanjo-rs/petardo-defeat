from vertice import Vertice

class VerticeGE(Vertice):
    def __init__(self, id, coordenadas, tipo_posicion, radio_vigilancia=0.0, altura=0.0):
        super().__init__(id, coordenadas)
        self.tipo_posicion = tipo_posicion  
        self.radio_vigilancia = radio_vigilancia
        self.altura = altura  
        self.tiene_torre = False
        self.soldados_presentes = []  
        self.reservas = 0