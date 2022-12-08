'''
capitalize ()
    Devuelve una copia de la cadena con el primer carácter en mayúscula.
center (width)
    Devuelve la cadena centrada en una cadena de longitud width. Se rellena con espacios.
count (sub[, start[, end]])
    Devuelve cuántas veces aparece sub en la cadena S[start:end]. Los argumentos opcionales start y end se interpretan según la notación de corte.
encode ([encoding[,errors]])
    Devuelve una versión codoficada de la cadena. La codificación predeterminada es la codificación predeterminada de cadenas. 
    El parámetro opcional errors fija el esquema de gestión de errores. Su valor predeterminado es 'strict', que indica que los errores de codificación harán saltar ValueError. 
    Otros valores posibles son 'ignore' (ignorar) y 'replace' (reemplazar).
endswith (suffix[, start[, end]])
    Devuelve verdadero si la cadena finaliza con el sufijo suffix especificado, en caso contrario falso. 
    Si se da valor al parámetro opcional start, la comprobación empieza en esa posición. Si se da valor al parámetro opcional end, la comprobación finaliza en esa posición.
expandtabs ([tabsize])
    Devuelve una copia de la cadena con todos los tabuladores expandidos a espacios. Si no se indica el paso de tabulación tabsize se asume 8.
find (sub[, start[, end]])
    Devuelve el menor índice de la cadena para el que sub se encuentre, de tal modo que sub quede contenido en el rango [start, end). 
    Los argumentos opcionales start y end se interpretan según la notación de corte. Devuelve -1 si no se halla sub.
index (sub[, start[, end]])
    Como find(), pero lanza ValueError si no se encuentra la subcadena.
isalnum ()
    Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos y hay al menos un carácter. En caso contrario, devuelve falso.
isalpha ()
    Devuelve verdadero si todos los caracteres de la cadena son alfabéticos y hay al menos un carácter. En caso contrario, devuelve falso.
isdigit ()
    Devuelve verdadero si todos los caracteres de la cadena son dígitos y hay al menos un carácter. En caso contrario, devuelve falso.
islower ()
    Devuelve verdadero si todos los caracteres alfabéticos de la cadena están en minúscula y hay al menos un carácter susceptible de estar en minúsculas. En caso contrario, devuelve falso.
isspace ()
    Devuelve verdadero si todos los caracteres de la cadena son espacio en blanco (lo que incluye tabuladores, espacios y retornos de carro) y hay al menos un carácter. En caso contrario, devuelve falso.
istitle ()
    Devuelve verdadero la cadena tiene forma de título (anglosajón) y hay al menos un carácter. En caso contrario, devuelve falso. 
    Se considera que una cadena tiene formato de título si todas sus palabras están en minúsculas a excepción de la primera letra de cada una, que debe ser mayúscula.
isupper ()
    Devuelve verdadero si todos los caracteres alfabéticos de la cadena están en mayúscula y hay al menos un carácter susceptible de estar en mayúsculas. En caso contrario, devuelve falso.
join (seq)
    Devuelve una cadena formada ppor la concatenación de todos los elementos de la secuencia seq. Los elementos se separan por la cadena que proporciona el método. 
    Se lanza TypeError si alguno de los elementos no es una cadena.
ljust (width)
    Devuelve la cadena justificada a la izquierda en una cadena de longitud width. Se rellena la cadena con espacios. Se devuelve la cadena original si width es menor que len(s).
lower ()
    Devuelve una copia de la cadena convertida en minúsculas.
lstrip ()
    Devuelve una copia de la cadena con el espacio inicial eliminado.
replace (old, new[, maxsplit])
    Devuelve una copia de la cadena en la que se han sustituido todas las apariciones de old por new. 
    Si se proporciona el argumento opcional maxsplit, sólo se sustituyen las primeras maxsplit apariciones.
rfind (sub [,start [,end]])
    Devuelve el índice máximo de la cadena para el que se encuentra la subcadena sub, tal que sub está contenido en cadena[start,end]. 
    Los argumentos opcionales start y end se interpretan según la notación de corte. Devuelve -1 si no se encuentra sub.
rindex (sub[, start[, end]])
    Como rfind() pero lanza ValueError si no se encuentra sub.
rjust (width)
    Devuelve la cadena justificada a la derecha en una cadena de longitud width. Se rellena la cadena con espacios. Se devuelve la cadena original si width es menor que len(s).
rstrip ()
    Devuelve una copia de la cadena con el espacio al final suprimido.
split ([sep [,maxsplit]])
    Devuelve una lista de las palabras de la cadena, usando sep como delimitador de palabras. 
    Si se indica maxsplit, se devolverán como mucho maxsplit valores (el último elemento contendrá el resto de la cadena). 
    Si no se especifica sep o es None, cualquier espacio en blanco sirve de separador.
splitlines ([keepends])
    Devuelve una lista de las líneas de la cadena, dividiendo por límites de línea. 
    No se incluyen los caracteres limitadores en la lista resultante salvo que se proporcione un valor verdadero en keepends.
startswith (prefix[, start[, end]])
    Devuelve verdadero si la cadena comienza por prefix, en caso contrario, devuelve falso. 
    Si se proporciona el parámetro opcional start, se comprueba la cadena que empieza en esa posición. Si se proporciona el parámetro opcional end, se comprueba la cadena hasta esa posición.
strip ()
    Devuelve una copia de la cadena con el espacio inicial y final suprimido.
swapcase ()
    Devuelve una copia de la cadena con las mayúsculas pasadas a minúsculas y viceversa.
title ()
    Devuelve una versión con formato título, es decir, con todas las palabras en minúsculas excepto la primera letra, que va en mayúsculas.
translate (table[, deletechars])
    Devuelve una copia de la cadena donde se han eliminado todos los caracteres de deletechars y se han traducido los caracteres restantes según la tabla de correspondencia 
    especificada por la cadena table, que debe ser una cadena de longitud 256.
upper ()
    Devuelve una copia de la cadena en mayúsculas.
'''
