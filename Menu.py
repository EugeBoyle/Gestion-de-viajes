from Pasajeros import Pasajero, calcular_costo_pasaje, buscar_pasajero_por_dni
from Ciudades import Ciudad, contar_pasajeros_por_ciudad



def menu():
    lista_pasajeros = []  # Lista para almacenar información de pasajeros.
    ciudades = []  # Lista para almacenar información de ciudade.

    while True:
        print("\nMenú:")
        print("1. Agregar pasajero")
        print("2. Agregar ciudad")
        print("3. Visualizar información del pasajero")
        print("4. Contar pasajeros por ciudad")
        print("5. Calcular costo del viaje para un pasajero")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # Agregar pasajero
            nombre = input("Ingrese el nombre del pasajero: ")
            dni = int(input("Ingrese el DNI del pasajero: "))
            destino = input("Ingrese el destino del pasajero: ")
            situacion = input("Ingrese la situación del pasajero (normal/estudiante/jubilado): ")
            nuevo_pasajero = Pasajero(nombre, dni, destino, situacion)
            lista_pasajeros.append(nuevo_pasajero)
        elif opcion == 2:
            # Agregar ciudad
            ciudad = input("Ingrese el nombre de la ciudad: ")
            pais = input("Ingrese el nombre del país: ")
            nueva_ciudad = Ciudad(ciudad, pais)
            ciudades.append(nueva_ciudad)
        elif opcion == 3:
            # Visualizar información del pasajero
            dni = int(input("Ingrese el DNI del pasajero: "))   
            pasajero = buscar_pasajero_por_dni(lista_pasajeros, dni)
            if pasajero:
                costo_pasaje = calcular_costo_pasaje(pasajero)
                print(f"Nombre: {pasajero.nombre}, Destino: {pasajero.destino}, Situación: {pasajero.situacion}, Costo del pasaje: {costo_pasaje}")
            else:
                print("Pasajero no encontrado.")

        elif opcion == 4:
            # Contar pasajeros por ciudad
            ciudad_destino = input("Ingrese el nombre de la ciudad: ")
            cantidad_pasajeros = contar_pasajeros_por_ciudad(lista_pasajeros, ciudad_destino)
            print(f"La cantidad de pasajeros que viajan a {ciudad_destino} es: {cantidad_pasajeros}")
        elif opcion == 5:
            # Calcular costo del viaje para un pasajero
            dni = int(input("Ingrese el DNI del pasajero: "))
            pasajero = buscar_pasajero_por_dni(lista_pasajeros, dni)
            if pasajero:
                costo_pasaje = calcular_costo_pasaje(pasajero)
                print(f"Costo del viaje para {pasajero.nombre} a {pasajero.destino}: {costo_pasaje}")
            else:
                print("Pasajero no encontrado.")
        elif opcion == 6:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
if __name__ == "__main__":
   menu()