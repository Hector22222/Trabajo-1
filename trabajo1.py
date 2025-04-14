# diccionario
base = {}

#menú interactivo

def menu():

    while True:

        print("")
        print("===== MENU PRINCIPAL =====")
        print("")
        print("1) Registrar Usuario")
        print("2) Iniciar Sesión")
        print("3) Mostrar Usuarios")
        print("4) Salir")
        print("")
        opcion = input("Selecciona una opcion (1-4): ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            inicio_usuario()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print(" Gracias por usar el programa ")
            break
        else:
            print(" Opcion invalida. Intente de nuevo.")


# registrar el usuario
def registrar_usuario():
    
    print("---------------------------")
    print("")
    print("--- Registro de Usuario ---")
    print("")
    while True:

        usuario = input("Ingrese nombre de usuario: ").strip()
        if usuario in base:

            print(" Ese usuario ya existe. Intenta con otro.")
        else:

            contraseña = input("Ingrese una contraseña: ").strip()
            nombre = input("Ingrese su nombre completo: ").strip()
            edad = input("Ingrese su edad: ").strip()
            base[usuario] = {
                "nombre": nombre,
                "contraseña": contraseña,
                "edad": edad
            }

            print(f" Usuario '{usuario}' registrado con exito")

            break


# inicio de sesion

def inicio_usuario():

    print("---------------------------")
    print("")
    print("--- Inicio de Sesion ---")
    print("")
    usuario = input("Nombre de usuario: ").strip()
    if usuario in base:

        contraseña = input("Contraseña: ").strip()
        if base[usuario]["contraseña"] == contraseña:

            print(f" Bienvenido, {base[usuario]['nombre']}!")
        else:

            print(" Contraseña incorrecta")
    else:

        print(" Usuario no encontrado")


#mostrar todos los usuarios registrados
def mostrar_usuarios():

    print("---------------------------")
    print("")
    print("--- Lista de Usuarios Registrados ---")
    print("")
    if not base:

        print("No hay usuarios registrados")
    else:

        for usuario, datos in base.items():

            print(f" Usuario: {usuario} | Nombre: {datos['nombre']} | Edad: {datos['edad']}")


# Ejecutar
menu()