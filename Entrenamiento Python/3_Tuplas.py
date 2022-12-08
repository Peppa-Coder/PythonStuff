# Creacion de la tupla
miTupla = ('Carlos', 10, 'Daniela', 20.5, 10)
# Mostrar indice 2 de la tupla
print(miTupla[2])
# Mostramos la tupla
print(miTupla)
# Transformar tupla en una lista
miLista = list(miTupla)
# Mostrar tupla convertida en lista
print(miLista)
# Encontrar valor dentro de la tupla
print('Daniela' in miTupla)
# Saber cuantas veces se encuentra un elemento dentro de una tupla
print(miTupla.count(10))
# Saber la longitud de una tupla
print(len(miTupla))
# Creando una tupla unitaria (debe ir la coma al final)
miTupla1 = ('Juan',)
# Revisando largo de la tupla unitaria
print(len(miTupla1))
# Creacion tuplaFecha
tuplaFecha = ('Carlos', 30, 11, 2001)
# Asignacion de valores de la tupla a las variables declaradas
nombre, dia, mes, anio = tuplaFecha
# Desempaquetado de tuplas
print(nombre)
print(dia)
print(mes)
print(anio)
# Buscar indice de un elemento dentro de una tupla
print(tuplaFecha.index(11))
