# las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda,
#  sirven para el trabajo y procesamiento de texto
import re

cadena = 'Aprendiendo expresiones regulares en Python. Python es felicidad'

textoBuscar = 'Python'

# search (texto que buscamos, texto donde queremos buscar)
textoEncontrado = re.search(textoBuscar, cadena)

print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())
print(re.findall(textoBuscar, cadena))
print(len(re.findall(textoBuscar, cadena)))
