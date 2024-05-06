from os import system
import sys
from enum import Enum
from datetime import date
import funciones.roles as roles
import interface.faces as faces

#Funciones globales y diccionarios locales.
def borrar_pantalla():
  if(sys.platform == "linux" or sys.platform == "darwin"):
    system("clear")
  else:
    system("cls")

def pausar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    x=input("Presione un tecla para continuar")
  else:
    system("pause")



servicios = {
  'area':{}
}

especialistas = {
  "doctores":{}
}

pacientes = {
  "paciente":{}
}

citas = {
  'cita': {}
}

historia = {
  'historico':{}
}