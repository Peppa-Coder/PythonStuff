import math

i = 0

while i < 3:
    i = i + 1
    print(f'Ejecucion {i}')
print('La ejecucion ha finalizado')

edad = int(input('Introduce tu edad: '))

while edad <= 0 or edad > 99:
    print('La edad ingresada no es correcta')
    edad = int(input('Introduce tu edad: '))
print('Gracias por colaborar, acceso permitido')
print(f'La edad ingresada es: {edad}')
print('El programa ha finalizado')

print('Programa de calculo de raiz cuadrada')

numero = int(input('Introduce un numero: '))
intentos = 0

while numero < 0:
    print('No se puede hallar la raiz de un numero negativo')
    if intentos == 2:
        print('Demasiados intentos. El programa ha finalizado.')
        break
    numero = int(input('Introduce un numero: '))
    if numero < 0:
        intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print(f'La raiz cuadrada de {numero} es {solucion}')
print('El programa ha finalizado')