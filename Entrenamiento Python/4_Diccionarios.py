# Creacion del diccionario
miDiccionario = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago',
                 'Francia': 'Paris', 'Reino Unido': 'Londres'}
# Buscar elemento del diccionario a traves de una clave
print(miDiccionario['Argentina'])
# Agregar elemento al diccionario
miDiccionario['Italia'] = 'Lisboa'
print(miDiccionario)
# Modificar elemento de un diccionario (se sobrescribe)
miDiccionario['Italia'] = 'Roma'
print(miDiccionario)
# Eliminar elemento de un diccionario
del miDiccionario['Reino Unido']
print(miDiccionario)
miDiccionario[23] = 'Jordan'
print(miDiccionario)
# Buscar a Jordan con su clave
print(miDiccionario[23])
# Creacion de tupla
miTupla = ('Carlos', 'Roberto', 'Daniela')
# Agregando tupla al diccionario
miDiccionario['Nombres'] = miTupla
print(miDiccionario)
# Creando nuevo diccionario con asignacion de claves de la tupla
nuevoDiccionario = {miTupla[0]: 'Chile', miTupla[1]: 'Francia'}
# Busqueda dentro del diccionario con clave de la tupla
print(nuevoDiccionario['Carlos'])
# Mostramos la tupla desde el diccionario
print(miDiccionario['Nombres'])
# Mostrar claves del nuevo diccionario
print(nuevoDiccionario.keys())
# Mostrando valores del nuevo diccionario
print(nuevoDiccionario.values())
# Mostrando largo del nuevo diccionario
print(len(nuevoDiccionario))
