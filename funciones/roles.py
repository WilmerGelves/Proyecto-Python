import funciones.globales as globals
import json
import modules.infMedicos as infM
import modules.infPacientes as infP
import interface.faces as faces

def newSpecialist():
    title = """
    ***********************
    * REGISTRO DE MÉDICOS *
    ***********************
    """
    globals.borrar_pantalla()
    print(title)
    identMedico = input('Número de identificacion del médico: ')
    nombreMedico = input('Nombre: ').lower()
    apellidos = input('Apellidos: ').lower()
    especialidad = input('Especialidad: ') .lower()
    correo = input('Correo: ').lower()
    consultorio = input('Número de consultorio: ')
    manana = int(input('Horario de la mañana: '))
    tarde = int(input('Horario de la tarde: '))
    especialista = {
        'identificacion': identMedico,
        'nombreMedico': nombreMedico,
        'apellidos':apellidos,
        'especilidad ':especialidad,
        'correo':correo,
        'consultorio':consultorio,
        'manana':manana,
        'tarde': tarde,
    }
    infM.AddData('doctores',identMedico, especialista) #Agrega la información suministrada al json.
    globals.especialistas.get('doctores').update({identMedico: especialista})#guarda la información en el diccionario local. 
    if(bool(input('Desea registrar otro servicio... S(Si) o Enter(No)'))):
        newSpecialist()
    else:
       faces.gestioM(0)

def newPaciente():
    globals.borrar_pantalla()
    cedula = input('Cedula del paciente: ')
    nombrePaciente =input('Nombre: ').lower()
    apellidos = input('Apellidos: ').lower()
    celular = input('Celular. ')
    paciente = {
        'cedula':cedula,
        'nombrePaciente':nombrePaciente,
        'apellidos':apellidos,
        'celular':celular,
    }
    infP.AddData('paciente',cedula,paciente)
    globals.pacientes.get('paciente').update({cedula:paciente})
    if(bool(input('Desea registrar otro servicio... S(Si) o Enter(No)'))):
        newPaciente()
    else:
       faces.gestioP(0)