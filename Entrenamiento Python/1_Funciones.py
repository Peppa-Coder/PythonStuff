print('==================== Funciones sin parametros ===================')

def mensaje():
    print('Aprendiendo python')
    print('Aprendiendo instrucciones basicas')
    print('Poco a poco iremos avanzando')


mensaje()


def suma():
    num1 = 5
    num2 = 7
    print(num1+num2)


suma()

print('=================== Funciones con parametros ===================')


def suma(num1, num2):
    print(num1+num2)


suma(5, 7)

suma(10, 15)

print('========== Funciones con parametros y retorno =========')


def suma(num1, num2):
    resultado = num1+num2
    return resultado

print(suma(5, 7))

almacena_resultado = suma(5, 8)
print(almacena_resultado)
