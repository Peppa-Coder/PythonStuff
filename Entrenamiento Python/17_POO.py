# Creacion de la clase
class Auto():
    # Creacion de constructor para definir el estado inicial de cada objeto perteneciente a la clase
    def __init__(self):
        # Atributos o propiedades de clase
        # Encapsulamiento de propiedad con __ antes del nombre para que no sea modificada fuera de la clase
        self.__largoChasis = 250
        self.__anchoChasis = 150
        self.__cantRuedas = 4
        self.__enmarcha = False

    # Metodo o comportamiento de clase
    def arrancar(self, arrancamos):

        self.__enmarcha = arrancamos

        if (self.__enmarcha):

            chequeo = self.__chequeo_interno()
        # Si enmarcha=True y chequeo = True
        if (self.__enmarcha and chequeo):

            return 'El auto esta en marcha'

        elif (self.__enmarcha and chequeo == False):

            return 'Algo anda mal en el auto, no se puede arrancar'

        else:

            return 'El auto esta detenido'

    # Metodo o comportamiento de clase
    def estado(self):

        print('El auto tiene', self.__cantRuedas, 'ruedas, un ancho de', self.__anchoChasis,
            'y un largo de', self.__largoChasis)
    # Encapsulamos el metodo para que no sea accesible fuera de la clase
    def __chequeo_interno(self):

        print('Realizando chequeo interno')

        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):

            return True

        else:

            return False

# Crear objeto, Instanciando o ejemplarizando una clase
miAuto = Auto()

print(miAuto.arrancar(True))

miAuto.estado()

print('--------------- Creacion del segundo objeto --------------')
# Crear objeto, Instanciando o ejemplarizando una clase
miAuto2 = Auto()

print(miAuto2.arrancar(False))
# Intento de modificar una propiedad de la clase, pero no se vera afectada, ya que esta encapsulada
miAuto2.__cantRuedas = 2

miAuto2.estado()
