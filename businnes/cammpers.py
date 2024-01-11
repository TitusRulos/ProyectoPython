import json
import os

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')  

def load_campers_json():
    try:
        with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido cargada")
            return lista_campers
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return {'campers_inscritos': []}  # Retorna un diccionario con una lista vacía si hay algún error al cargar

lista_campers = load_campers_json()

def validar_edad(edad):
    try:
        edad = int(edad)
        return 12 <= edad <= 70
    except ValueError:
        return False

def validar_identificacion(identificacion):
    return len(identificacion) < 10

def crear_camper():
    nombre = input("Ingrese el nombre del cliente: ")

    # Validar que el nombre sea un string
    while not isinstance(nombre, str) or not nombre:
        
        print("Por favor, ingrese un nombre válido.")
        nombre = input("Ingrese el nombre del cliente: ")

    edad = input("Ingrese la edad del cliente: ")

    # Validar que la edad sea un número entre 12 y 70
    while not validar_edad(edad):
        limpiar_pantalla()
        print("Por favor, ingrese una edad válida (entre 12 y 70).")
        edad = input("Ingrese la edad del cliente: ")

    email = input("Ingrese el correo electrónico del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    identificacion = input("Ingrese su número de cédula: ")

    # Validar que la identificación tenga menos de 10 dígitos
    while not validar_identificacion(identificacion):
        print("Por favor, ingrese una identificación válida (menos de 10 dígitos).")
        identificacion = input("Ingrese su número de cédula: ")

    camper = {
        'nombre': nombre,
        'edad': edad,
        'email': email,
        'telefono': telefono,
        'direccion': direccion,
        'id': identificacion
    }

    if 'campers_inscritos' not in lista_campers:
        lista_campers['campers_inscritos'] = []

    lista_campers['campers_inscritos'].append(camper)

    try:
        with open(os.path.join("data", "campers.json"), 'w') as archivo_json:
            json.dump(lista_campers, archivo_json, indent=2)
            print("El camper ha sido guardado exitosamente")
    except Exception as e:
        print(f"Error al guardar el camper: {e}")

def listar_campers():
    print("Listado de campers: ")
    if 'campers_inscritos' in lista_campers:
        for camper in lista_campers['campers_inscritos']:
            print(camper)
    else:
        print("No hay campers inscritos actualmente")