from io import open
# parametros (nombre de archivos, modo (w para writing))
archivo = open('archivo.txt', 'w')

frase = 'Estupendo dia para estudiar Python \n sobretodo para rellenar mi portafolio'

archivo.write(frase)

archivo.close()
