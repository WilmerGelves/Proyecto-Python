import funciones.globales as globals
import interface.faces as faces
import funciones.todoCitas as cts
def menuCitas(op :int):
    title = """
    ********************
    * GESTION DE CITAS *
    ********************
    """
    menuC = '\t1.Asignar cita\n\t2.Cancelar cita\n\t3.Salir'
    globals.borrar_pantalla()
    if (op != 3):
        print(title)
        print(menuC)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opcion inválida')
            globals.pausar_pantalla()
            menuCitas(0)
        else:
            match (op):
                case 1:
                    cts.newCita()  
                case 2:
                    cts.deleteCita()
                case 3:
                    globals.borrar_pantalla()
                    print('Ha salido de Gestión de citas')
                    globals.pausar_pantalla()
                    faces.gestionP(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    menuCitas(0)

