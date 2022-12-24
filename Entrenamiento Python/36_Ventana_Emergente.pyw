from tkinter import *
# Ventanas emergentes
from tkinter import messagebox
# Manejo de archivos
from tkinter import filedialog
root = Tk()
root.title('Menus')


def infoAdicional():
    # Como primer parametro el titulo de la ventana, y segundo parametro lo que va dentro
    messagebox.showinfo('Carlos Tittle', 'Carlos Content')


def avisoLicencia():
    messagebox.showwarning(
        'Licencia', 'Licencia 2022 activada permanentemente.')


'''
def salirAplicacion():
    # askquestion devuelve un valor yes, por lo que es ideal almacenar este valor en una variable para despues utilizarlo en condicionales
    valor = messagebox.askquestion('Salir', '¿Deseas salir de la aplicación?')
    if valor == 'yes':
        root.destroy()
'''


def salirAplicacion():
    # askokcancel devuelve un valor True o Flase al seleccionar una de las dos opciones en pantalla, por lo que es ideal almacenar este valor en una variable para despues utilizarlo en condicionales
    valor = messagebox.askokcancel(
        'Exit', 'Do you want to exit the application?')
    if valor == True:
        root.destroy()


def cerrarDocumento():
    valor = messagebox.askretrycancel(
        'Reintentar', 'No es posible cerrar el documento bloqueado')
    if valor == False:
        root.destroy()


def abrirFichero():
    # askopenfilename, metodo que devuelve la ruta del archivo que seleccionamos
    fichero = filedialog.askopenfilename(title='Open', initialdir='C:/', filetypes=(
        ('Ficheros de Texto', '*.txt'), ('Ficheros de Excel', '*.xlsx'), ('Todos los ficheros', '*.*')))
    print(fichero)


barraMenu = Menu(root)
root.config(menu=barraMenu)

# tearoff para sacar el separador inicial que hay al abrir un menu
menuFile = Menu(barraMenu, tearoff=0)
# Agregamos opciones al menu File
menuFile.add_command(label='New File')
menuFile.add_command(label='Open File', command=abrirFichero)
menuFile.add_separator()
menuFile.add_command(label='Save')
menuFile.add_command(label='Save as')
menuFile.add_separator()
menuFile.add_command(label='Close', command=cerrarDocumento)
menuFile.add_command(label='Exit', command=salirAplicacion)

menuEdit = Menu(barraMenu, tearoff=0)
menuEdit.add_command(label='Undo')
menuEdit.add_command(label='Redo')
menuEdit.add_separator()
menuEdit.add_command(label='Cut')
menuEdit.add_command(label='Copy')
menuEdit.add_command(label='Paste')
menuEdit.add_separator()
menuEdit.add_command(label='Find')
menuEdit.add_command(label='Replace')

menuTools = Menu(barraMenu)

menuHelp = Menu(barraMenu, tearoff=0)
menuHelp.add_command(label='License', command=avisoLicencia)
menuHelp.add_command(label='About Peppa App', command=infoAdicional)

barraMenu.add_cascade(label='File', menu=menuFile)
barraMenu.add_cascade(label='Edit', menu=menuEdit)
barraMenu.add_cascade(label='Tools', menu=menuTools)
barraMenu.add_cascade(label='Help', menu=menuHelp)


root.mainloop()
