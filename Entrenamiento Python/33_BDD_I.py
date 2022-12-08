import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()
# miCursor.execute(
#    'CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGRER, SECCION VARCHAR(20))')

# miCursor.execute(
#    'INSERT INTO PRODUCTOS VALUES("BALON", 15, "DEPORTES")')
'''
variosProductos=[
    ('Camiseta', 10, 'Deportes'),
    ('Jarrón', 8, 'Cerámica'),
    ('Camión', 10, 'Jugueteria')
]

miCursor.executemany('INSERT INTO PRODUCTOS VALUES (?,?,?)', variosProductos)
'''
miCursor.execute(
    'SELECT * FROM PRODUCTOS')

# para recuperar la informacion de la base de datos utilizar fetchall, donde devuelve una lista con todos los registros que nos devuelve la instruccion SQL
variosProductos = miCursor.fetchall()

# visualizamos la informacion almacenada en la variable varios productos, recorriendola con un ciclo for para que traiga uno a uno
for producto in variosProductos:
    print('Nombre Producto:', producto[0],'\nCategoría Producto:', producto[2], '\nPrecio:', producto[1], 'USD')

miConexion.commit()

miConexion.close()
