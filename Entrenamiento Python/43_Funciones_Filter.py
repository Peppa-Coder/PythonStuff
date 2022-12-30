# Este tipo de funciones filter verifican que los elemntos de una secuencia cumplan una funcion,
# devolviendo un iterador de elementos que cumplen dicha funcion

def numero_par(num):
    if num % 2 == 0:
        return True


numeros = [17, 24, 7, 39, 8, 51, 92]

# filter devuelve un objeto, por lo que previo a esta funcion le decimos que lo imprima como una lista en este caso.
# Generalmente filter se utiliza para filtrar objetos
# filter (condicion, lo que se va a filtrar)
print(list(filter(numero_par, numeros)))

# lambda en este caso remplaza la funcion numero_par y simplifica la sintaxis dejando todo en una linea de codigo
print(list(filter(lambda numero_par_remplazo: numero_par_remplazo % 2 == 0, numeros)))


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

salarios_altos = filter(
    lambda empleadito:empleadito.salario > 500000, listaEmpleados)

for employee in salarios_altos:
    print(employee)
