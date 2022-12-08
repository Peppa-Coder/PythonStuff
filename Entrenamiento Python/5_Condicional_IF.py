print('####### Programa de evaluacion de notas de estudiantes ########')


# Utilizando input
nota_estudiante = input('Introduce la nota del estudiante: ')


def evaluacion(nota):  # Creacion de funcion
    valoracion = 'Aprobado'
    if nota < 4:
        valoracion = 'Reprobado'
    return valoracion


print(evaluacion(int(nota_estudiante)))
