def divide():
    try:
        op1 = (float(input('Introduce el primer numero: ')))
        op2 = (float(input('Introduce el segundo numero: ')))
        print(f'La division es: {op1/op2}')
    except ValueError:
        print('Valor erroneo ingresado')
    except ZeroDivisionError:
        print('No se puede dividir por 0')
    finally:  # Esto hace que se ejecute siempre, existan o no errores, aqui no es necesario.
        print('Calculo finalizado')


divide()
