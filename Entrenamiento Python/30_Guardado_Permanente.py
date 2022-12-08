import pickle


class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print('Se ha creado una persona nueva con el nombre de:', self.nombre)

    # Convertimos en cadena de texto la información de un objeto para ver la informacion de las personas que se guardarán en el fichero externo
    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)


class ListaPersonas:

    personas = []
    # Constructor

    def __init__(self):
        # Creacion o apertura del fichero en modo agregar informacion binaria
        listaDePersonas = open('ficheroExterno', 'ab+')
        # Debemos desplazar el cursor al principio para que cuando se lea la información del fichero, lea desde el inicio.
        listaDePersonas.seek(0)

        try:
            # Cargamos la lista personas con los datos almacenados en la variable listaDePersonas (fichero), esta instruccion debeía controlarse con excepcion, ya que,  la primera vez que se abra el fichero, estará vacio.
            self.personas = pickle.load(listaDePersonas)
            print('Se cargaron {} personas del fichero externo.'.format(
                len(self.personas)))
        except:
            print('El fichero está vacio.')
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    # Se le agrega a la funcion un parametro tipo persona para que agregue esa persona a la lista
    def agregarPersonas(self, persona):
        # Agregar persona a la lista personas
        self.personas.append(persona)
        self.guardarPersonasEnFicheroExterno()

    # Función que recorra la lista personas y imprima lo que encuentre en cada vuelta de bucle
    def mostrarPersonas(self):
        for i in self.personas:
            print('A continuación se mostrarán las personas:', i)

    def guardarPersonasEnFicheroExterno(self):
        # Apertura del fichero en modo escritura binaria
        listaDePersonas = open('ficheroExterno', 'wb')
        # Volcado de datos de la lista personas al fichero abierto almacenado en la variable listaDePersonas
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print('La informacion del fichero externo es la siguiente: ')
        for i in self.personas:
            print(i)


# Instanciamos la clase ListaPersonas para crear el fichero y lo hacemos antes de crear una persona para que con ese objeto tengamos acceso a los metodos agregarPersonas() y mostrarPersonas()
miLista = ListaPersonas()
persona = Persona('Pato', 'Masculino', 72)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
