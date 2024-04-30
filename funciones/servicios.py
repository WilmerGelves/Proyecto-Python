import funciones.globales as globals
import json
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
    codServicio = input('Ingrese el código del servicio: ').lower()
    nombreServicio = input('Nombre del servicio: ').lower()
    servicio = {
        'codServicio': codServicio,
        'nombreServicio': nombreServicio
    }
    infS.AddData('area',codServicio, servicio) 
    globals.servicios.get('area').update({codServicio: servicio})
    if(bool(input('Desea registrar otro servicio... S(Si) o Enter(No)'))):
        newService()
    else:
        faces.gestionS(0)

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