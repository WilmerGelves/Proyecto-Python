import funciones.globales as globals
import modules.infMedicos as infM
import modules.infPacientes as infP
import modules.infCitas as infC 
from datetime import datetime
import modules.gestionHistoricos as gestor
import main
import interface.faces as faces

#Funcion para que el médico cree la historia clinica según los motivos de la consulta.
def createHistory():
    medico = infM.ReadFile()
    usuario = infP.ReadFile()
    informacion = infC.ReadFile()
    cedulaPaciente = input('Cédula del paciente: ')
    try:
        if cedulaPaciente in usuario.get('paciente').get(cedulaPaciente).get('cedula'):
            nombrePaciente = usuario.get('paciente').get(cedulaPaciente).get('nombrePaciente')
            apellidoPaciente = usuario.get('paciente').get(cedulaPaciente).get('apellidos')
            edad = usuario.get('paciente').get(cedulaPaciente).get('edad')
            genero = usuario.get('paciente').get(cedulaPaciente).get('genero')
            identEspecialista = input('Indentificación del especialista: ')
            if identEspecialista in medico.get('doctores').get(identEspecialista).get('identificacion'):
                nombreEspecialista = medico.get('doctores').get(identEspecialista).get('nombreMedico')
                apellidoEspecialista = medico.get('doctores').get(identEspecialista).get('apellidos')
                especialidad = medico.get('doctores').get(identEspecialista).get('especialidad')
                print('Motivo de la consulta:',informacion.get('cita').get(cedulaPaciente).get('motivo'))
                motivoCita = informacion.get('cita').get(cedulaPaciente).get('motivo')
                globals.pausar_pantalla()
                diagnostico = input( 'Ingrese su diagnóstico: ')
                tratamiento = input( 'Tratamiento: ')
                ahora = datetime.now()
                fecha =  ahora.strftime("%d/%m/%Y %I:%M %p")
                Historia = {
                    'cedulaPaciente':cedulaPaciente,
                    'nombrePaciente':nombrePaciente,
                    'apellidosPaciente':apellidoPaciente,
                    'edad':edad,
                    'genero':genero,
                    'fecha':fecha,
                    'motivoCita':motivoCita,
                    'nombreEspecialista':nombreEspecialista,
                    'apellidosEspecialista':apellidoEspecialista,
                    'especialidad':especialidad,
                    'diagnostico':diagnostico,
                    'tratamiento':tratamiento
                }
                gestor.AddData('historico',cedulaPaciente,Historia) 
                globals.historia.get('historico').update({cedulaPaciente:Historia})
                opciones = 'Desea realizar una nueva historia: \n1.Si\n2.Gestion al paciente\n3.Terminar turno'
                print(opciones)
                op = int(input('=>'))
                while(op != 1 and op != 2 and op != 3):
                    globals.borrar_pantalla()
                    print('Opcion inválida...Intente Nuevamente')
                    print(opciones)
                    op = int(input('=>'))
                if(op == 1):
                    createHistory()
                elif(op == 2):
                    faces.gestionP(0)
                else:
                    main.menuPrincipal(4)
    except AttributeError:
        globals.borrar_pantalla()
        print('Datos inválidos,paciente no registrado o medico no existe...')
        globals.pausar_pantalla()
        createHistory()
        


#Funcion para qu el paciente pueda visualizar sus históricos.
def historialPaciente():
    globals.borrar_pantalla()
    cc = input('Ingrese su cédula nuevamente:  ')
    try:
        info = globals.historia.get('historico').get(cc)
        print(info)
        globals.pausar_pantalla()
    except ValueError:
        mensaje = 'Verifique los datos ingresados...\n1.Intentar nuevamente\n2.Salir del programa'
        print(mensaje)
        op = int(input('=>'))
        while (op != 1 and op != 2):
            globals.borrar_pantalla()
            print(mensaje)
            op = int(input('=>'))
        if op == 1 :
            historialPaciente()
        else :
            exit()

#Funcion para que el usuario visualice el historico de un paciente. 
def historialMedico():
    globals.borrar_pantalla()
    cc = input('Cedula del paciente: ')
    try:
        info = globals.historia.get('historico').get(cc)
        print(info)
        globals.pausar_pantalla()
    except ValueError:
        mensaje = 'Verifique los datos ingresados...\n1.Intentar nuevamente\n2.Gestion del paciente\n3.Salir'
        print(mensaje)
        op = int(input('=>'))
        while (op != 1 and op != 2 and op != 3):
            globals.borrar_pantalla()
            print(mensaje)
            op = int(input('=>'))
        if op == 1 :
            historialPaciente()
        elif op == 2 :
            faces.gestionP(0)
        else :
            exit()
            
