import funciones.globales as globals
import modules.infMedicos as infM
import modules.infPacientes as infP
import modules.infServicios as infS
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
        faces.gestionM(0)

def newPaciente():
    globals.borrar_pantalla()
    cedula = input('Cedula del paciente: ')
    nombrePaciente =input('Nombre: ').lower()
    apellidos = input('Apellidos: ').lower()
    celular = input('Celular: ')
    fechaNacimiento = input('Fecha de nacimiento: ').lower() #falta agregar formato de fecha para que calcule solo la edad.
    edad = input('Edad: ')
    genero = input('Genero: ').lower() 
    paciente = {
        'cedula':cedula,
        'nombrePaciente':nombrePaciente,
        'apellidos':apellidos,
        'celular':celular,
        'fechaNacimiento':fechaNacimiento,
        'edad':edad,
        'genero':genero
    }
    infP.AddData('paciente',cedula,paciente)
    globals.pacientes.get('paciente').update({cedula:paciente})
    if(bool(input('Desea registrar otro servicio... S(Si) o Enter(No)'))):
        newPaciente()
    else:
        faces.gestionP(0)

def buscarP():
    globals.borrar_pantalla()
    tipo = input('Cedula del paciente a buscar: ')
    try:
        info = globals.pacientes.get('paciente').get(tipo)
    except ValueError:
        return None
    else:
        return info
    

def modificarP():
    dataPaciente = buscarP()
    cedula,nombrePaciente,apellidos,celular,fechaNacimiento,edad,genero = dataPaciente.values()
    for key in dataPaciente.keys():
        if (key != 'cedula'):
            if(bool(input(f'Desea modificar el {key} S(si) Enter(no)'))):
                dataPaciente[key] = input(f'Ingrese el nuevo valor de {key}: ')
    globals.pacientes.get('paciente').update({cedula: dataPaciente})
    infS.UpdateFile(globals.pacientes)    
    faces.gestionP(0)