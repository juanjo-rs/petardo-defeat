
from arista import Arista
class AristaGE(Arista):
    
    def __init__(self,vertice_inicio,vertice_fin,habilitado,id,tiempo_pie,tiempo_moto,tiempo_reconstruccion,resistencia_max,resistencia_actual,es_puente=False):
        super().__init__(vertice_inicio,vertice_fin,habilitado)
        self.id=id
        self.es_puente=es_puente
        self.tiempo_pie=tiempo_pie
        self.tiempo_moto=tiempo_moto
        self.tiempo_reconstruccion=tiempo_reconstruccion
        self.resistencia_max=resistencia_max
        self.resistencia_actual=resistencia_actual
        