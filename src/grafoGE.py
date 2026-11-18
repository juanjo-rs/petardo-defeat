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
    
    
    def _calcular_tiempos(self):
        
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
                   
            
    def _determinar_torres(self, lista_aristaGM):
            torres_elegidas = []
            
            while len(torres_elegidas) < self.cantidad_k:
                mayor = 0
                vertice_elegido = None
                
                for v in self.vertices:
                    if v.tipo_posicion != "candidato a torre" or v not in self.diccionario_tiempo or v in torres_elegidas:
                        continue
                    
                    cp = self.longitud_total_torre(v, lista_aristaGM)
                    if cp <= 0:
                        continue
                    
                    Sp = cp / (1 + (self.diccionario_tiempo[v] / self.d0))
                    
                    if Sp > mayor:
                        mayor = Sp
                        vertice_elegido = v
                    elif Sp == mayor and vertice_elegido is not None:
                        
                        if self.diccionario_tiempo[v] < self.diccionario_tiempo[vertice_elegido]:
                            vertice_elegido = v
                        
                        elif self.diccionario_tiempo[v] == self.diccionario_tiempo[vertice_elegido]:
                            if v.id < vertice_elegido.id:
                                vertice_elegido = v
                
                
                if vertice_elegido is None:
                    break
                    
                torres_elegidas.append(vertice_elegido)
                
          
                for arista in lista_aristaGM:
                    if not arista.vigilado and vertice_elegido.alcanza_corredor(arista):
                        arista.vigilado = True
                        
            return torres_elegidas
                            
                    
                
                    
                    
    def longitud_total_torre(self,vertice:VerticeGE,lista_aristasGM):
        contador=0
        for n in lista_aristasGM:
            
            if not n.vigilado and vertice.alcanza_corredor(n):
                contador+=n.longitud
        return contador