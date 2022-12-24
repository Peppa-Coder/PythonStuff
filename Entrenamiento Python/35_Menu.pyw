from tkinter import *

root = Tk()

root.title('Menus')

barraMenu = Menu(root)
root.config(menu=barraMenu)

# tearoff para sacar el separador inicial que hay al abrir un menu
menuFile = Menu(barraMenu, tearoff=0)
#Agregamos opciones al menu File
menuFile.add_command(label='New File')
menuFile.add_command(label='Open File')
menuFile.add_separator()
menuFile.add_command(label='Save')
menuFile.add_command(label='Save as')
menuFile.add_separator()
menuFile.add_command(label='Exit')

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

menuHelp = Menu(barraMenu)

barraMenu.add_cascade(label='File', menu=menuFile)
barraMenu.add_cascade(label='Edit', menu=menuEdit)
barraMenu.add_cascade(label='Tools', menu=menuTools)
barraMenu.add_cascade(label='Help', menu=menuHelp)


root.mainloop()
