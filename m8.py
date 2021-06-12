'''
    Calcular las medias de las estaturas de una clase. Deducir 
    cuántos son más altos que la media y cuántos más bajos que dicha media.
'''
import random

matriz = []

for i in range(0, 5):
    matriz.append([])
    for j in range(0, 5):
        matriz[i].append(random.randint(150, 210))

media = 0

suma = 0
elementos = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        elementos += 1

media = suma / elementos

altos = 0
bajos = 0

for fila in matriz:
    for elemento in fila:
        if elemento >= media:
            altos += 1
        else:
            bajos += 1

print(f'La media de altura de una clase es de {media}cms, hay {altos} alumnos mayores a la media y {bajos} menores a la media')