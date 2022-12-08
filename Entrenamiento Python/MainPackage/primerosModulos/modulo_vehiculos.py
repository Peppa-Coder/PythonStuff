class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca:', self.marca, '\nModelo:', self.modelo, '\nEn marcha:',
              self.enmarcha, '\nAcelerando:', self.acelera, '\nFrenando:', self.frena)


class Furgon(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return 'El furgon esta cargado'
        else:
            return 'El furgon no esta cargado'

# Creacion de la clase moto heredando de la clase vehiculos


class Moto(Vehiculos):
    hwheelie = ''
    def wheelie(self):
        self.hwheelie = 'Voy haciendo wheelie'

    # Se sobrescribe el metodo estado de la clase vehiculo para modificarlo y agregarle wheelie
    def estado(self):
        print('Marca:', self.marca, '\nModelo:', self.modelo, '\nEn marcha:',
              self.enmarcha, '\nAcelerando:', self.acelera, '\nFrenando:', self.frena, '\n', self.hwheelie)


class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True