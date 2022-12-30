import re
# USANDO METACARACTERES
lista = [
    'http://www.facebook.com',
    'ftp://www.facebook.es',
    'http://www.facebook.es',
    'ftp://www.facebook.com',
]
# $ Para buscar el final
for elemento in lista:
    if re.findall('es$', elemento):
        print(elemento)

print('---------------------------------------')
# ^ Para buscar el inicio
for elemento in lista:
    if re.findall('^ftp', elemento):
        print(elemento)

print('---------------------------------------')

lista1 = [
    'hombres',
    'mujeres',
    'niñas',
    'niños',
    'camion',
    'camión',
]

for elemento in lista1:
    if re.findall('niñ[ao]s', elemento):
        print(elemento)

print('---------------------------------------')

for elemento in lista1:
    if re.findall('cami[oó]n', elemento):
        print(elemento)
