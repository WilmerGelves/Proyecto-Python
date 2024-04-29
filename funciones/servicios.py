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
    globals.servicios.get('area').update({codServicio: nombreServicio})
    if(bool(input('Desea registrar otro servicio... S(Si) o Enter(No)'))):
        newService()
    else:
        faces.gestionS(0)
