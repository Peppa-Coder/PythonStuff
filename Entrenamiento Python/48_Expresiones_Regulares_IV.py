import re
# Repasando funciones match y search
# Utiles para patrones de busqueda en cadenas de texto
nombre1 = 'Sandra Lopez'
nombre2 = 'Saul Gomez'
nombre3 = 'Paul Lopez'
nombre4 = 'sandra Lopez'

# la funcion match siempre busca al principio y la funcion search busca en toda la cadena de texto
# re.IGNORECASE para que reconozca mayusculas y minusculas
if re.match('Sandra', nombre4, re.IGNORECASE):
    print('El nombre se ha encontrado')
else:
    print('No se ha encontrado ningun nombre')

print('----------------------------------')

# El . remplaza cualquier caracter que pueda haber en su lugar a la hora de realizare la busqueda
if re.match('.aul', nombre3):
    print('El nombre se ha encontrado')
else:
    print('No se ha encontrado ningun nombre')

# Para buscar digitos, utilizar '\d'