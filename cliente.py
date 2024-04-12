import random

Usuarios = []

def registrar_usuario():
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

# Comentario innecesario 

    user_id = random.randint(100, 999)
    Usuarios.append({
        'ID': user_id,
        'Nombre': nombre,
        'Apellido': apellido,
        'Cédula': cedula,
        'Teléfono': telefono,
        'Oficina': oficina,
        'Sede': sede
    })
    
    print(f"ID: {user_id}, te has registrado con éxito")

def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Registrar Usuario")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion in ['2', '3', '4']:
            print("Esta opción aún no está implementada.")
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main_menu()
