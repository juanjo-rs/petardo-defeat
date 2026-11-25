def bellman_ford(grafo, id_origen, id_destino):
    aristas = []
    distancias = {}
    caminos = {}

    # 1. Preparar diccionarios y sacar la lista de aristas
    for vertice in grafo.vertices:
        distancias[vertice.id] = float('inf')
        caminos[vertice.id] = []

        for adyacente in vertice.adyacentes:
            vecino = adyacente[0]
            consumo = adyacente[1]
            aristas.append((vertice.id, vecino.id, consumo))

    # El nodo inicial empieza en 0
    distancias[id_origen] = 0

    cantidad_vertices = len(grafo.vertices)
    N = 0
    cambio = False

    # 2. Ciclo principal de Bellman-Ford
    while N < cantidad_vertices:
        cambio = False

        for arista in aristas:
            origen = arista[0]
            destino = arista[1]
            consumo = arista[2]

            if distancias[origen] != float('inf'):
                suma = distancias[origen] + consumo

                if suma < distancias[destino]:
                    distancias[destino] = suma

                    # Copiar las aristas que llevaba origen y agregar la nueva arista
                    ruta_actualizada = caminos[origen].copy()
                    ruta_actualizada.append((origen, destino, consumo))
                    caminos[destino] = ruta_actualizada

                    cambio = True

        if cambio == False:
            break

        N = N + 1

    # 3. Verificar si hubo ciclo negativo
    if cambio == True:
        return ([], None)

    # 4. Verificar si se pudo llegar al destino
    if distancias[id_destino] == float('inf'):
        return ([], None)

    # 5. Retornar directamente la lista de aristas del destino y su costo
    ruta = caminos[id_destino]
    consumo_total = distancias[id_destino]
    return (ruta, consumo_total)









def dijkstra(grafo, id_origen, id_destino):
    distancias = {}
    caminos = {}
    adyacencias = {}
    vistos = []

    # 1. Inicializar diccionarios
    for vertice in grafo.vertices:
        distancias[vertice.id] = float('inf')
        caminos[vertice.id] = []
        adyacencias[vertice.id] = vertice.adyacentes

    distancias[id_origen] = 0
    actual = id_origen
    cantidad_vertices = len(grafo.vertices)
    N = 0

    # 2. Ciclo principal de Dijkstra
    while N < cantidad_vertices:
        vistos.append(actual)

        # Paso A: Solo actualizar distancias de los adyacentes del nodo actual
        for adyacente in adyacencias[actual]:
            vecino = adyacente[0].id
            peso = adyacente[1]

            if vecino not in vistos:
                suma = distancias[actual] + peso

                if suma < distancias[vecino]:
                    distancias[vecino] = suma

                    ruta_actualizada = caminos[actual].copy()
                    ruta_actualizada.append((actual, vecino, peso))
                    caminos[vecino] = ruta_actualizada

        # Paso B: Buscar en TODO el diccionario el no visto con menor distancia
        menor = float('inf')
        siguiente_nodo = None

        for nodo in distancias:
            if nodo not in vistos:
                if distancias[nodo] < menor:
                    menor = distancias[nodo]
                    siguiente_nodo = nodo

        # Si ya no quedan nodos alcanzables por visitar, salimos
        if siguiente_nodo == None:
            break

        actual = siguiente_nodo
        N = N + 1

    # 3. Verificar si se pudo llegar al destino
    if distancias[id_destino] == float('inf'):
        return ([], None)

    ruta = caminos[id_destino]
    costo_total = distancias[id_destino]
    return (ruta, costo_total)



#m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
#]

def suma_diagonales(matriz):
    diagonal_principal=0
    diagonal_secundaria=0
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if i==j:
                diagonal_principal+=matriz[i][j]
            suma=i+j
            if suma==len(matriz[i])-1:
                diagonal_secundaria+=matriz[i][j]
            
    print(diagonal_principal)
    print(diagonal_secundaria)
    
#suma_diagonales(m)

m = [
    [10, 2,  5, 1],   # Suma = 18
    [4,  20, 3, 2],   # Suma = 29 (Mayor fila -> índice 1)
    [1,  1,  2, 0]    # Suma = 4
]
# Sumas columnas: col0=15, col1=23, col2=10, col3=3 (Menor col -> índice 3)
# Salida esperada: (1, 3)


def extremos_matriz(matriz):
    mayor_fila=0
    menor_colunma=float('inf')
    indice_mayor=0
    indice_menor=None
    
    for i in range(len(matriz)):
        suma_fila=0
        suma_columna=0
        for j in range(len(matriz[i])):
            suma_fila+=matriz[i][j]
            if i>=j:
             suma_columna+=matriz[j][i]
            
            
        if suma_fila>mayor_fila:
            mayor_fila=suma_fila
            indice_mayor=i
        if suma_columna<menor_colunma:
            menor_colunma=suma_columna
            
      
            
    return (indice_mayor,menor_colunma)

print(extremos_matriz(m))
    
        
        
        
            
            
            
        