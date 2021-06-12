'''
    Calcular el número de elementos de negativos, cero y 
    positivos de una matriz de 9x9 elementos.
'''
import random

matriz = []

for i in range(0, 9):
    matriz.append([])
    for j in range(0, 9):
        matriz[i].append(random.randint(-100, 100))

negativos = 0
cero = 0
positivos = 0

for fila in matriz:
    for elemento in fila:
        if elemento > 0:
            positivos += 1
        elif elemento == 0:
            cero += 1
        elif elemento < 0:
            negativos += 1

print(f'Hay un total de {negativos} numeros negativos')
print(f'Hay un total de {cero} numeros que son ceros') 
print(f'Hay un total de {positivos} numeros positivos')
