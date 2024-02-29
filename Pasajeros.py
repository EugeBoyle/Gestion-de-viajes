class Pasajero:
    def __init__(self, nombre, dni, destino, situacion):
        self.nombre = nombre
        self.dni = dni
        self.destino = destino
        self.situacion = situacion

def calcular_costo_pasaje(self):
     costo_normal = 3500 
     if self.situacion == "estudiante":
         return costo_normal * 0.8  # Descuento del 20%
     elif self.situacion == "jubilado":
        return costo_normal * 0.5  # Descuento del 50%
     else:
         return costo_normal


def buscar_pasajero_por_dni(lista_pasajeros, dni):
     for pasajero in lista_pasajeros:
         if pasajero.dni == dni:
              return pasajero
     return None




