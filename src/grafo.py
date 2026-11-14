from arista import Arista
from vertice import Vertice


class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.vertices = []
        self.aristas = []
        self.lista_adyacencia = {}
        self.matriz_adyacencia = []
        self.indices = {}

    def agregarVertice(self, vertice: Vertice):
        if vertice.id not in self.indices:
            self.vertices.append(vertice)
            self.indices[vertice.id] = len(self.vertices) - 1
            self.lista_adyacencia[vertice] = []
            for fila in self.matriz_adyacencia:
                fila.append(0)
            self.matriz_adyacencia.append([0] * len(self.vertices))

    def agregarArista(self, arista: Arista):
        u = arista.vertice_inicio
        v = arista.vertice_fin

        if u.id not in self.indices:
            self.agregarVertice(u)
        if v.id not in self.indices: 
            self.agregarVertice(v)

        i1 = self.indices[u.id]
        i2 = self.indices[v.id]

        self.aristas.append(arista)
        self.lista_adyacencia[u].append((v, arista))
        self.matriz_adyacencia[i1][i2] = arista

        if not self.dirigido:
            self.lista_adyacencia[v].append((u, arista))
            self.matriz_adyacencia[i2][i1] = arista

    def recorridoAnchura(self, valor_inicial):
        if valor_inicial not in self.indices:
            print("El vertice no existe")
            return []
        return self._recorridoAnchura(valor_inicial)

    def _recorridoAnchura(self, valor_inicial):
        inicio = self.vertices[self.indices[valor_inicial]]
        recorrido = []
        visitados = [inicio]
        cola = []
        cola.append(inicio)
        while cola:
            actual = cola.pop(0)
            recorrido.append(actual.id)
            vecinos = sorted(
                self.lista_adyacencia[actual],
                key=lambda tupla: (getattr(tupla[1], "tiempo_recorrido", 0), tupla[0].id),
            )
            for vecino, _ponderado in vecinos:
                if vecino not in visitados:
                    cola.append(vecino)
                    visitados.append(vecino)
        return recorrido

    def recorridoProfundidad(self, valor_inicial):
        if valor_inicial not in self.indices:
            print("vertice no existente")
            return []
        recorrido = []
        visitados = []
        inicio = self.vertices[self.indices[valor_inicial]]
        self._recorridoProfundidad(inicio, recorrido, visitados)
        return recorrido

    def _recorridoProfundidad(self, vertice_i, recorrido, visitados):
        if vertice_i not in visitados:
            recorrido.append(vertice_i.id)
            vecinos = sorted(
                self.lista_adyacencia[vertice_i],
                key=lambda tupla: (getattr(tupla[1], "tiempo_recorrido", 0), tupla[0].id),
            )
            visitados.append(vertice_i)
            for vecino, _ponderado in vecinos:
                self._recorridoProfundidad(vecino, recorrido, visitados)
        return recorrido

    def encontrarMenosValor(self):
        def auxiliar(contador):
            if contador == len(self.aristas) - 1:
                return self.aristas[contador]
            resto = auxiliar(contador + 1)
            actual = self.aristas[contador]
            return actual if actual.tiempo_recorrido < resto.tiempo_recorrido else resto
        return auxiliar(0)

    def obtener_aristas(self):
            return self.aristas
        
    def obtener_arista(self,u:Vertice,v:Vertice):
       for i in range(len(self.aristas)):
           if (self.aristas[i].vertice_inicio==u and self.aristas[i].vertice_fin==v)or(self.aristas[i].vertice_inicio==v and self.aristas[i].vertice_fin==u):
               return self.aristas[i]
       return None
        