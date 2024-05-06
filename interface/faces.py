import main
import funciones.globales as globals
import funciones.roles as roles
import funciones.servicios as sv
import interface.citas as citas
import funciones.gestorHistorico as gh
#Este es el cuerpo del programa, son  parte de los movimientos de un sitio a otro
def gestionS(op : int ):
    title = """
    ***********************
    * MODULO DE SERVICIOS *
    ***********************
    """
    menuS = '\t1.Agregar Servicio.\n\t2.Buscar Servicio.\n\t3.Modificar Servicio.\n\t4.Eliminar Servicio.\n\t5.Salir'
    globals.borrar_pantalla()
    if (op != 5):
        print(title)
        print(menuS)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida')
            globals.pausar_pantalla()
            gestionS(0)
        else:
            match(op):
                case 1:
                    sv.newService()
                case 2:
                    resultado = sv.buscarS()
                    if resultado is None:
                        print('El servicio no fue encontrado...')
                        globals.pausar_pantalla()
                        gestionS(0)
                    else:
                        print(resultado)
                        globals.pausar_pantalla()
                        gestionS(0)
                    
                case 3:
                    sv.modificarS()
                case 4:
                    sv.deleteS()
                case 5:
                    globals.borrar_pantalla()
                    print('Has salido de gestión de Servicios')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionS(0)

            



def gestionM(op :int):
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
            gestionM(0)
        else:
            match (op):
                case 1:
                    roles.newSpecialist()
                case 2:
                    roles.modificarE()
                case 3:
                    resultado = roles.buscarE()
                    if resultado is None:
                        print('El especialista no fue encontrado...')
                        globals.pausar_pantalla()
                        gestionM(0)
                    else:
                        print(resultado)
                        globals.pausar_pantalla()
                        gestionM(0)
                case 4:
                    roles.deleteE()
                case 5:
                    globals.borrar_pantalla()
                    print('Ha salido de gestion al médico')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionM(0)


def gestionP(op :int):
    title = """
    ***********************
    * GESTION Al PACIENTE *
    ***********************
    """
    menuP = '\t1.Registrar paciente\n\t2.Gestionar cita\n\t3.Buscar paciente\n\t4.Editar paciente\n\t5.Crear historial del paciente\n\t6.Salir'
    globals.borrar_pantalla()
    if (op != 6):
        print(title)
        print(menuP)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opcion inválida')
            globals.pausar_pantalla()
            gestionP(0)
        else:
            match (op):
                case 1:
                    roles.newPaciente()
                case 2:
                    citas.menuCitas(0)
                case 3:
                    resultado = roles.buscarP()
                    if resultado is None:
                        print('El paciente no fue encontrado...')
                        globals.pausar_pantalla()
                        gestionS(0)
                    else:
                        print(resultado)
                        globals.pausar_pantalla()
                        gestionP(0)
                case 4:
                    roles.modificarP()
                case 5:
                    gh.createHistory()
                case 6:
                    globals.borrar_pantalla()
                    print('Ha salido de gestion al paciente')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionP(0)


