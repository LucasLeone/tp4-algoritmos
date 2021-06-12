'''
    Calcular la suma de todos los elementos de una matriz 5x5,
    así como la media aritmética de los mismos.
'''
import random

matriz = []

for i in range(0, 5):
    matriz.append([])
    for j in range(0, 5):
        matriz[i].append(random.randint(0, 100))

suma = 0
elementos = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        elementos += 1

media = suma / elementos

print(f'La suma de todos los elementos es {suma} y la media es {media}')
print(matriz)