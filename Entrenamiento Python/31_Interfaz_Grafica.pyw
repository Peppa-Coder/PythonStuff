# Libreria a utilizar de python
from tkinter import *
# Libreria ideal
from PyQt5 import *
# Creacion de Ventana
raiz = Tk()

raiz.title('Primera Ventana')

# No se puede redimensionar la ventana Parametro tipo booleano 1- True 0- False (Ancho, Largo)
raiz.resizable(450, 450)

# Tamaño por defecto de la ventana
raiz.geometry('650x350')

# Modificamos el background
raiz.config(bg='')

# miImagen = PhotoImage(file='./Iconos/favicon.png')

# Creamos el frame
miFrame = Frame(bg='green')
miFrame1 = Frame(bg='red')
miFrame2 = Frame(height='100', width='300', bg='purple')

cuadroNombres = Entry(miFrame2)
cuadroNombres.grid(row=0, column=1, padx=4, pady=4)

cuadroApellidos = Entry(miFrame2)
cuadroApellidos.grid(row=1, column=1, padx=4, pady=4)

cuadroEmail = Entry(miFrame2)
cuadroEmail.grid(row=2, column=1, padx=4, pady=4)

cuadroPassword = Entry(miFrame2)
cuadroPassword.grid(row=3, column=1, padx=4, pady=4)
cuadroPassword.config(show='*')

textoDescripcion = Text(miFrame2)
textoDescripcion.grid(row=4, column=1, padx=4, pady=4)


# Creacion de scrollbar para el cuadro de texto de la descripcion
scrollY = Scrollbar(miFrame2, command=textoDescripcion.yview)
# Utilizo sticky='nsew' para que el scroll se adapte al cuadro de texto
scrollY.grid(row=4, column=2, sticky='nsew')
# Hacemos que la scrollbar indique en que posicion del cuadro estamos
textoDescripcion.config(width=16, height=10, yscrollcommand=scrollY.set)

# Labels son para mostrar texto generalmente e imagenes
miLabel = Label(miFrame, text='Mi primera app de escritorio en Python', font=(
    'Comic Sans MS', 18))

# grid divide el contenedor en varios cuadros como un cuaderno, donde se le da posicion al label en este caso con row y column
labelNombres = Label(miFrame2, text='Nombres:', font=('Comic Sans MS', 8))
labelNombres.grid(row=0, column=0, sticky='e', padx=4, pady=4)

# sticky funciona con puntos cardinales (w e n s)
labelApellidos = Label(miFrame2, text='Apellidos:', font=('Comic Sans MS', 8))
labelApellidos.grid(row=1, column=0, sticky='e', padx=4, pady=4)

labelEmail = Label(miFrame2, text='Email:', font=('Comic Sans MS', 8))
labelEmail.grid(row=2, column=0, sticky='e', padx=4, pady=4)

labelPassword = Label(miFrame2, text='Contraseña:', font=('Comic Sans MS', 8))
labelPassword.grid(row=3, column=0, sticky='e', padx=4, pady=4)

labelDescripcion = Label(miFrame2, text='Descripción:',
    font=('Comic Sans MS', 8))
labelDescripcion.grid(row=4, column=0, sticky='e', padx=4, pady=4)

def codigoButtonEnvio():
    pass

buttonEnvio = Button(miFrame2, text='Finalizar', command=codigoButtonEnvio)
buttonEnvio.grid(row=5, column=1)
#miLabel1 = Label(miFrame, image=miImagen)

# Empaquetamos el frame y lo ponemos en la parte inferior rellenado horizontalmente
miFrame.pack(side='bottom', fill='x')
miLabel.place(x=150)
# miLabel1.place(x=150)

miFrame1.pack(side='top', fill='x')

# side no esta funcionando
miFrame2.pack()

# Bucle infinito que hace que la ventana se mantenga abierta permanentemente, es importante que este metodo este siempre al final
raiz.mainloop()
