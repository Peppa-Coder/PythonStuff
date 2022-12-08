import pickle


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


auto1 = Vehiculos('Mazda', 'MX5')

auto2 = Vehiculos('Seat', 'Leon')

auto3 = Vehiculos('Renault', 'Megane')

autos = [auto1, auto2, auto3]

fichero = open('lista_autos', 'wb')

pickle.dump(autos, fichero)

fichero.close()

del fichero

aperturaFichero = open('lista_autos', 'rb')

cargaFichero = pickle.load(aperturaFichero)

aperturaFichero.close()

for i in cargaFichero:
    print(i.estado())
