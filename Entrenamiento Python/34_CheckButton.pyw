from tkinter import *

root = Tk()

root.title('RadioButton')

vacuno=IntVar()
pollo=IntVar()
cerdo=IntVar()

def opcionesViaje():
    # Esta sera la variable donde se almacenará el texto que aparecerá al final de la interfaz
    opcionEscogida = ''
    if vacuno.get()==1:
        opcionEscogida+=' Vacuno'
    if pollo.get()==1:
        opcionEscogida+=' Pollo'
    if cerdo.get()==1:
        opcionEscogida+=' Cerdo'
    # Esto hace que la variable textoFinal guarde en su interior lo que tenga la variable opcionEscogida
    textoFinal.config(text=opcionEscogida)


frame=Frame(root)
frame.pack()

Label(frame,text='Elige lo que te gusta:', width=50).pack()

Checkbutton(frame,text='Vacuno', variable=vacuno, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text='Pollo', variable=pollo, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text='Cerdo', variable=cerdo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame, text='Aqui apareceran las opciones escogidas')
textoFinal.pack()


root.mainloop()