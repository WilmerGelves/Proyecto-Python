import funciones.globales as globals
import modules.infServicios as infS
import interface.faces as faces

def newService():
    title = """
    *******************
    * NUEVO  SERVICIO *
    *******************
    """
    globals.borrar_pantalla()
    print(title)
    try:
        codServicio = int(input('Ingrese el código del servicio: '))
        codServicio = str(codServicio)
        nombreServicio = input('Nombre del servicio: ').lower()
        servicio = {
            'codServicio': codServicio,
            'nombreServicio': nombreServicio
        }
        infS.AddData('area',codServicio, servicio) 
        globals.servicios.get('area').update({codServicio: servicio})
        opciones = 'Desea hacer un nuevo registro: \n1.Si\n2.No'
        print(opciones)
        try:
            op = int(input('=>'))
            while(op != 1 and op != 2):
                globals.borrar_pantalla()
                print('Opcion inválida...Intente Nuevamente')
                print(opciones)
                op = int(input('=>'))
            if(op == 1):
                newService()
            else:
                faces.gestionS(0)
        except ValueError:
            print('Opción inválida.Intente nuevamente')
            newService()
    except ValueError:
        print('Estas ingresando caracteres no permitidos')
        globals.pausar_pantalla()
        newService()

def buscarS():
    globals.borrar_pantalla()
    tipo = input('Código del servicio a buscar: ')
    try:
        info = globals.servicios.get('area').get(tipo)
    except ValueError:
        return None
    else:
        return info
    

def modificarS():
    try:
        dataService = buscarS()
        codServicio,nombreServicio = dataService.values()
        for key in dataService.keys():
            if(key != 'codServicio'):
                if(bool(input(f'Desea modificar {key} S(si) Enter(no)'))):
                    dataService[key] = input(f'Ingrese el nuevo valor de {key}: ')
        globals.servicios.get('area').update({codServicio: dataService})
        infS.UpdateFile(globals.servicios)
        print(globals.servicios)
        faces.gestionS(0)
    except AttributeError:
        print('Servicio no encontrado')
        globals.pausar_pantalla()
        faces.gestionS(0)


def deleteS():
    dataDel = buscarS()
    try:
        if 'codServicio' in dataDel:
            codServicio = dataDel['codServicio']
            opciones = 'Desea Eliminar\n1.Si\n2.No'
            print(opciones)
            op = int (input('=>'))
            while (op != 1 and op != 2):
                globals.borrar_pantalla()
                print(opciones)
                op = int (input('=>'))
            if (op == 1):
                globals.servicios.get('area').pop(codServicio)
                infS.UpdateFile(globals.servicios)
                faces.gestionS(0)
            else:
                faces.gestionS(0)
        else:
            print('Especialista no encontrado.')
            faces.gestionS(0)
    except TypeError:
        print('Servicio no encontrado')
        globals.pausar_pantalla()
        faces.gestionS(0)
            