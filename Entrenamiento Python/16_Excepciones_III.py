import math


def evaluaEdad(edad):
    if edad < 0:  # Raise permite poner el tipo de error que uno quiera y personalizarlo
        raise TypeError('La edad no puede ser menor a 0')
    if edad < 20:
        return 'Eres muy joven'
    elif edad < 40:
        return 'Eres joven'
    elif edad < 65:
        return 'No eres muy joven'
    elif edad < 100:
        return 'Cuidate...'


print(evaluaEdad(1))

# CALCULO DE RAIZ


def calculaRaiz(num1):

    if num1 < 0:
        raise ValueError('El numero no puede ser negativo')
    else:
        return math.sqrt(num1)


op1 = int(input('Introduce el primer numero: '))

try:

    print(calculaRaiz(op1))

except ValueError as NumeroNegativo:

    print(NumeroNegativo)

print('Programa finalizado')
