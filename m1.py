'''
    Escribir un algoritmo que permita obtener el número de elementos positivos,
    negativos, nulos, mayores a 250, iguales a 19 e inferiores a 90 de una matriz de
    50x50 componentes
'''
from math import inf
import random

matriz = []
positivos = []
negativos = []
nulos = []
mayores = []
iguales_19 = []
inferiores = []

for i in range(0, 50):
    matriz.append([])
    for j in range(0, 50):
        matriz[i].append(random.randint(-500, 500))


for i in range(0, len(matriz) - 1):
    for j in matriz[i]:
        if j > 0:
            positivos.append(j)

        if j < 0:
            negativos.append(j)

        if j == 0:
            nulos.append(j)

        if j > 250:
            mayores.append(j)
        
        if j == 19:
            iguales_19.append(j)

        if j < 90:
            inferiores.append(j)

print(f'Hay un total de {len(positivos)} numeros positivos y son:')
print(positivos)
print(' ')
print(f'Hay un total de {len(negativos)} numeros negativos y son:')
print(negativos)
print(' ')
print(f'Hay un total de {len(nulos)} elementos nulos')
print(' ')
print(f'Hay un total de {len(mayores)} numeros mayores a 250 y son:')
print(mayores)
print(' ')
print(f'Hay un total de {len(iguales_19)} numeros iguales a 19')
print(' ')
print(f'Hay un total de {len(inferiores)} numeros inferiores a 90 y son:')
print(inferiores)
