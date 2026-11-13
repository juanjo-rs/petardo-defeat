class Convoy:
    def __init__(self, grafo_inferior, unidades_iniciales: list):
        self.grafo = grafo_inferior
        self.unidades = unidades_iniciales
        self.vertice_actual = self.grafo.vertice_entrada
        self.vertice_anterior = None
        self.ruta_actual = []
        self.arista_actual = None
        self.tiempo_restante_arista = 0.0

    def unidades_vivas(self) -> list:
        return [u for u in self.unidades if u.viva]

    def recalcular_pesos(self, torres_activas: list, alpha: float):
        for arista in self.grafo.obtener_aristas():
            tiempo_e = arista.tiempo_recorrido
            peligro_promedio = self._calcular_peligro_corredor(arista, torres_activas)
            daño_potencial = peligro_promedio * tiempo_e
            arista.peso_dinamico = tiempo_e + (alpha * daño_potencial)

    def tomar_decision_interseccion(self):
        if self.vertice_actual == self.grafo.vertice_salida:
            return

        rutas_posibles = self.grafo.dijkstra_rutas(self.vertice_actual, self.grafo.vertice_salida)
        
        if not rutas_posibles:
            return

        mejor_ruta = rutas_posibles[0]

        if len(mejor_ruta) > 1 and mejor_ruta[1] == self.vertice_anterior:
            for ruta in rutas_posibles:
                if len(ruta) > 1 and ruta[1] != self.vertice_anterior:
                    mejor_ruta = ruta
                    break

        self.ruta_actual = mejor_ruta
        self._avanzar_primer_corredor()

    def _avanzar_primer_corredor(self):
        if len(self.ruta_actual) > 1:
            siguiente_vertice = self.ruta_actual[1]
            self.arista_actual = self.grafo.obtener_arista(self.vertice_actual, siguiente_vertice)
            self.tiempo_restante_arista = self.arista_actual.tiempo_recorrido
            self.vertice_anterior = self.vertice_actual
            self.vertice_actual = None

    def _calcular_peligro_corredor(self, arista, torres_activas: list) -> float:
        peligro = 0.0
        # oigan, aquí falta la fórmula del peligro. el pdf dice que toca revisar el daño en el inicio, medio y fin del corredor. por ahora lo dejo en 0 para que el código corra y no bote error. apenas terminen las clases de torre y soldado armamos esto bien con los nombres de variables que ustedes le pongan a eso.
        return peligro