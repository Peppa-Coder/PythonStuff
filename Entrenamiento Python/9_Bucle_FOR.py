#######################################
print('Bucle for con un parametro')
for i in range(5):  # En este caso el bucle recorreria del 0 al 5
    print(f'Valor de la variable: {i}')
#######################################
print('Bucle for con doble parametro')
for i in range(5, 10):  # En este caso el bucle recorreria desde el 5 hasta el 9
    print(f'Valor de la variable: {i}')
#######################################
print('Bucle for con triple parametro')
for i in range(4, 11, 2):  # En este caso el bucle recorreria del 4 al 10 de 2 en 2
    print(f'Valor de la variable: {i}')
#######################################
for i in range(2):
    print('Hola')
#######################################
valido = False
email = input('Introduce tu email: ')

for i in range(len(email)):
    if email[i] == '@':
        valido = True
if valido:
    print('Email correcto')
else:
    print('Email incorecto')
#######################################
contador = 0
miEmail = input('Introduce tu direccion de email: ')

for i in miEmail:
    if (i == '@' or i == '.'):  # Esta condicion no es suficiente para validacion
        contador = contador + 1   # Si el correo tiene + de 1 punto, habria conflicto
if contador == 2:
    print('Email correcto')
else:
    print('Email incorrecto')
#######################################
