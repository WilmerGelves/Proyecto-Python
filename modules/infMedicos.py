import json 
import os

DATA_MEDICOS = 'data/'  #ruta de la carpeta que almacena los datos.

def NewFile(*param):
    with open(DATA_MEDICOS,"w") as wf: #bufer de escritura
        json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
    with open(DATA_MEDICOS,"w") as fw:
        json.dump(param[0],fw,indent=4)


def AddData(*param):
    doctores = list(param)
    with open(DATA_MEDICOS,"r+") as rwf: #buefer de escritura y lectura. 
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[doctores[0]].update({doctores[1]:doctores[2]})
        else:
            data_file.update({param[0]})
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)


def ReadFile(): #Si el archivo exites, carga el contenido dentro de ellos.
    with open(DATA_MEDICOS,"r") as rf:
        return json.load(rf)
    


#Verificando si el archivo existe en nuestra carpeta data. 
def checkFile(*param):
    data = list(param)
    if(os.path.isfile(DATA_MEDICOS)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])