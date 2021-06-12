'''
    Se dispone de una matriz de 100 números enteros. 
    Calcular su valor máximo y el orden que ocupa en la tabla.
'''
import random

matriz = []

for i in range(0, 10):
    matriz.append([])
    for j in range(0, 10):
        matriz[i].append(random.randint(0, 100))

maximo = 0
x = 0
y = 0

for fila in matriz:
    for elemento in fila:
        if elemento > maximo:
            maximo = elemento


for a in range(0, 10):
    for b in range(0, 10):
        if matriz[a][b] == maximo:
            x = a
            y = b

print(f'El valor maximo es {maximo} y esta en la posicion ({x}, {y})')
print(matriz)