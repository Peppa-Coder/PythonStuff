from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona():
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


# Creando primera vista
def saludo(request):
    # Vista de Prueba
    return HttpResponse('Hola Mundo')


# %s es un marcador de posicion donde con % se asigna lo que se quiere poner en el lugar
def fecha(request):
    # Vista que muestra la fecha y hora actual
    fecha_actual = datetime.datetime.now()
    # Esto no se debe hacer asi, se debe trabajar con plantillas para dar formato
    # Las plantillas se utilizan con la finalidad de separar el codigo html de python
    contenido = '''<html>
        <body>
        <h2>
        Fecha y hora actuales: %s
        </h2>
        </body>
        </html>''' % fecha_actual
    return HttpResponse(contenido)


def calcula_edad(request, edad, anio):
    # Vista con parametros que recibe edad y supuesto año para calcular la edad futura
    periodo = anio - 2022
    edadFutura = edad + periodo
    documento = '<html><body><h2>En el año %s tendrás %s años' % (
        anio, edadFutura)
    return HttpResponse(documento)


def prueba_plantilla(request):
    nombre = 'Juanito'
    fecha_hora = datetime.datetime.now()
    p1 = Persona('veronica', 'villagran')
    lenguajes = ["Python", "Swift", "C++", "Java", "JavaScript", "Ruby"]
    # Correcta creacion de vistas utilizando plantillas
    # La forma correcta de traer la plantilla es utilizando cargadores (loader), pero en este caso, escribiremos la ruta
    # La razon por la que se utilizan cargadores, es para no llamar a todos estos metodos cada vez que quiera ingresar un documento html externo
    # ----------------- Sin Loader!! -----------------
    '''doc_externo = open(
        'C:/Users/Chami/Documents/PythonStuff/Django/PrimerProyecto/PrimerProyecto/Templates/plantilla1.html')'''
    # Se crea un objeto de tipo template para que lea el documento
    '''plt = Template(doc_externo.read())'''
    # Se cierra documento luego de ser leido para no utilizar recursos de mas
    '''doc_externo.close()'''
    # # Rescatando valores de variables en el contexto
    '''contexto = Context({'nombre_profesor': nombre,
                        'apellido_profesor': 'Riquelme',
                        'fecha_hora': fecha_hora,
                        'nombre_persona': p1.nombre,
                        'apellido_persona': p1.apellido,
                        'lenguajes_programacion': lenguajes})'''
    # Aqui es donde se renderiza el documento
    '''documento = plt.render(contexto)'''
    # -------------------- Utilizando Loader!! -------------------
    # Desde el modulo loader importamos la funcion get_template y la utilizamos para indicar las plantillas a utilizar
    # Para que python encuentre esta plantilla, en el archivo settings.py se deben modificar los DIRS, donde se ingresa la ruta en la que estarán guardadas las plantillas
    '''doc_externo = get_template('plantilla1.html')'''
    # El metodo render del loader (que viene de una clase Template igual), es diferente al Template anterior, donde se le pasaba un contexto. Aqui solo acepta diccionarios.
    # Usando un loader nos ahorramos 2 lineas de codigo, donde podrían ser mucho mas en el caso de querer utilizar diferentes plantillas, ya que,
    # no hay que abrir, leer y cerrar cada uno de estos documentos utilizados gracias a los cargadores
    diccionario = {'nombre_profesor': nombre,
                'apellido_profesor': 'Riquelme',
                'fecha_hora': fecha_hora,
                'nombre_persona': p1.nombre,
                'apellido_persona': p1.apellido,
                'lenguajes_programacion': lenguajes}
    '''documento = doc_externo.render(diccionario)
    return HttpResponse(documento)'''
    #---------Usando funcion render del módulo shortcuts---------
    # Con esto simplificamos aun mas el codigo indicando todo en los parametros del render proveniente del shortcut
    # Tener claro que para que reconozca la plantilla, debe especificarse en el archivo settings en el apartado DIRS de los TEMPLATES
    return render(request, 'plantilla1.html', context=diccionario)

def prueba_herencia(request):
    fecha_actual = datetime.datetime.now()
    diccionario = {'fecha_hora': fecha_actual}
    return render(request, 'pruebaHerencia.html', context=diccionario)