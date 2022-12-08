from tkinter import *

root = Tk()

miFrame = Frame(root)
miFrame.pack()

# Variable global que recibirá string de cualquier operacion que el usuario utilice
operacion = ''
# Variable donde se almacenara la suma de los valores introducidos
resultado = 0

# Especificamos que la variable va a contener en su interior un string de caracteres con StringVar
screenNumber = StringVar()

# Relacionamos la variable creada a la pantalla
screen = Entry(miFrame,  textvariable=screenNumber)
# Con columnspan le decimos cuantas columnas queremos que ocupe la pantalla
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(bg='black', fg='white', justify='right')

'''
# Set para establecer el numero 4 y como la variable screenNumber está relacionado a la pantlla, ahi es donde se escribirá, utilizamos el metodo get para obtener lo que ya está en pantalla y concatenamos el 4
def numeroPulsado():
    # En resumen este comando dice que el set de screenNumber será lo que ya hay en pantalla, mas un 4
    screenNumber.set(screenNumber.get() + '4')
'''


# Funcion mejorada que logra obtener lo que hay en pantalla y escribir un numero dependiendo del boton pulsado, asi no creamos una funcion para cada numero
def numeroPulsado(num):
    global operacion
    # Si el usuario presiona el boton suma, que no siga concatenando numeros y escriba el nuevo numero
    if operacion != '':
        screenNumber.set(num)
        # Vaciamos la variable operacion para que comience a concatenar nuevamente
        operacion = ''
    else:
        #Si no, que siga concatenando
        screenNumber.set(screenNumber.get() + num)


# Parametro sum para almacenar lo que hay en pantalla cuando pulso el boton +
def suma(num):
    global operacion
    global resultado
    # Para que el valor numerico que hay en pantalla se sume al resultado
    resultado+=float(num)
    operacion = 'suma'
    # Para que al presionar +, en la pantalla aparezca lo que vamos sumando
    screenNumber.set(resultado)


# No se puede llamar resultado la funcion porque ya hay una variable global llamada asi
def resultado_igual():
    global resultado
    # Esto hará que sume lo que está guardado en la variable resultado, mas lo que está en pantalla que aún no se ha sumado
    screenNumber.set(resultado+float(screenNumber.get()))
    # Se resetea la variable resultado para que despues de apretar el boton igual, empiece de 0
    resultado = 0

button7 = Button(miFrame, text='7', width=3,
                command=lambda: numeroPulsado('7'))
button7.grid(row=2, column=1)

button8 = Button(miFrame, text='8', width=3,
                command=lambda: numeroPulsado('8'))
button8.grid(row=2, column=2)

button9 = Button(miFrame, text='9', width=3,
                command=lambda: numeroPulsado('9'))
button9.grid(row=2, column=3)

buttonDiv = Button(miFrame, text='/', width=3)
buttonDiv.grid(row=2, column=4)

# Sin lambda, la funcion numeroPulsado recibiria el parametro 4 asignado en la llamada inmediatamente, por lo que al ser llamada la funcion, no espera que el usuario presione un boton y se muestra el resultado antes de tiempo.
# En resumen, lo que hace lambda es que no ejecuta la funcion, y lo convierte en una referencia a la funcion para que la funcion se llame cuando el usuario pulse el boton y no apenas lea la llamada en el codigo
button4 = Button(miFrame, text='4', width=3,
                command=lambda: numeroPulsado('4'))
button4.grid(row=3, column=1)

button5 = Button(miFrame, text='5', width=3,
                command=lambda: numeroPulsado('5'))
button5.grid(row=3, column=2)

button6 = Button(miFrame, text='6', width=3,
                command=lambda: numeroPulsado('6'))
button6.grid(row=3, column=3)

buttonMult = Button(miFrame, text='*', width=3)
buttonMult.grid(row=3, column=4)

button1 = Button(miFrame, text='1', width=3,
                command=lambda: numeroPulsado('1'))
button1.grid(row=4, column=1)

button2 = Button(miFrame, text='2', width=3,
                command=lambda: numeroPulsado('2'))
button2.grid(row=4, column=2)

button3 = Button(miFrame, text='3', width=3,
                command=lambda: numeroPulsado('3'))
button3.grid(row=4, column=3)

buttonSubt = Button(miFrame, text='-', width=3)
buttonSubt.grid(row=4, column=4)

button0 = Button(miFrame, text='0', width=3,
                command=lambda: numeroPulsado('0'))
button0.grid(row=5, column=1)

buttonDot = Button(miFrame, text='.', width=3,
                command=lambda: numeroPulsado('.'))
buttonDot.grid(row=5, column=2)

buttonEqual = Button(miFrame, text='=', width=3, command=lambda:resultado_igual())
buttonEqual.grid(row=5, column=3)

# command=lambda:suma(screenNumber.get() para que obtenga lo que esta escrito en pantalla
buttonAdd = Button(miFrame, text='+', width=3, command=lambda:suma(screenNumber.get()))
buttonAdd.grid(row=5, column=4)

root.mainloop()
