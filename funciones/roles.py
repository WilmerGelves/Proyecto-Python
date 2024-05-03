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
    horarioA = input('Horario: ').lower()
    especialista = {
        'identificacion': identMedico,
        'nombreMedico': nombreMedico,
        'apellidos':apellidos,
        'especilidad ':especialidad,
        'correo':correo,
        'consultorio':consultorio,
        'horarioA':horarioA
    }
    infM.AddData('doctores',identMedico, especialista) #Agrega la información suministrada al json.
    globals.especialistas.get('doctores').update({identMedico: especialista})#guarda la información en el diccionario local. 
    opciones = 'Desea hacer un nuevo registro: \n1.Si\n2.No'
    print(opciones)
    op = int(input('=>'))
    while(op != 1 and op != 2):
        globals.borrar_pantalla()
        print('Opcion inválida...Intente Nuevamente')
        print(opciones)
        op = int(input('=>'))
    if(op == 1):
        newPaciente()
    else:
        faces.gestionM(0)

def buscarE():
    globals.borrar_pantalla()
    tipo = input('Cedula del/la especialista a buscar: ')
    try:
        info = globals.especialistas.get('doctores').get(tipo)
    except ValueError:
        return None
    else:
        return info
    

def modificarE():
    dataEspecialista = buscarE()
    identMedico,nombreMedico,apellidos,especialidad,correo,consultorio,horarioA = dataEspecialista.values()
    for key in dataEspecialista.keys():
        if (key != 'identificacion'):
            if(bool(input(f'Desea modificar {key} S(si) Enter(no)'))):
                dataEspecialista[key] = input(f'Ingrese un nuevo valor para {key}: ')
    globals.especialistas.get('doctores').update({identMedico:dataEspecialista})
    infM.UpdateFile(globals.especialistas)    
    faces.gestionM(0)

def deleteE():
    dataDel = buscarE()
    if 'identificacion' in dataDel:
        identificacion = dataDel['identificacion']
        opciones = 'Desea Eliminar\n1.Si\n2.No'
        print(opciones)
        op = int (input('=>'))
        while (op != 1 and op != 2):
            globals.borrar_pantalla()
            print(opciones)
            op = int (input('=>'))
        if (op == 1):
            globals.especialistas.get('doctores').pop(identificacion)
            infM.UpdateFile(globals.especialistas)
            faces.gestionM(0)
        else:
            faces.gestionM(0)
    else:
        print('Especialista no encontrado.')
        faces.gestionM(0)

#-----------------------------------------------------#--------------------------------------------------#----------------------------------------
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
    globals.borrar_pantalla()
    opciones = 'Desea hacer un nuevo registro: \n1.Si\n2.No'
    print(opciones)
    op = int(input('=>'))
    while(op != 1 and op != 2):
        globals.borrar_pantalla()
        print('Opcion inválida...Intente Nuevamente')
        print(opciones)
        op = int(input('=>'))
    if(op == 1):
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
            if(bool(input(f'Desea modificar {key} S(si) Enter(no)'))):
                dataPaciente[key] = input(f'Ingrese el nuevo valor de {key}: ')
    globals.pacientes.get('paciente').update({cedula:dataPaciente})
    infP.UpdateFile(globals.pacientes)    
    faces.gestionP(0)
