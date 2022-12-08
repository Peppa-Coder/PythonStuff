from io import open
# Modo lectura (parametro )
archivo = open('archivo.txt', 'r')
# each text line is a list part
lineas_texto = archivo.readlines()

archivo.close()

print(lineas_texto[1])
