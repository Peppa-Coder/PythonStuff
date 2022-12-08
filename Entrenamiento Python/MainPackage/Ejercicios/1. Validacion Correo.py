''' Crea un programa que pida introducir una dirección de email por teclado. El programa 
debe imprimir en consola si la dirección de email es correcta o no en función de si esta 
tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o 
ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email 
o al final, la dirección también será errónea,'''


def validarEmail():
    email = input('Introduce tu email: ')
    arroba = email.count('@')
    if (arroba != 1 or email.rfind('@') == (len(email)-1) or email.find('@') == 0):
        print('El email no es correcto')
        print((len(email)-1))
    else:
        print('El mail es correcto')

validarEmail()
