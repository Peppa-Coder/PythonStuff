import sqlite3

miConexion = sqlite3.connect('Gestion Productos')

# Cursor para usar sentencioas sql
miCursor = miConexion.cursor()

# Triple comillas para ejecutar varias lineas de codigo y no escribir todo el sql en una
miCursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos(
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(50) UNIQUE,
        precio INTEGER,
        seccion VARCHAR(20))
''')
# UNIQUE para hacer que un campo no se repita ↑
variosProductos = [
    ('Camiseta', 10, 'Deportes'),
    ('Jarrón', 8, 'Cerámica'),
    ('Camión', 10, 'Jugueteria')
]

miCursor.executemany('INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)', variosProductos)

miConexion.commit()

miConexion.close()
