for letra in 'Python':
    if letra == 'h':
        continue  # Esto hace el ciclo siga sin imprimir la letra h, ya que continue esta antes del print
    print(letra)

nombre = 'Carlos Muñoz Carrasco'
contador = 0
for i in nombre:
    if i == ' ':
        continue
    contador += 1
print(f'La cantidad de letras del nombre es: {contador}')


class MiClase:
    pass  # Para implementar mas tarde


email = input('Introduce tu email, por favor: ')

for i in email:
    if i == '@':
        arroba=True
        break;
else:
    arroba=False
print(arroba)