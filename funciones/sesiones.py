import funciones.globales as globals
import json
import main
import funciones.barraProgreso as barra
import interface.interfazInicio as inicio
import funciones.gestorHistorico as gh

def administrador():
    with open('data/administrador.json', 'r') as rf:
        usuario = json.load(rf)
    
    cedulaAdministrador = input('Ingrese la su cédula: ')
    try:
        if (cedulaAdministrador in usuario.get('administrador').get(cedulaAdministrador).get('cedulaUser')):
            barra.barraProgresoP()
    except AttributeError:
        barra.barraProgresoD()
        inicio.menuEntrada(0)
    

def medico():
    with open('data/especialistas.json','r') as rf:
        especialista = json.load(rf)

    identidad = input('Número de identificación: ')
    try:
        if identidad in especialista.get('doctores').get(identidad).get('identificacion'):
            barra.barraProgresoP()
    except AttributeError:
        barra.barraProgresoD()
        inicio.menuEntrada(0)
        globals.borrar_pantalla()


def paciente():
    with open('data/pacientes.json', 'r') as rf:
        clientes = json.load(rf)
    cc = input('Ingrese su Cédula:')
    try:
        if cc in clientes.get('paciente').get(cc).get('cedula'):
            barra.barraProgresoP()
            gh.historialPaciente()
          
    except AttributeError:
        barra.barraProgresoD()
        inicio.menuEntrada(0)
        globals.borrar_pantalla()
