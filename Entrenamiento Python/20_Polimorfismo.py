class Auto():

    def desplazamiento(self):
        print('Me desplazo utilizando 4 ruedas')


class Moto():

    def desplazamiento(self):
        print('Me desplazo utilizando 2 ruedas')


class Camion():

    def desplazamiento(self):
        print('Me desplazo utilizando 6 ruedas')

# Para no llamar todos los metodos desplazamiento de cada objeto, se aplica polimorfismo mas abajo
'''miVehiculo = Moto()

miVehiculo.desplazamiento()

miVehiculo2 = Auto()

miVehiculo2.desplazamiento()

miVehiculo3 = Camion()

miVehiculo3.desplazamiento()'''


# Aplicacion de polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


# Podemos utilizar cualquier objeto para traer el metodo desplazamiento de ese objeto en especifico, en este caso Camion, Auto y Moto
miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo)
