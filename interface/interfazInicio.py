import funciones.globales as globals
import funciones.sesiones as sesion
def menuEntrada(op :int):
    globals.borrar_pantalla()
    title = """
    **************************************
    * CENTRO MEDICO - CARLOOS ARDILA LULE *
    *         INICIO DE SESIÓN           *
    **************************************
    """
    entrada = '\t1.Administrador\n\t2.Médico\n\t3.Paciente\n\t4.Cerrar programa'
    if (op !=4 ):
        print(title)
        print(entrada)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida')
            globals.pausar_pantalla()
            menuEntrada(0)
        else:
            match (op):
                case 1:
                    sesion.administrador()
                case 2:
                    sesion.medico()
                case 3:
                    sesion.paciente()
                case 4:
                    globals.borrar_pantalla()
                    print('Fue un gusto servirle...Vuelva pronto.')
                    globals.pausar_pantalla()
                    exit()
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    menuEntrada(0)
