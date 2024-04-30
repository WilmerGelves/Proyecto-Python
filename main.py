import modules.infMedicos as infM
import modules.infPacientes as infP
import modules.infServicios as infS
import interface.faces as faces
import funciones.globales as globals


def menuPrincipal(op):
    globals.borrar_pantalla()
    encabezdo = """
    **************************************
    * CENTRO MEDICO - CALROS ARDILA LULE *
    **************************************
    """
    options = '\t1.Gestion de Servicios.\n\t2.Gestionar al médico.\n\t3.Gestion al pacientes.\n\t4.Salir'
    if (op != 4):
        print(encabezdo)
        print(options)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida...')
            globals.pausar_pantalla()
            menuPrincipal(0)
        else:
            match (op):
                case 1: 
                    faces.gestionS(0)
                case 2: 
                    faces.gestionM(0)
                case 3: 
                    faces.gestionP(0)
                case 4: 
                    globals.borrar_pantalla()
                    print('Fue un gusto servirle...Vuelva pronto.')
                    globals.pausar_pantalla()
                case _:
                    globals.borrar_pantalla()
                    print('Está ingresando una opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    menuPrincipal(0)

if __name__ == '__main__':
    infM.DATA_MEDICOS= 'data/especialistas.json'
    infM.checkFile(globals.especialistas)
    infP.DATA_PACIENTES = 'data/pacientes.json'
    infP.checkFile(globals.pacientes)
    infS.MY_DATABASE = 'data/serviciosClinica.json'
    infS.checkFile(globals.servicios)
    menuPrincipal(0)

    