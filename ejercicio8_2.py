import pickle

# create vehicle class
class Vehiculo:
        def __init__(self, modelo, velocidad, puertas, color):
            self.modelo = modelo
            self.velocidad = velocidad
            self. puertas = puertas
            self.color = color
        def __str__(self):
            return f'el auto es un {self.modelo} tiene una velocidad maxima de {self.velocidad} es de {self.puertas} puertas y es de color {self.color}'
    
# create object and print
auto = Vehiculo("Golf",188, 5, "Gris")
print(auto)

f = open('vehiculo_obj.bin', 'wb')
pickle.dump(auto, f)
f.close()

f = open('vehiculo_obj.bin', 'rb')
auto = pickle.load(f)
f.close()