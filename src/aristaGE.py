
from arista import Arista
class AristaGE(Arista):
    
    def __init__(self,vertice_inicio,vertice_fin,habilitado,id,tiempo_pie,tiempo_moto,tiempo_reconstruccion,resistencia_max,resistencia_actual,personas_reconstruccion,es_puente=False):
        super().__init__(vertice_inicio,vertice_fin,habilitado)
        self.id=id
        self.es_puente=es_puente
        self.tiempo_pie=tiempo_pie
        self.tiempo_moto=tiempo_moto
        self.tiempo_reconstruccion=tiempo_reconstruccion
        self.resistencia_max=resistencia_max
        self.resistencia_actual=resistencia_actual
        self.personas_reconstruccion=personas_reconstruccion
        self.tiempo_restante_reconstruccion=0
    def desgastar_puente(self, medio: str) -> bool:
    
         if not self.es_puente or not self.habilitado or medio != "moto":
            return False

         self.resistencia_actual -= 1

       
         if self.resistencia_actual <= 0:
            self.resistencia_actual = 0
            self.habilitado = False
            self.tiempo_restante_reconstruccion = self.tiempo_reconstruccion
            return True

         return False