import funciones.globales as globals
import modules.infMedicos as infM
import modules.infPacientes as infP
import modules.infServicios as infS
import interface.faces as faces
import funciones.servicios as sv
from datetime import datetime

def newSpecialist():
    title = """
    ***********************
    * REGISTRO DE MÉDICOS *
    ***********************
    """
    globals.borrar_pantalla()
    print(title)
    servicio = infS.ReadFile()
    longitud = (len(servicio['area']))
    if (longitud == 0 ):
        print('No se han registrado servicios...\nPara añadir un especilista se debe haber registrado al menos un servicio.')
        globals.pausar_pantalla()
        sv.newService()
    else:
        codigo = input('Codigo del servicio que ofrecerá el médico: ')
        try:
            if codigo == servicio['area'][codigo]['codServicio']:
                identMedico = input('Número de identificacion del médico: ')
                nombreMedico = input('Nombre: ').lower()
                apellidos = input('Apellidos: ').lower()
                especialidad = servicio.get('area').get(codigo).get('nombreServicio')
                correo = input('Correo: ').lower()
                consultorio = input('Número de consultorio: ')
                #Formato de atención.
                try:
                    entradaM = input('Entrada mañana (Horas:Minutos): ')
                    salidaM = input('Salida mañana (HH:MM): ')
                    entradaT = input('Entrada tarde (HH:MM): ')
                    salidaT = input('Salida tarde (HH:MM): ')
                    entradaM = datetime.strptime(entradaM, "%H:%M")
                    salidaM = datetime.strptime(salidaM, "%H:%M")
                    entradaT = datetime.strptime(entradaT, "%H:%M")
                    salidaT = datetime.strptime(salidaT, "%H:%M")
                    atencion = f"de {entradaM.strftime('%I:%M %p')} a {salidaM.strftime('%I:%M %p')} y de {entradaT.strftime('%I:%M %p')} a {salidaT.strftime('%I:%M %p')}"
                except ValueError:
                    print('Verifique el formato de hora ingresado,\n se esta trabajando con un formato 24 horas.')
                    globals.pausar_pantalla()
                    faces.gestionM(0)
                especialista = {
                    'identificacion': identMedico,
                    'nombreMedico': nombreMedico,
                    'apellidos':apellidos,
                    'especialidad ':especialidad,
                    'correo':correo,
                    'consultorio':consultorio,
                    'horario':atencion,
                    }
                infM.AddData('doctores',identMedico, especialista) #Agrega la información  al json.
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
        except KeyError:
            print('Ingrese nuevamente el código...\nAl parecer la empresa no ofrece este servicio.')
            globals.pausar_pantalla()
            newSpecialist()
    

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
    try:
        dataEspecialista = buscarE()
        identMedico,nombreMedico,apellidos,especialidad,correo,consultorio,horario = dataEspecialista.values()
        for key in dataEspecialista.keys():
            if (key != 'identificacion'):
                if(bool(input(f'Desea modificar {key} S(si) Enter(no)'))):
                    dataEspecialista[key] = input(f'Ingrese un nuevo valor para {key}: ')
        globals.especialistas.get('doctores').update({identMedico:dataEspecialista})
        infM.UpdateFile(globals.especialistas)    
        faces.gestionM(0)
    except AttributeError:
        print('Especialista no encontrado')
        globals.pausar_pantalla()
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
    print('Igrese su fecha de nacimiento:')
    try:
        dia = int(input('Dia: '))
        while (dia < 1 or dia > 31 ):
            print('Ingrese un día valido...')
            dia = int(input('Dia: '))
            globals.borrar_pantalla()
        mes = int(input('Mes: '))
        while (mes < 1 or mes > 12):
            print('Ingrese un mes váilido...')
            mes = int(input('Mes: '))
            globals.borrar_pantalla()
        year = int(input('Año: '))
        while(year < 1890):
            print('Imposible que el paciente este vivo...')
            year = int(input('Año: '))
            globals.borrar_pantalla()
    except ValueError:
        print('Ingrese una opción válida...')
        globals.pausar_pantalla()
        newPaciente()
    fechaNacimiento = {'day':dia,
                       'month':mes,
                       'year':year 
                    }
    añoActual = datetime.now().year
    edad = añoActual - year
    genero = input('Genero(M o F): ')
    while (genero != 'f' and genero != 'm'):
        globals.borrar_pantalla()
        print('Género inválido.. M(hombre) o F(Mujer)')
        globals.pausar_pantalla()
        genero = input('Genero: ')
    paciente = {
        'cedula':cedula,
        'nombrePaciente':nombrePaciente,
        'apellidos':apellidos,
        'celular':celular,
        'fechaNacimiento':fechaNacimiento,
        'edad':edad,
        'genero':genero,
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