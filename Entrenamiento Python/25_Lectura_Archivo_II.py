from io import open
# Modo lectura (parametro )
archivo = open('archivo.txt', 'r')
# seek para posicionar el puntero en un lugar especifico del texto delarchivo
archivo.seek(9)
# each text line is a list part
texto = archivo.read()

print(texto)
