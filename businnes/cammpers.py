import json
import os


def load_campers_json():
    try:
      with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
        lista_campers = json.load(archivo_json)
        print("La lista de campers ha sido guardada")
        return lista_campers
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

lista_campers = {}

def crear_camper():
    nombre = input("Ingrese el nombre del cliente: ")
    edad = (input("Ingrese la edad del cliente: "))
    email = input("Ingrese el correo electrónico del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")

    camper = {
        'nombre': nombre,
        'edad': edad,
        'email': email,
        'telefono': telefono,
        'direccion': direccion
    }
    lista_campers.update(camper)
    print(lista_campers)
    print("Se creó el camper con éxito")
    guardar_json()




def guardar_json():
    try:
      with open(os.path.join("data", "campers.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError: 
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
      

      

def listar_campers():
    print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)