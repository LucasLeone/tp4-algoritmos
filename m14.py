'''
    Escribir un algoritmo que lea 100 resultado de análisis de sangre y los ponga en
    orden ascendente utilizando un método de ordenación.
'''
import random

vector = []

for i in range(0, 100):
    vector.append(random.randint(30, 200))

for i in range(1, len(vector)):
    for j in range(0, len(vector) - i):
        if (vector[j+1] < vector[j]):
            aux = vector[j]
            vector[j] = vector[j+1]
            vector[j+1] = aux

print(vector)