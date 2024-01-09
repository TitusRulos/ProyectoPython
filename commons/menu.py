from commons.utils import validar_opcion

def menu_principal():
    print(" _Menú Principal_")
    print("| 1. Campers    |")
    print("|---------------|")
    print("| 2. Trainers   |")
    print("|---------------|")
    print("| 3. Matriculas |")
    print("|---------------|")
    print("| 4. Aulas      |")
    print("|---------------|")
    print("| 5. Reportes   |")
    print("|---------------|")
    print("| 6. Salir      |")
    print("|_______________|")       
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_campers():
    print("________Campers_________")
    print("| 1. Crear campers     |")
    print("|----------------------|")
    print("| 2. listar campers    |")
    print("|----------------------|")
    print("| 3. Modificar campers |")
    print("|----------------------|")
    print("| 4. Salir             |")
    print("|______________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op
    
    
def menu_trainers():
    print("________Trainers________")
    print("| 1. Crear trainer     |")
    print("|----------------------|")
    print("| 2. Buscar trainer    |")
    print("|----------------------|")
    print("| 3. Modificar trainer |")
    print("|----------------------|")
    print("| 4. Salir             |")
    print("|______________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_matriculas():
    print("_________Matriculas_______")
    print("|1. Crear Matriculas     |")
    print("|------------------------|")
    print("|2. Buscar Matriculas    |")
    print("|------------------------|")
    print("|3. Modificar Matriuclas |")
    print("|------------------------|")
    print("|4. Salir                |")
    print("|________________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_aulas():
    print("________Aulas________")
    print("|1. Crear Aulas     |")
    print("|-------------------|")
    print("|2. Buscar Aulas    |")
    print("|-------------------|")
    print("|3. Modificar Aulas |")
    print("|-------------------|")
    print("|4. Salir           |")
    print("|___________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_reportes():
    print("________________Reportes___________________")
    print("| 1. Listar campers estado inscripto      |")
    print("|-----------------------------------------|")
    print("| 2. Listar campers aprobaron examen      |")
    print("|-----------------------------------------|")
    print("| 3. Listar trainers trabajando en campus |")
    print("|-----------------------------------------|")
    print("| 4. Salir                                |")
    print("|_________________________________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op