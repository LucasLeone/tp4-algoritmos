'''
    Se trata de resolver el siguiente problema escolar: Dadas las notas de los alumnos de
    un colegio (primer año-secundaria), en las diferentes asignaturas (5 como límite), se trata
    de calcular la media de cada asignatura, la media total de la clase y ordenar los alumnos
    por orden decreciente de notas medias individuales.
'''
import random

matriz = []

print('10 ALUMNOS DE PRIMER AÑO')

for i in range(0, 10):
    matriz.append([])
    for j in range(0, 5):
        matriz[i].append(random.randint(1, 10))

media_materias = []

while True:
    notas = []
    
    x = 0
    y = 0
    for fila in range(0, 10):
        for columna in range(0, 5):
            notas.append(matriz[fila][columna])

            x += 1
            y += 1

            if x == 9 and y == 4:
                break

    print(notas)
