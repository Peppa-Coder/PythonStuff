from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

root.title('Primer Formulario')
barraMenu = Menu(root)
root.config(menu=barraMenu)
root.geometry('300x380')


def crearBase():
    try:
        miConexion = sqlite3.connect("Gestion Primera App")
        miCursor = miConexion.cursor()
        miCursor.execute('''
        CREATE TABLE Usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres VARCHAR(50),
            apellidos VARCHAR(50),
            password VARCHAR(12),
            direccion VARCHAR(50),
            comentario VARCHAR(200))
        ''')
        messagebox.showinfo(
            'Base de Datos', 'Conexión establecida correctamente')
    except:
        messagebox.showwarning('¡Atención!', 'Conexión existente')


def cerrarApp():
    valor = messagebox.askquestion('Salir', 'Desea cerrar la aplicación?')
    if valor == 'yes':
        root.destroy()


def limpiarCampos():
    zId.set('')
    zName.set('')
    zSurname.set('')
    zPass.set('')
    zAddr.set('')
    commentText.delete(1.0, END)


def crearCampo():
    miConexion = sqlite3.connect('Gestion Primera App')
    miCursor = miConexion.cursor()
    # Guardamos en una variable toda la informacion para luego hacer la consulta parametrizada
    datos = zName.get(), zSurname.get(), zPass.get(), zAddr.get(), commentText.get('1.0', END)
    # Codigo con concatenacion sin consulta parametrizada
    '''
    miCursor.execute('INSERT INTO Usuarios VALUES(NULL, "' + zName.get() +
        '","' + zSurname.get() +
        '","' + zPass.get() +
        '","' + zAddr.get() +
        '","' + commentText.get('1.0', END) + '")')
    '''
    # Consulta parametrizada en la creacion para evitar SQL INJECTION
    miCursor.execute('INSERT INTO Usuarios VALUES(NULL,?,?,?,?,?)',(datos))
    miConexion.commit()
    messagebox.showinfo('Crear', 'Registro creado exitosamente')


def leerCampo():
    miConexion = sqlite3.connect('Gestion Primera App')
    miCursor = miConexion.cursor()
    miCursor.execute('SELECT * FROM Usuarios WHERE id =' + zId.get())
    user = miCursor.fetchall()
    for usuario in user:
        zId.set(usuario[0])
        zName.set(usuario[1])
        zSurname.set(usuario[2])
        zPass.set(usuario[3])
        zAddr.set(usuario[4])
        commentText.insert(1.0, usuario[5])
    miConexion.commit()


def modificarCampo():
    miConexion = sqlite3.connect('Gestion Primera App')
    miCursor = miConexion.cursor()
    # Guardamos en una variable toda la informacion para luego hacer la consulta parametrizada
    datos = zName.get(), zSurname.get(), zPass.get(), zAddr.get(), commentText.get('1.0', END)    
    # Codigo con concatenacion sin consulta parametrizada
    '''
        miCursor.execute('UPDATE Usuarios SET nombres = "' + zName.get() +
        '", apellidos="' + zSurname.get() +
        '", password="' + zPass.get() +
        '", direccion="' + zAddr.get() +
        '", comentario="' + commentText.get(1.0, END) +
        '" WHERE id=' + zId.get())
    '''
    # Consulta parametrizada en la modificacion para evitar SQL INJECTION
    miCursor.execute('UPDATE Usuarios SET nombres=?, apellidos=?, password=?, direccion=?, comentario=? WHERE id=' + zId.get(), (datos))
    miConexion.commit()
    messagebox.showinfo('Modificar', 'Registro modificado exitosamente')

def eliminarCampo():
    miConexion = sqlite3.connect('Gestion Primera App')
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM Usuarios WHERE id =" + zId.get())
    miConexion.commit()
    messagebox.showinfo('Eliminar', 'Registro eliminado exitosamente')

menuBD = Menu(barraMenu, tearoff=0)
menuBD.add_command(label='Conectar', command=crearBase)
menuBD.add_command(label='Salir', command=cerrarApp)

menuFunciones = Menu(barraMenu, tearoff=0)
menuFunciones.add_command(label='Limpiar Campos', command=limpiarCampos)

menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label='Licencia')
menuAyuda.add_command(label='Acerca de...')

barraMenu.add_cascade(label='Base de Datos', menu=menuBD)
barraMenu.add_cascade(label='Funciones', menu=menuFunciones)
barraMenu.add_cascade(label='Ayuda', menu=menuAyuda)

frame1 = Frame(root)
frame1.pack()
frame1.config()

frame2 = Frame(root)
frame2.pack()

idLabel = Label(frame1, text='Id:')
idLabel.grid(row=0, column=0, sticky='e')

nameLabel = Label(frame1, text='Nombres:')
nameLabel.grid(row=1, column=0, sticky='e')

surnameLabel = Label(frame1, text='Apellidos:')
surnameLabel.grid(row=2, column=0, sticky='e')

passLabel = Label(frame1, text='Contraseña:')
passLabel.grid(row=3, column=0, sticky='e')

adressLabel = Label(frame1, text='Dirección:')
adressLabel.grid(row=4, column=0, sticky='e')

textFrameLabel = Label(frame1, text='Comentarios:')
textFrameLabel.grid(row=5, column=0, sticky='e')

# Hay que usar StringVar para que se entienda que estos entry recibiran cadenas de tipo string y asi se podran resetear
zId = StringVar()
zName = StringVar()
zSurname = StringVar()
zPass = StringVar()
zAddr = StringVar()

idEntry = Entry(frame1, textvariable=zId)
idEntry.grid(row=0, column=1, padx=10, pady=10)

nameEntry = Entry(frame1, textvariable=zName)
nameEntry.grid(row=1, column=1, padx=10, pady=10)

surnameEntry = Entry(frame1, textvariable=zSurname)
surnameEntry.grid(row=2, column=1, padx=10, pady=10)

passEntry = Entry(frame1, textvariable=zPass, show='*')
passEntry.grid(row=3, column=1, padx=10, pady=10)

adressEntry = Entry(frame1, textvariable=zAddr)
adressEntry.grid(row=4, column=1, padx=10, pady=10)


commentText = Text(frame1)

scrollY = Scrollbar(frame1, command=commentText.yview)
# Utilizo sticky='nsew' para que el scroll se adapte al cuadro de texto
scrollY.grid(row=5, column=2, sticky='nsew')

commentText.grid(row=5, column=1, padx=10, pady=10)
# Hacemos que la scrollbar indique en que posicion del cuadro estamos
commentText.config(width=16, height=6, yscrollcommand=scrollY.set)


createButton = Button(frame2, text='Crear', command=crearCampo)
createButton.grid(row=0, column=0, padx=10, pady=10)

createButton = Button(frame2, text='Leer', command=leerCampo)
createButton.grid(row=0, column=1, padx=10, pady=10)

createButton = Button(frame2, text='Modificar', command=modificarCampo)
createButton.grid(row=0, column=2, padx=10, pady=10)

createButton = Button(frame2, text='Eliminar', command=eliminarCampo)
createButton.grid(row=0, column=3, padx=10, pady=10)
root.mainloop()
