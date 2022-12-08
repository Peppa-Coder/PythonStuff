""" Funcion normal
def generaPares(limite):

    num = 1
    miLista = []

    while num < limite:
        miLista.append(num*2)
        num += 1
    return miLista

print(generaPares(10))
 """
#Generador (mas eficiente en comparacion a la funcion)
def generaPares(limite):

    num = 1

    while num < limite:
        yield num*2
        num += 1

devuelvePares=generaPares(10)
        
'''for i in devuelvePares:
   print(i)''' 

print(next(devuelvePares))

print('Aqui podria haber mas codigo')

print(next(devuelvePares))

print('Aqui podria haber mas codigo')

print(next(devuelvePares))