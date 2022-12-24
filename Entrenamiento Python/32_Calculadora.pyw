from tkinter import *

root = Tk()

miFrame = Frame(root)
miFrame.pack()

# Variable global que recibirá string de cualquier operacion que el usuario utilice
operacion = ''
# Variable donde se almacenara la suma de los valores introducidos
resultado = 0

reset_pantalla=False

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


def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla != False:
        screenNumber.set(num)
        reset_pantalla = False
    else:
        #Si no, que siga concatenando
        screenNumber.set(screenNumber.get() + num)


# Parametro sum para almacenar lo que hay en pantalla cuando pulso el boton +
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    # Para que el valor numerico que hay en pantalla se sume al resultado
    resultado+=int(num)
    operacion = 'suma'
    reset_pantalla = True
    # Para que al presionar +, en la pantalla aparezca lo que vamos sumando
    screenNumber.set(resultado)

num1=0

contador_resta=0

def resta(num):

    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla
    
    if contador_resta == 0:
        num1=int(num)
        resultado=num1
    else:
        if contador_resta == 1:
            resultado=num1-int(num)
        else:
            resultado = int(resultado)-int(num)
        screenNumber.set(resultado)
        resultado = screenNumber.get()
    
    # Para que el valor numerico que hay en pantalla se reste al resultado
    contador_resta = contador_resta + 1
    operacion = 'resta'
    # Para que al presionar +, en la pantalla aparezca lo que vamos sumando
    reset_pantalla=True



# No se puede llamar resultado la funcion porque ya hay una variable global llamada asi
def resultado_igual():
    global resultado
    global operacion
    global contador_resta
    if operacion == 'suma':
        screenNumber.set(resultado+int(screenNumber.get()))
        resultado = 0
    elif operacion == 'resta':
        screenNumber.set(int(resultado))-int(screenNumber.get())
        resultado = 0
        contador_resta = 0
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

buttonSubt = Button(miFrame, text='-', width=3, command=lambda:resta(screenNumber.get()))
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
