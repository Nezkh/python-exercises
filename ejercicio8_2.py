import pickle

class Vehiculo:
    
    def __init__(self, velocidad, puertas, ruedas, color):
        self.velocidad = velocidad
        self. puertas = puertas
        self.ruedas = ruedas
        self.color = color

    def __str__(self):
        return 