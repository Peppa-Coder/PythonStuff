# Un decorador es una funcion que añade funcionalidad a otras funciones, que como resultado final, devuelve una función

# Este archivo.py es solo para motivos explicativos de como funciona un decorador

def funcion_decorador(funcion_parametro):
    def funcion_interior():
        # Acciones adicionales que decorarán
        print('Realizando calculo...')
        funcion_parametro()
        # Acciones adicionales que decorarán
        print('Calculo realizado ✓')
    return funcion_interior

# Elegimos las funciones que queremos decorar con @funcion_decorador

@funcion_decorador
def suma():
    print(15+20)


def resta():
    print(30-10)


suma()
resta()
