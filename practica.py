numeros = [4, 2, 7, 4, 9, 2, 4, 7, 5, 9, 2, 2]

def analizar_numeros(numeros):
   
   if numeros:
       
       return _analizar_numeros(numeros)
   else:
       return None

def _analizar_numeros(numeros):
    diccionario_frecuencia={} 
    mayor_frecuencia=0
    mas_frecuente=None
    unicos=[]
    vistos=[]
    for i in range(len(numeros)):
       numero= numeros[i]
       contador=0
       diccionario_frecuencia[numero]=0
       if numero not in vistos:
           vistos.append(numero)
       for j in range(len(numeros)):
            if numero==numeros[j]:
               contador+=1
               diccionario_frecuencia[numero]=contador
            if contador>mayor_frecuencia:
                mayor_frecuencia=contador
                mas_frecuente=numeros[j]
       if contador==1:
           unicos.append(numero)
           
    
    frecuencia_mayor=(mas_frecuente,mayor_frecuencia)
    
    diccionario_resultado={}
    clave1="frecuencia"
    clave2="mas_frecuente"
    clave3="unicos"
    clave4="sin_repetidos"
    diccionario_resultado[clave1]=diccionario_frecuencia
    diccionario_resultado[clave2]=frecuencia_mayor
    diccionario_resultado[clave3]=unicos
    diccionario_resultado[clave4]=vistos
    
    return diccionario_resultado
    
               
    
    

#print(analizar_numeros(numeros))

           
                
        
notas = [
    ("Ana", "Programacion", 4.5),
    ("Luis", "Matematicas", 3.8),
    ("Ana", "Matematicas", 4.0),
    ("Pedro", "Programacion", 3.5),
    ("Luis", "Programacion", 4.2),
    ("Pedro", "Matematicas", 4.8),
    ("Ana", "Programacion", 3.5)
]

def organizar_notas(notas):
    if notas:
        return _organizar_notas(notas)
    else:
        return None
def _organizar_notas(notas):
  diccionario={}
  
  for n in notas:
      diccionario_interno={}
      nombre= n[0]
      materia=n[1]
      nota=n[2]
      if nombre not in diccionario:
       diccionario[nombre]={}
      
      
      diccionario_interno[materia]=nota
      
      diccionario[nombre].update(diccionario_interno)
      
  return diccionario
  
#print(organizar_notas(notas))

conexiones = [
    ("Manizales", "Pereira"),
    ("Pereira", "Armenia"),
    ("Manizales", "Bogota"),
    ("Bogota", "Medellin"),
    ("Pereira", "Medellin"),
]

def construir_grafo(conexiones):
    diccionario={}
    for n in conexiones:
       conexion1= n[0]
       conexion2=n[1]
       if conexion1 not in diccionario:
        diccionario[conexion1]=[]
       if conexion2 not in diccionario:
           diccionario[conexion2]=[]
       diccionario[conexion1].append(conexion2)
       diccionario[conexion2].append(conexion1)
    return diccionario

#print(construir_grafo(conexiones))
       
    
    
red = {
    "Ana": {"Luis", "Pedro", "Sofia"},
    "Luis": {"Ana", "Carlos", "Sofia"},
    "Pedro": {"Ana", "Elena","Luis"},
    "Sofia": {"Ana", "Luis"},
    "Carlos": {"Luis"},
    "Elena": {"Pedro"},
}
def amigos_en_comun(red, persona1, persona2):
   amigos1= red[persona1]
   amigos2=red[persona2]
   comun=set()
   for n in amigos1:
       if n in amigos2:
           if n!=persona1:
               comun.add(n)
   return comun

#print(amigos_en_comun(red,"Pedro","Sofia"))

def sugerir_amigos(red,nombre):
    amigos=red[nombre]
    sugerencias=set()
    for n in amigos:
       sugerencia=red[n]
       for m in sugerencia:
           if m not in amigos and m !=nombre:
                sugerencias.add(m)
    return sugerencias
#print(sugerir_amigos(red,"Ana"))
        
def dijkstra(self,vertice_inicial,vertice_objetivo):
    distancias={}
    previos={}
    por_visitar=[]
    por_visitar.append((0,vertice_inicial))
    visitados=set()
    for n in self.vertices:
        previos[n]=None
        if n == vertice_inicial:
            distancias[n]=0
        else:
            distancias[n]=float('inf')
    return self._dijkstra(vertice_inicial,vertice_objetivo,distancias,previos,por_visitar,visitados)

