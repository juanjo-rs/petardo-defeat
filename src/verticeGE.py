from vertice import Vertice
from aristaGM import AristaGM
class VerticeGE(Vertice):
    def __init__(self, id, coordenadas, tipo_posicion, radio_vigilancia=0.0, altura=0.0):
        super().__init__(id, coordenadas)
        self.tipo_posicion = tipo_posicion  
        self.radio_vigilancia = radio_vigilancia
        self.altura = altura  
        self.tiene_torre = False
        self.soldados_presentes = []  
        self.reservas = 0
        
        
    def _calcular_distancia(self,punto_medio:tuple[float,float]):
      factorx=punto_medio[0]-self.coordenadas[0]
      factory=punto_medio[1]-self.coordenadas[1]
      distancia=(factorx**2 + factory**2)**0.5
      return distancia
  
    def alcanza_corredor(self,arista:AristaGM):
        punto_medio=arista._calcular_punto_medio()
        distancia=self._calcular_distancia(punto_medio)
        return distancia<=self.radio_vigilancia
        