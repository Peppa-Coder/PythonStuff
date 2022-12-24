from tkinter import *

root = Tk()

# variable que almacene valores de tipo entero
varOpcion = IntVar()


def imprimir():

    if varOpcion.get() == 1:

        etiqueta.config(text='Has elegido Masculino')

    elif varOpcion.get() == 2:

        etiqueta.config(text='Has elegido Femenino')

    else:
        etiqueta.config(text='Has elegido Otro')


Label(root, text='Genero').pack()

# con los parametros variable y value estos funcionan independientemente, es decir, solo se puede seleccionar uno
Radiobutton(root, text='Masculino', variable=varOpcion,
            value=1, command=imprimir).pack()

Radiobutton(root, text='Femenino', variable=varOpcion,
            value=2, command=imprimir).pack()

Radiobutton(root, text='Otro', variable=varOpcion,
            value=3, command=imprimir).pack()

etiqueta = Label(root, text='Aqui aparecerá lo que eliges')
etiqueta.pack()

root.mainloop()
