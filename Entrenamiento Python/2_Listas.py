# Creacion de la lista
miLista = ['Carlos', 'Daniela', 'Angel',
           'Nacho', 'Abel', 'Mauri', 'David', 'Pipe']

print('------------- Numero especifico de la lista -----------')
print(miLista[2])

print('--------- Numero especifico de la lista (en reversa) ----------')
print(miLista[-2])

print('------------- Porcion de una lista -----------')
print(miLista[1:5])

print('------------- Porcion de una lista -----------')
print(miLista[2:])

print('------------- Agregando elemento al final de la lista -----------')
miLista.append('Leidy')
print(miLista)

print('------ Agregando elemento en un lugar especifico de la lista ------')
miLista.insert(1, 'Ariel')
print(miLista)

print('----------------- Agregar varios elementos a la lista ---------------')
miLista.extend(['Esteban', 'Debora'])
print(miLista)

print('--------- Obteniendo valor de indice de un elemento de la lista -----------')
print(miLista.index('Daniela'))

print('--------- Encontrar un elemento en la lista -----------')
print('Daniela' in miLista)

print('--------- Eliminar elemento especifico en la lista -----------')
miLista.remove('Daniela')
print(miLista[:])

print('--------- Eliminar elemento especifico en la lista con el index -----------')
miLista.pop(2)
print(miLista)

# Creacion segunda lista
miLista2 = ['Sandra', 'Lucia']

# Union de lista
miListaUnida = miLista+miLista2

print('------------------------ Lista unida -------------------------')
print(miListaUnida)

print('------------------------ Multilpicacion de la lista --------------------')
miListaMultiplicada = ['Chango', 'Antu'] * 3
print(miListaMultiplicada)
