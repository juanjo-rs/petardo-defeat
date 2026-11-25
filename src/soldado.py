

class Soldado:
    
    def __init__(self,unidad):
        self.unidad=unidad
        self.costo=self.determinar_costo()
        self.daño=self.determinar_daño()
        self.alcance_base=self.determinar_alcance_base()
        self.frecuencia=self.determinar_frecuencia()
        self.en_transito = False 
        
    def determinar_costo(self):
        if self.unidad=="infanteria":
            return 100
        elif self.unidad=="francotirador":
            return 300
        else:
            return 500
        
    def determinar_daño(self):
        if self.unidad=="infanteria":
            return 10
        elif self.unidad=="francotirador":
            return 50
        else:
            return 100
    def determinar_alcance_base(self):
        if self.unidad=="infanteria":
            return 5
        elif self.unidad=="francotirador":
            return 20
        else:
            return 15
        
    def determinar_frecuencia(self):
        if self.unidad=="infanteria":
            return 1
        elif self.unidad=="francotirador":
            return 0.5
        else:
            return 0.2
        