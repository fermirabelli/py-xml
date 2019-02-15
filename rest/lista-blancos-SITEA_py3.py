import xml.etree.ElementTree as ET
import copy
import xml.dom.minidom
from random import seed
from random import random
from random import randint
import datetime
import time
import secrets
from numpy.random import choice

file = ET.parse('lista-blancos.xml')

b=file.find("blancos")
seed(1)
contadorElementos=0

idDesignacion=120
epoch=1525354920
      

orig = datetime.datetime.fromtimestamp(1525354920)
new = orig + datetime.timedelta(days=90)
#print(int(time.mktime(new.timetuple())))


naturaleza = {'CONOCIDA','PERSONAL OFENSIVO','VEHICULO A RUEDAS','VEHICULO BLINDADO','CAMINO','PUENTE','EDIFICIO','POSICION DE ARTILLERIA','DEFENSA AEREA','FORTIFICACION DE TIERRA','FORTIFICACION DE CEMENTO','INSTALACION LOGISTICA'}
efecto = {'PERTURBACION','NEUTRALIZACION','DETENCION','DESTRUCCION','CEGAMIENTO','SENALAMIENTO','ILUMINACION'}
orientacion = {'N','S','O','E'}
prioridad= {'I','II','III','IV'}
visible = ["true","false"]
vistoEnTabla = ["true","false"]

probabilidad = [0.9, 0.1]


for x in range(3):
    for c in b.findall(".//ar.mil.cideso.sitea.blanco.Blanco"):
        dupe = copy.deepcopy(c) #copiar elemento
        #tratamiento  Id de desginacion
        elems = dupe.findall('designacion')
        for elem in elems:
            elem.text = 'MH'+str(idDesignacion)
            m = file.find("mapaDestinatarios")
            #nodoDestinatario = xml.dom.minidom.parseString("<entry></entry>").documentElement
            #child1 = xml.dom.minidom.parseString("<string>MH"+str(idDesignacion)+"</string>").documentElement
            #child2 = xml.dom.minidom.parseString("<string>"+str(int(round(random()*10)))+"</string>").documentElement
            nodoDestinatario =ET.Element('entry')
            child1 = ET.SubElement(nodoDestinatario,'string')
            child1.text="MH"+str(idDesignacion)
            child2 = ET.SubElement(nodoDestinatario,'string')
            child2.text=str(randint(1,9))
            m.append(nodoDestinatario) #insert the new node
            #print(nodoDestinatario)
            idDesignacion=idDesignacion+1
        #tratamiento aleatorizacion de latitud
        elems = dupe.findall('latitud')
        for elem in elems:
            c=float(elem.text)+(random()/10)-0.05
            elem.text =str(c)
        #tratamiento aleatorizacion de longitud
        elems = dupe.findall('longitud')
        for elem in elems:
            c=float(elem.text)+(random())-0.5
            elem.text =str(c)
        #tratamiento aleatorizacion de naturaleza
        elems = dupe.findall('naturaleza')
        for elem in elems:
            secure_random = secrets.SystemRandom()
            list_of_random_items = secure_random.sample(naturaleza,1)
            elem.text =list_of_random_items[0]
        #tratamiento aleatorizacion de Fecha
        elems = dupe.findall('fechaHora')
        for elem in elems:
            #print(elem)
            elemsEpoch = elem.findall('epoch')
            for elemEpoch in elemsEpoch:
                epoch=epoch+(random()*900)
                elemEpoch.text =str(int(round(epoch)))
                #print(elemEpoch.text,int(round(int(epoch))))
        #tratamiento aleatorizacion de cota
        elems = dupe.findall('cota')
        for elem in elems:
            c=float(elem.text)+(random()*40)
            elem.text =str(round(c,1))
        #tratamiento aleatorizacion de frente
        elems = dupe.findall('frente')
        for elem in elems:
            c=float(elem.text)+(random()*20)
            elem.text =str(round(c,1))
        #tratamiento aleatorizacion de profundidad
        elems = dupe.findall('profundidad')
        for elem in elems:
            c=float(elem.text)+(random()*12)
            elem.text =str(round(c,1))
        #tratamiento aleatorizacion de efecto
        elems = dupe.findall('efecto')
        for elem in elems:
            secure_random = secrets.SystemRandom()
            list_efecto = secure_random.sample(efecto,1)
            elem.text =list_efecto[0]
        #tratamiento aleatorizacion de prioridad
        elems = dupe.findall('prioridad')
        for elem in elems:
            secure_random = secrets.SystemRandom()
            list_efecto = secure_random.sample(prioridad,1)
            elem.text =list_efecto[0]
        #tratamiento aleatorizacion de visible
        elems = dupe.findall('visible')
        for elem in elems:
            elem.text =choice(visible, p=probabilidad)
        #tratamiento aleatorizacion de vistoEnTabla
        elems = dupe.findall('vistoEnTabla')
        for elem in elems:
            elem.text =choice(vistoEnTabla, p=probabilidad)
        #tratamiento aleatorizacion de orientacion
        elems = dupe.findall('orientacion')
        for elem in elems:
            secure_random = secrets.SystemRandom()
            list_orientacion = secure_random.sample(orientacion,1)
            elem.text =list_orientacion[0]   
        b.append(dupe) #insertar elemento nuevo
        contadorElementos=contadorElementos+1

#print(ET.tostring(file))
#print(b,dupe,elem.text)

file.write("out-lista-blancos.xml")
print(contadorElementos)
#file.close()

