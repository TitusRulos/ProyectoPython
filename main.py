from commons.utils import limpiar_pantalla
from commons.menus import menu_principal,menu_trainers,menu_campers,menu_matriculas,menu_aulas,menu_reportes
from businnes.cammpers import crear_camper,listar_campers,load_campers_json,lista_campers

#bootstrap


# funtions
def campers():
    load_campers_json()
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       crear_camper()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_campers()
       input("Clic cualquier teclas [continuar]: ")
def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()

    

#start
while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       campers()
   elif op==2:
       trainers()
   elif op==3:
       matriculas()
   elif op==4:
       aulas()
   elif op==5:
       reportes()
   elif op==6:
       print("Saliendo")
       break