def _dijkstra(self,vertice_inicial,vertice_objetivo,distancias,previos,por_visitar,visitados):
    
    while por_visitar:
        menor=float('inf')
        vertice_actual=None
        
        for n in por_visitar:
            if n[0]<menor:
                menor=n[0]
                vertice_actual=n[1]
                tupla_menor=n
        por_visitar.remove(tupla_menor)
        
        if vertice_actual not in visitados:
         visitados.add(vertice_actual)
        else:
            continue
        if vertice_actual==vertice_objetivo:
            break
        conexiones=self.lista_adyacencia[vertice_actual]
        for n in conexiones:
            if  n[1].habilitado:
                vecino=n[0]
                if vecino in visitados:
                    continue
                nuevo_costo=distancias[vertice_actual] + n[1].peso_dinamico
                if nuevo_costo<distancias[vecino]:
                    distancias[vecino]=nuevo_costo
                    previos[vecino]=vertice_actual
                    tupla=(nuevo_costo,vecino)
                    por_visitar.append(tupla)
    infinto=float('inf')
    costo_objetivo=distancias[vertice_objetivo]
    if costo_objetivo ==infinto:
        return None
    ruta=[]
    paso=vertice_objetivo
    while paso != None:
        ruta.append(paso)
        paso=previos[paso]
        
    return (distancias[vertice_objetivo],ruta.reverse())
                
                
                    
         

def prim(self,vertice_inicial):
        if vertice_inicial not in self.vertices or vertice_inicial!=self.base:
            return None
        else:
            arbol_minimo={}
            vertices_vistos=[]
            vertices_vistos.append(vertice_inicial)
            aristas_vistas=[]
            
            return self._prim(vertice_inicial,arbol_minimo,vertices_vistos,aristas_vistas)

def _prim(self,vertice_inicial,arbol_minimo,vertices_vistos,aristas_vistas):

    while len(vertices_vistos) < len(self.vertices):
        menor=float('inf')
        for n in vertices_vistos:
            adyacentes=self.lista_adyacencia[n]
            for m in adyacentes:
                if m[0] in vertices_vistos or m[1] in aristas_vistas:
                    continue
                else:
                    if m[1].tiempo_pie< menor:
                        proveniente=n
                        if m[1].vertice_inicio==n:
                            vertice_menor=m[1].vertice_fin
                        else:
                            vertice_menor=m[1].vertice_inicio
                        arista_menor=adyacentes[m][1]
                        menor=m[1].tiempo_pie
                        tupla_menor=m
        
        
        aristas_vistas.append(arista_menor)
        if proveniente in arbol_minimo:
         arbol_minimo[proveniente].append(tupla_menor)
        else:
            arbol_minimo[proveniente]=[]
            arbol_minimo[proveniente].append(tupla_menor)
        arbol_minimo[vertice_menor].append((proveniente, arista_menor))#para bidireccional
        vertices_vistos.append(vertice_menor)
    return arbol_minimo


conexiones1 = [("B", 10), ("C", 4), ("D", 15)]

def recorrer(conexiones1):
    for conexion in conexiones1:
        if conexion[1]<12:
            print (conexion[0])

recorrer(conexiones1)
        
        


        
                        
                        
       
                        
def dijkstra(self, vertice_inicial, vertice_objetivo):
    if vertice_inicial not in self.vertices or vertice_objetivo not in self.vertices:
        return None
    distancias = {}
    previos = {}
    por_visitar = []
    por_visitar.append((0, vertice_inicial))
    visitados = set()
    for n in self.vertices:
        previos[n] = None
        if n == vertice_inicial:
            distancias[n] = 0
        else:
            distancias[n] = float('inf')
    return self._dijkstra(vertice_inicial, vertice_objetivo, distancias, previos, por_visitar, visitados)

def _dijkstra(self, vertice_inicial, vertice_objetivo, distancias, previos, por_visitar, visitados):
    while por_visitar:
        menor = float('inf')
        vertice_actual = None
        
        for n in por_visitar:
            if n[0] < menor:
                menor = n[0]
                vertice_actual = n[1]
                tupla_menor = n
        por_visitar.remove(tupla_menor)
        
        if vertice_actual not in visitados:
            visitados.add(vertice_actual)
        else:
            continue
        if vertice_actual == vertice_objetivo:
            break
        conexiones = self.lista_adyacencia[vertice_actual]
        for n in conexiones:
            if n[1].habilitado:
                vecino = n[0]
                if vecino in visitados:
                    continue
                nuevo_costo = distancias[vertice_actual] + n[1].peso_dinamico
                if nuevo_costo < distancias[vecino]:
                    distancias[vecino] = nuevo_costo
                    previos[vecino] = vertice_actual
                    tupla = (nuevo_costo, vecino)
                    por_visitar.append(tupla)

    costo_objetivo = distancias[vertice_objetivo]
    if costo_objetivo == float('inf'):
        return None
        
    ruta = []
    paso = vertice_objetivo
    while paso is not None:
        ruta.append(paso)
        paso = previos[paso]
    
    ruta.reverse()
    return (costo_objetivo, ruta)