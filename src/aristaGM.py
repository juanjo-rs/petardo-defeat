from arista import Arista


class AristaGM(Arista):
    def __init__(self, id, vertice_inicio, vertice_fin, habilitado, longitud: float, velocidad: float):
        super().__init__(vertice_inicio, vertice_fin, habilitado)
        self.id=id
        if longitud <=0:
            raise ValueError("la longitud es una cantidad invalida")
        self.longitud = longitud
        if velocidad<=0:
            raise ValueError("la velocidad es una cantidad invalida")
        self.velocidad = velocidad
        self.tiempo_recorrido = self._calcular_tiempo(self.longitud, self.velocidad)
        self.peso_dinamico=self.tiempo_recorrido
    
    def _calcular_tiempo(self, longitud, velocidad):
        return longitud / velocidad
