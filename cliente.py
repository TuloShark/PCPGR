import random
from areas import areas

Usuarios = []

def registrar_usuario(mi_area):
    print("\nRegistrar Usuario")
    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha():
        print("Error: El nombre debe contener solo letras.")
        nombre = input("Ingrese su nombre: ")

    apellido = input("Ingrese su apellido: ")
    while not apellido.isalpha():
        print("Error: El apellido debe contener solo letras.")
        apellido = input("Ingrese su apellido: ")

    cedula = input("Ingrese su cédula: ")
    while not (cedula.isdigit() and len(cedula) == 9):
        print("Error: La cédula debe tener 9 caracteres numéricos.")
        cedula = input("Ingrese su cédula: ")

    telefono = input("Ingrese su teléfono: ")
    while not (telefono.isdigit() and len(telefono) == 8):
        print("Error: El teléfono debe tener 8 caracteres numéricos.")
        telefono = input("Ingrese su teléfono: ")

    oficina = input("Ingrese su oficina: ")
    while not oficina.isalpha():
        print("Error: La oficina debe contener solo letras.")
        oficina = input("Ingrese su oficina: ")

    sede = input("Ingrese su sede: ")
    while not sede.isalpha():
        print("Error: La sede debe contener solo letras.")
        sede = input("Ingrese su sede: ")

    while True:
        print("\nSeleccione un área para el usuario:")
        print("1. Área Desarrollo")
        print("2. Área Diseño")
        print("3. Área Marketing")
        print("4. Área Contabilidad")
        print("5. Salir")
        opcion_area = input("Seleccione una opción: ")

        if opcion_area in ['1', '2', '3', '4']:
            resultado = mi_area.registrarUsuario({
                'Nombre': nombre, 'Apellido': apellido, 'Cédula': cedula,
                'Teléfono': telefono, 'Oficina': oficina, 'Sede': sede
            }, int(opcion_area))

            if resultado == -1:
                print("No existe campo disponible en esta área. Elija otra área o salga.")
            else:
                user_id = random.randint(100, 999)
                print(f"ID: {user_id}, te has registrado con éxito en el área seleccionada.")
                break
        elif opcion_area == '5':
            break
        else:
            print("Opción no válida, intente de nuevo.")

def consultar_area(mi_area):
    while True:
        print("\nMenú de Áreas")
        print("1. Área Desarrollo")
        print("2. Área Diseño")
        print("3. Área Marketing")
        print("4. Área Contabilidad")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3', '4']:
            area_idx = int(opcion)
            disponibles = mi_area.consultarDisponibles(area_idx)
            print(f"Espacios disponibles en el área seleccionada: {disponibles}")
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intente de nuevo.")

def main_menu():
    mi_area = areas(maxAreaDis=5, maxAreaDevs=5, maxAreaMarke=5, maxAreaContabilidad=5)
    while True:
        print("\nMenú Principal")
        print("1. Seleccionar Área")
        print("2. Registrar Usuario")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            consultar_area(mi_area)
        elif opcion == '2':
            registrar_usuario(mi_area)
        elif opcion == '3':
            print("Hola")
        elif opcion == '4':
            print("Mundo")
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main_menu()
