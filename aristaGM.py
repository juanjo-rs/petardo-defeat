from arista import Arista

class AristaGM(Arista):
    def __init__(self,vertice_inicio, vertice_fin,habilitado,longitud:float,velocidad:float):
        super().__init__(vertice_inicio,vertice_fin,habilitado)
        self.longitud=longitud
        self.velocidad=velocidad
        self.tiempo_recorrido=self._calcular_tiempo(self.longitud,self.velocidad)
        
    def _calcular_tiempo(self,longitud,velocidad):
        return longitud/velocidad