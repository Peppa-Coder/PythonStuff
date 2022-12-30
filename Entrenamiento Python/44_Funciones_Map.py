# Aplica una funcion a cada elemento de una lista iterable devolviendo una lista con los resultados

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self) -> str:
        return '{} que trabaja como {} tiene un salario de ${}'.format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado('Juan', 'Director', 750000),
    Empleado('Pedro', 'Subdirector', 450000),
    Empleado('Roberto', 'Jefe', 350000),
    Empleado('Daniela', 'Secretaria', 550000),
    Empleado('Florencia', 'Ejecutivo', 150000)
]


def calculo_comision(empleado):
    if empleado.salario <= 400000:
        empleado.salario *= 1.03
    return empleado


# Creamos una lista para almacenar lo que devuelva la funcion map
# map(funcion, lista a filtrar)
# Lo que hace esta linea de codigo es que a cada elemento de la listaEmpleados le aplica la funcion calculo_comision
listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)
