def suma(num1, num2):
    return num1+num2


def resta(num1, num2):
    return num1-num2


def multiplica(num1, num2):
    return num1*num2


def divide(num1, num2):
    try:  # Excepcion
        return num1/num2
    except ZeroDivisionError:  # Excepcion
        print('No se puede dividir entre 0')
        return ('Operacion erronea')


while True:
    try:
        op1 = (int(input("Introduce el primer numero: ")))
        op2 = (int(input("Introduce el segundo numero: ")))
        break
    except:
        print('La operacion no se pudo realizar, Intente nuevamente')

operacion = input(
    "Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")
