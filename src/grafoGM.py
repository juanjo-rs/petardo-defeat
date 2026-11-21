from grafo import Grafo
from verticeGM import VerticeGM
from collections import deque


class GrafoGM(Grafo):
    def __init__(self, dirigido=False):
        super().__init__(dirigido)
        self.vertice_entrada = None
        self.vertice_salida = None

    def validar_entrada_salida(self, vertice_entrada: VerticeGM, vertice_salida: VerticeGM):
        if vertice_entrada not in self.vertices or vertice_salida not in self.vertices:
            return False
        if vertice_entrada == vertice_salida:
            return False
        return self._validar_entrada_salida(vertice_entrada, vertice_salida)

    def _validar_entrada_salida(self, vertice_entrada, vertice_salida):
        cola = deque()
        cola.append(vertice_entrada)
        vistos = []

        while cola:
            vertice = cola.popleft()
            vistos.append(vertice)
            if len(self.lista_adyacencia[vertice]) > 0:
                for i in range(len(self.lista_adyacencia[vertice])):
                    adyacente = self.lista_adyacencia[vertice][i][0]
                    arista = self.lista_adyacencia[vertice][i][1]
                    if not arista.habilitado:
                        continue
                    if adyacente == vertice_salida:
                        self.vertice_entrada = vertice_entrada
                        self.vertice_salida = vertice_salida
                        return True
                    if adyacente not in cola and adyacente not in vistos:
                        cola.append(adyacente)

        return False

    def _peso_arista(self, arista):
        if hasattr(arista, "peso_dinamico") and arista.peso_dinamico is not None:
            return arista.peso_dinamico
        return arista.tiempo_recorrido

    def dijkstra_rutas(self, origen, destino):
        if origen not in self.vertices or destino not in self.vertices:
            return []

        distancias = {}
        padres = {}
        no_vistos = []
        for v in self.vertices:
            distancias[v] = float("inf")
            padres[v] = None
            no_vistos.append(v)
        distancias[origen] = 0

        while len(no_vistos) > 0:
            menor = float("inf")
            actual = None
            for v in no_vistos:
                if distancias[v] < menor:
                    menor = distancias[v]
                    actual = v

            if actual is None or distancias[actual] == float("inf"):
                break

            no_vistos.remove(actual)
            if actual == destino:
                break

            adyacentes = self.lista_adyacencia[actual]
            for i in range(len(adyacentes)):
                vecino = adyacentes[i][0]
                arista = adyacentes[i][1]
                if not arista.habilitado:
                    continue
                if vecino not in no_vistos:
                    continue
                nueva = distancias[actual] + self._peso_arista(arista)
                if nueva < distancias[vecino]:
                    distancias[vecino] = nueva
                    padres[vecino] = actual

        if distancias[destino] == float("inf"):
            return []

        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = padres[actual]
        ruta.reverse()
        return [ruta]
