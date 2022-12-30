# En este archivo.py veremos como utilizar la documentacion para realizar pruebas

# El orden para realizar pruebas con testmod es documentando con triple comilla en el siguiente orden: 
# Descripcion de la funcion, triple mayor que para asignar lo que se va a testear y por ultimo el resultado esperado de la prueba. 

import doctest

def areaTriangulo(base, altura):
    
    '''
    Calcula el area de un triangulo
    >>> areaTriangulo(3,6) 
    'El area del triangulo es 9'
    '''
    
    return 'El area del triangulo es {}'.format(int(base*altura)/2)

doctest.testmod()