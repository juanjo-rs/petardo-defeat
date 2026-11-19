from soldado import Soldado

class Torre:
    
    def __init__(self,altura,beta):
        self.altura=altura
        self.soldados=[]
        self.beta=beta
        self.reservas=0
        
    def alcance_efectivo(self, soldado:Soldado):
        return soldado.alcance_base * (1 + self.beta * self.altura)
    
    def reservar(self, soldados_a_llegar: list[Soldado]):
        suma = len(self.soldados) + self.reservas + len(soldados_a_llegar)
        if suma <= 3:
         self.reservas += len(soldados_a_llegar)
         return True
        else:
         return False
        
    def agregar_soldado(self,soldado:Soldado):
        self.reservas-=1
        self.soldados.append(soldado)