print('Evaluacion obtener beca')

distancia = int(input('Ingrese distancia en km: '))
print('La distancia es: ' + str(distancia))

hermanos = int(input('Ingrese cantidad de hermanos: '))
print('La cantidad de hermanos es: ' + str(hermanos))

salario_familiar = int(input('Ingrese salario familiar anual bruto: '))
print('El salario familiar es: ' + str(salario_familiar))

if distancia > 40 and hermanos > 2 or salario_familiar <= 20000:
    print('Obtienes la beca')
else:
    print('No cumples los requisitos')

print('Asignaturas optativas año 2022')

print('Informática gráfica - Pruebas de software - Usabilidad y accesibilidad')
opcion=input('Ingresa la asignatura escogida: ')

asignatura=opcion.lower()

if asignatura in ('informática gráfica','pruebas de software','usabilidad y accesibilidad'):
    print('La asignatura escogida es: ' + asignatura)
else:
    print('Asignatura invalida')
