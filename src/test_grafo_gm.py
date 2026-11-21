from verticeGM import VerticeGM
from aristaGM import AristaGM
from grafoGM import GrafoGM

e = VerticeGM("E", (0, 0), True, False)
m = VerticeGM("M", (5, 0), False, False)
s = VerticeGM("S", (10, 0), False, True)

g = GrafoGM(dirigido=False)
g.agregarArista(AristaGM("c1", e, m, True, 5, 2))
g.agregarArista(AristaGM("c2", m, s, True, 5, 1))

print("camino E-S:", g.validar_entrada_salida(e, s))
print("entrada:", g.vertice_entrada.id, "salida:", g.vertice_salida.id)

rutas = g.dijkstra_rutas(e, s)
print("n rutas:", len(rutas))
print("ruta ids:", [v.id for v in rutas[0]])
print("obtener_arista E-M:", g.obtener_arista(e, m).id)
