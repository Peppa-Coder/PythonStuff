import re

lista1 = [
    'MA1',
    'MA2',
    'HE1',
    'HE2',
    'MA3',
    'CA1',
    'MA4',
    'MAA',
    'MAB',
    'MAC',
    'MA.1',
    'MA:2',
    'HE.1',
]
# Trabajando con rangos [x-x]
for elemento in lista1:
    if re.findall('MA[0-3]', elemento):
        print(elemento)

print('-------------------------------------')

for elemento in lista1:
    # Cuando se trabaja con rangos, si utilizamos el simbolo ^, podemos ver los que son diferentes del rango escrito
    if re.findall('MA[^0-2]', elemento):
        print(elemento)

print('-------------------------------------')

for elemento in lista1:
    # Busca todos los elementos de la lista que contengan alguna letra de la A a la C
    if re.findall('[A-C]', elemento):
        print(elemento)

print('-------------------------------------')

for elemento in lista1:
    # Busca todos los elementos de la lista que empiecen con alguna letra de la A a la C
    if re.findall('^[A-C]', elemento):
        print(elemento)

print('-------------------------------------')

for elemento in lista1:
    # Busca todos los elementos de la lista que termine con algun número del 3 al 4
    if re.findall('[3-4]$', elemento):
        print(elemento)

print('-------------------------------------')

for elemento in lista1:
    # Utilizando doble rango
    if re.findall('MA[3-4A-B]', elemento):
        print(elemento)

print('-------------------------------------')

for elemento in lista1:
    # Trae todo lo que tenga . y : despues del MA
    if re.findall('MA[.:]', elemento):
        print(elemento)
