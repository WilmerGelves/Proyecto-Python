import main
import funciones.globales as globals
import funciones.roles as doc
import funciones.servicios as sv
def gestionS(op : int ):
    title = """
    ***********************
    * MODULO DE SERVICIOS *
    ***********************
    """
    menuS = '\t1.Agregar Servicio.\n\t2.Modificar Servicio.\n\t3.Eliminar Servicio.\n\t4.Salir'
    globals.borrar_pantalla()
    if (op != 4):
        print(title)
        print(menuS)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opcion inválida')
            globals.pausar_pantalla()
            gestionS(0)
        else:
            match(op):
                case 1:
                    sv.newService()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    globals.borrar_pantalla()
                    print('Has salido de gestión de Servicios')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionS(0)

            



def gestioM(op :int):
    title = """
    **********************
    * GESTION DEL MEDICO *
    **********************
    """
    menuM = '\t1.Registrar médico\n\t2.Editar médico\n\t3.Buscar médico\n\t4.Eliminar médico\n\t5.Salir'
    globals.borrar_pantalla()
    if (op != 5):
        print(title)
        print(menuM)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opcion inválida')
            globals.pausar_pantalla()
            gestioM(0)
        else:
            match (op):
                case 1:
                    doc.newSpecialist()
                case 2:
                    gestioM(0)
                case 3:
                    gestioM(0)
                case 4:
                    gestioM(0)
                case 5:
                    globals.borrar_pantalla()
                    print('Ha salido de gestion al médico')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestioM(0)


def gestioP(op :int):
    title = """
    ***********************
    * GESTION Al PACIENTE *
    ***********************
    """
    menuP = '\t1.Registrar paciente\n\t2.Asignar cita\n\t3.Buscar paciente\n\t4.Editar paciente\n\t5.Salir'
    globals.borrar_pantalla()
    if (op != 5):
        print(title)
        print(menuP)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opcion inválida')
            globals.pausar_pantalla()
            gestioM(0)
        else:
            match (op):
                case 1:
                    doc.newPaciente()
                case 2:
                    gestioP(0)
                case 3:
                    gestioP(0)
                case 4:
                    gestioP(0)
                case 5:
                    globals.borrar_pantalla()
                    print('Ha salido de gestion al paciente')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestioP(0)
