class Persona():

    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print('Nombre:', self.nombre, 'Edad:',
            self.edad, 'Residencia:', self.residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
    # super() sirve para llamar un metodo de la super clase
    def descripcion(self):
        super().descripcion()
        print('Salario:', self.salario, 'Antiguedad:', self.antiguedad)
        
Manuel = Persona('Manuel', 55, 'Puente Alto')

Manuel.descripcion()

# Revision de principio de sustitución (Una persona no siempre es empleado)
print(isinstance(Manuel, Empleado))
