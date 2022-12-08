import pickle
# Creacion de lista
lista_nombres = ['Pedro', 'Ana', 'Maria', 'Isabel ']
# Creacion fichero externo para que escriba y transforme a codigo binario(nombre, modo wb (writebinary))
fichero_binario = open('lista_nombres', 'wb')
# Volcado de la lista al fichero (informacion a volcar, nombre de fichero donde se volcara)
pickle.dump(lista_nombres, fichero_binario)
# cierra el fichero
fichero_binario.close()
# elimina de la memoria el fichero
del fichero_binario
