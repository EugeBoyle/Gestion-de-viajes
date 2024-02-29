class Ciudad:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

def contar_pasajeros_por_ciudad(lista_pasajeros, ciudad_destino):
    count = 0
    for pasajero in lista_pasajeros:
        if pasajero.destino == ciudad_destino:
            count += 1
    return count
