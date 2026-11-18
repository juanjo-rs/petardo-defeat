from verticeGE import VerticeGE
from grafo import Grafo
from collections import deque
class GrafoGE(Grafo):
    
    def __init__(self, base: VerticeGE, cantidad_k, d0=1.0, beta=0.0):
        super().__init__(dirigido=False)
        self.base = base
        self.cantidad_k = cantidad_k
        self.d0 = d0
        self.beta = beta
        self.torres = []
        self.arbol_minimo = {}
        self.diccionario_tiempo={}

    def prim(self, vertice_inicial):
        if vertice_inicial not in self.vertices or vertice_inicial != self.base:
            return None
        else:
            arbol_minimo = {vertice_inicial: []}
            vertices_vistos = []
            vertices_vistos.append(vertice_inicial)
            aristas_vistas = []
            
            self.arbol_minimo = self._prim(vertice_inicial, arbol_minimo, vertices_vistos, aristas_vistas)
            return self.arbol_minimo

    def _prim(self, vertice_inicial, arbol_minimo, vertices_vistos, aristas_vistas):
        while len(vertices_vistos) < len(self.vertices):
            menor = float('inf')
            arista_menor = None
            for n in vertices_vistos:
                adyacentes = self.lista_adyacencia[n]
                for m in adyacentes:
                    if m[0] in vertices_vistos or not m[1].habilitado or m[1].tiempo_pie is None or m[1].tiempo_pie <= 0:
                        continue
                    else:
                        if m[1].tiempo_pie < menor:
                            proveniente = n
                            if m[1].vertice_inicio == n:
                                vertice_menor = m[1].vertice_fin
                            else:
                                vertice_menor = m[1].vertice_inicio
                            arista_menor = m[1]
                            menor = m[1].tiempo_pie
                            tupla_menor = m
                        elif m[1].tiempo_pie == menor:
                            if m[1].id < arista_menor.id:
                                proveniente = n
                                if m[1].vertice_inicio == n:
                                    vertice_menor = m[1].vertice_fin
                                else:
                                    vertice_menor = m[1].vertice_inicio
                                arista_menor = m[1]
                                menor = m[1].tiempo_pie
                                tupla_menor = m

            if arista_menor is None:
                break

            aristas_vistas.append(arista_menor)
            if proveniente in arbol_minimo:
                arbol_minimo[proveniente].append(tupla_menor)
            else:
                arbol_minimo[proveniente] = []
                arbol_minimo[proveniente].append(tupla_menor)
                
            if vertice_menor not in arbol_minimo:
                arbol_minimo[vertice_menor] = []
            arbol_minimo[vertice_menor].append((proveniente, arista_menor))
            
            vertices_vistos.append(vertice_menor)
        self.arbol_minimo=arbol_minimo
        return arbol_minimo
    
    
    def calcular_tiempos(self):
        
        cola=deque([self.base])
        marcas=[]
        diccionario_tiempos={}
        diccionario_tiempos[self.base]=0
        while cola:
            
           vertice= cola.popleft()
           marcas.append(vertice)
           if len(self.arbol_minimo[vertice])>0:
            for n in self.arbol_minimo[vertice]:
                
               adyacente=n[0]
               tiempo=diccionario_tiempos[vertice]+n[1].tiempo_pie
               if adyacente not in cola and adyacente not in marcas:
                   cola.append(adyacente)
                   diccionario_tiempos[adyacente]=tiempo
        self.diccionario_tiempo=diccionario_tiempos
        return diccionario_tiempos
                   
           
           