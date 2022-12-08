import pickle
# Guardamos la apertura del archivo en modo lectura binaria dentro de la variable fichero
fichero = open('lista_nombres', 'rb')
# Utilizamos load para acceder a la informacion del archivo leido y lo guardamos en la variable lista
lista = pickle.load(fichero)
# Visualizamos la informacion
print(lista)
