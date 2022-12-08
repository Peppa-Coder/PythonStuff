#YIELD FROM ES PARA ACCEDER A ELEMENTOS DENTRO DE OTROS ELEMENTOS SIN NECESIDAD
# DE USAR FOR ANIDADOS COMO SE VE EN EL CODIGO COMENTADO
def generadorCiudad(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudades_devueltas = generadorCiudad(
    'Santiago', 'Maipu', 'Providencia', 'Huechuraba')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
