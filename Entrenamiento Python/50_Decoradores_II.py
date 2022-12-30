# Creando decoradores con parametros

# Utilizamos la nomenclatura * para que reciba la cantidad que sea de parametros,
# esto se debe hacer tanto en la funcion parametro del decorador, como en la funcion interior de la funcion decorador
# args es solo por convencion, puede ser un nombre cualquiera
# Tambien se le puede pasar a la funcion parametros con keywords con **
# kwargs tambien es por convencion y viene de keyword arguments
def funcion_decorador(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print('Realizando calculo...')
        funcion_parametro(*args, **kwargs)
        print('Calculo realizado ✓')
    return funcion_interior

# Decorando funcion
@funcion_decorador
def suma(num1, num2):
    print(num1 + num2)

@funcion_decorador
def resta(num1, num2):
    print(num1 - num2)

@funcion_decorador
def potencia(base, exponente):
    print(pow(base, exponente))


suma(10, 5)
resta(20, 5)
# Al llamar esta funcion, en los parametros le ingresamos argumentos de tipo keywords, donde las claves serian base y exponente, y los valores serian 5 y 3
# Para hacer esto se utiliza la nomenclatura ** en el decorador
potencia(base=5, exponente=3)
