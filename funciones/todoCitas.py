import funciones.globales as globals
import modules.infMedicos as infM
import modules.infPacientes as infP
import modules.infServicios as infS
import modules.infCitas as infC
import funciones.roles as roles
from datetime import datetime 
import interface.citas  as citas
import main
#Función que permite generar la asignación de citas. 
def newCita():
    servicios = infS.ReadFile()
    medicos = infM.ReadFile()
    pacientes = infP.ReadFile()
    globals.borrar_pantalla()
    cedula = input("Ingrese el número de cédula del paciente: ")
    try:
        if cedula in pacientes.get('paciente').get(cedula).get('cedula'):
            nombrePaciente = pacientes.get('paciente').get(cedula).get('nombrePaciente')
            apellidos = pacientes.get('paciente').get(cedula).get('apellidos')
            celular = pacientes.get('paciente').get(cedula).get('celular')
            edad = pacientes.get('paciente').get(cedula).get('edad')
            globals.borrar_pantalla()
            servicio = input('Codigo del servico: ')
            if servicio in servicios.get('area').get(servicio).get('codServicio'):
                print(medicos)
                cedulaMedico = input('Ingrese la identificacion del médico: ')
                if cedulaMedico in medicos.get('doctores').get(cedulaMedico).get('identificacion'):
                    nombreMedico = medicos.get('doctores').get(cedulaMedico).get('nombreMedico')
                    apellidoMedico = medicos.get('doctores').get(cedulaMedico).get('apellidos')
                    numConsultorio = medicos.get('doctores').get(cedulaMedico).get('consultorio')
                    try:
                        fechaHora = input('Ingrese la fecha y la hora de la cita en formato (dia-mes-año Hora:minutos): ')
                        fechaHora = datetime.strptime(fechaHora,"%d %m %Y  %H:%M")
                        fechaHora = fechaHora.strftime('%d/%m/%Y  a las  %I:%M')
                        motivoCita = input('Ingrese el motivo de la consulta: ')
                        cita = {
                        'fechaHora': fechaHora,
                        'cedPaciente': cedula,
                        'nombre':nombrePaciente,
                        'apellidos':apellidos,
                        'edad':edad,
                        'celular':celular,
                        'motivo':motivoCita,
                        'nombreMedico':nombreMedico,
                        'apellidoMedico':apellidoMedico,
                        'numConsultorio':numConsultorio
                        }
                        infC.AddData('cita',cedula,cita) 
                        globals.citas.get('cita').update({cedula:cita})
                        opciones = 'Desea crear una nueva cita: \n1.Si\n2.No'
                        print(opciones)
                        op = int(input('=>'))
                        while(op != 1 and op != 2):
                            globals.borrar_pantalla()
                            print('Opcion inválida...Intente Nuevamente')
                            print(opciones)
                            op = int(input('=>'))
                        if(op == 1):
                            newCita()
                        else:
                            citas.menuCitas(0)
                    except ValueError:   
                        print('Formato inválido')
                        globals.pausar_pantalla()
                        newCita()
    except AttributeError:
        globals.borrar_pantalla()
        print('Datos inválidos,paciente no registrado o medico no existe...\nIngrese:\n1.Registrar paciente\n2.Volver a ingresar los datos\n3.Menu principal')
        op = int(input('=>'))
        while (op !=1 and op !=2 and op !=3):
            globals.borrar_pantalla()
            print('Opcion inválida...Intente nuevamente.')
            op = int(input('=>'))
        if op == 1:
            roles.newPaciente()
        elif op == 2:
            newCita()
        else:
            main.menuPrincipal(0)

def buscarCita():
    globals.borrar_pantalla()
    cc = input('Cedula del paciente: ')
    try:
        info = globals.citas.get('cita').get(cc)
    except ValueError:
        return None
    else:
        return info
    
    


def deleteCita():
    dataDel = buscarCita()
    try:
        if 'cedPaciente' in dataDel:
            cedula = dataDel['cedPaciente']
            opciones = 'Desea Eliminar\n1.Si\n2.No'
            print(opciones)
            op = int (input('=>'))
            while (op != 1 and op != 2):
                globals.borrar_pantalla()
                print(opciones)
                op = int (input('=>'))
            if (op == 1):
                globals.citas.get('cita').pop(cedula)
                infC.UpdateFile(globals.citas)
                citas.menuCitas(0)
            else:
                citas.menuCitas(0)
        else:
            print('Especialista no encontrado.')
            citas.menuCitas(0) 
    except TypeError:
        print('No se encontró ningún registro.')
        globals.pausar_pantalla()
        citas.menuCitas(0)