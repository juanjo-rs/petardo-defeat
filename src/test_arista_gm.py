from verticeGM import VerticeGM
from aristaGM import AristaGM

v1= VerticeGM("A",(2,3),False,False)
v2=VerticeGM("B",(3,2),False,True)

a1= AristaGM("a",v1,v2,True,12,6)
print(a1._calcular_tiempo(a1.longitud,a1.velocidad))

try:
    AristaGM("b",v1,v2,True,12,0)
except ValueError as e:
    print("error esperado: ",e)