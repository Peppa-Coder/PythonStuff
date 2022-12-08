def sumar(num1, num2):
    return num1+num2


def restar(num1, num2):
    return num1-num2


def multiplicar(num1, num2):
    return num1*num2


def dividir(num1, num2):
    try:  # Excepcion
        return num1/num2
    except ZeroDivisionError:  # Excepcion
        print('No se puede dividir entre 0')
        return ('Operacion erronea')


def potencia(base, exponente):
    print('El resultado de la suma es: ', base**exponente)


def redondear(numero):
    print('El numero de la suma es: ', round(numero))
