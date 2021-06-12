'''
    Calcular la suma de los números de
    la diagonal principal de una matriz 4 por 4.
'''
import random

matriz = []

for i in range(0, 4):
    matriz.append([])
    for j in range(0, 4):
        matriz[i].append(random.randint(0, 100))

principal = []

for x in range(0, 4):
    principal.append(matriz[x][x])

principal = sum(principal)

print(matriz)
print(f'La suma de la principal es: {principal}')