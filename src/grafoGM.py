from grafo import Grafo
from verticeGM import VerticeGM
from collections import deque
from aristaGM import AristaGM
class GrafoGM(Grafo):
    def __init__(self, dirigido=False):
        super().__init__(dirigido)
        self.vertice_entrada = None
        self.vertice_salida =None


    def validar_entrada_salida(self,vertice_entrada:VerticeGM, vertice_salida:VerticeGM):
        if vertice_entrada not in self.vertices or vertice_salida not in self.vertices:
            return False
        if vertice_entrada==vertice_salida:
            return False
        return self._validar_entrada_salida(vertice_entrada,vertice_salida)
    
    def _validar_entrada_salida(self,vertice_entrada,vertice_salida):
        
     cola=deque()
     cola.append(vertice_entrada)
     vistos=[]
     
     while cola:
         
         vertice=cola.popleft()
         vistos.append(vertice)
         if len(self.lista_adyacencia[vertice])>0:
          for i in range(len(self.lista_adyacencia[vertice])):
             adyacente=self.lista_adyacencia[vertice][i][0]
             if adyacente==vertice_salida:
                 self.vertice_entrada=vertice_entrada
                 self.vertice_salida=vertice_salida
                 return True
             if adyacente not in cola and adyacente not in vistos:
                 cola.append(adyacente)
                 
     return False
      
         
   