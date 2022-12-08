print('Verificacion de acceso')

edad_usuario = int(input('Introduce tu edad, por favor: '))

if edad_usuario < 18:
    print('No puedes pasar')
elif edad_usuario > 100:
    print('Ingresa una edad correcta')
else:
    print('Puedes pasar')

print('Verificacion de edad')

edad = 7

if 0 < edad < 100:
    print('Edad correcta')
else:
    print('Edad incorrecta')   

print('Nota alumno')

nota_alumno= int(input('Introduce una nota, por favor: '))

if nota_alumno < 4:
    print('Insuficiente')
elif nota_alumno < 5:
    print('Pasable')
elif nota_alumno < 6:
    print('Bueno')
elif nota_alumno < 7:
    print('Muy bueno')
elif nota_alumno == 7:
	print('Excelente')
else:
    int(input('Nota inválida'))
    
print('El programa ha finalizado')

