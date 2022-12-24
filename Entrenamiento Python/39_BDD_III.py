import sqlite3

miConexion = sqlite3.connect('Gestion Productos')

# Cursor para usar sentencioas sql
miCursor = miConexion.cursor()

miCursor.execute('SELECT * FROM Productos WHERE SECCION ="Cerámica"')

#fetchall para devolver todos los registros de la consulta sql en un array
productos = miCursor.fetchall()

print(productos)

miCursor.execute('UPDATE Productos SET precio = 35 WHERE nombre_articulo = "Camiseta"')

miCursor.execute('DELETE FROM Productos WHERE nombre_articulo = "Camión"')

miConexion.commit()

miConexion.close()
