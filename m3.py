'''
    Leer una matriz de 3 por 3 elementos y calcular la suma de cada una de sus filas y
    columnas, dejando dichos resultados en dos vectores, uno de la suma de filas y otro
    de las columnas.
'''
import random

matriz = []

for i in range(0, 3):
    matriz.append([])
    for j in range(0, 3):
        matriz[i].append(random.randint(0, 10))

filas = []
for i in matriz:
    suma = sum(i)
    filas.append(suma)

columnas = []
for i in zip(*matriz):
    suma = sum(i)
    columnas.append(suma)

print(matriz)
print(filas)
print(columnas)