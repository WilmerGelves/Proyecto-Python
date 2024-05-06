from tqdm import tqdm
import time
import funciones.globales as globals

def barraProgresoP():
    elementos = range(100)
    for elemento in tqdm(elementos,desc='Verificando: '):
        time.sleep(0.01)
    
    print('Acceso permitido... ')
    globals.pausar_pantalla()

def barraProgresoD():
    elementos = range(100)
    for elemento in tqdm(elementos,desc='Verificando: '):
        time.sleep(0.01)
    
    print('Acceso denegado... ')
    globals.pausar_pantalla()
