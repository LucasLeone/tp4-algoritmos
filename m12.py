'''
    Se necesita cargar una matriz de 50 elementos, obtener cuántos elementos son pares
    y cuántos son impares. Luego se pide la sumatoria de aquellos números que se
    encuentran posesionados en celdas pares. Indicar el mayor y menor elemento de la
    lista con su correspondiente ubicación.
    En conclusión se obtendrán como resultado:
        La impresión de toda la matriz ingresada
        Los valores de las variables CNP - CNI - SUMA PP - MAX- MIN – PMAX – PMIN
'''
import random

matriz = []

for i in range(0, 50):
    matriz.append([])
    for j in range(0, 50):
        matriz[i].append(random.randint(0, 200))

pares = 0
impares = 0

suma_pares = []
mayor_pares = 0
mayor_coordenadas = [-1, -1]
menor_pares = 201 # Pongo un numero mayor al numero maximo del random para no tener que validar si x=0
menor_coordenadas = [-1, -1]


for x in range(0, 50):
    for y in range(0, 50):
        if matriz[x][y] % 2 == 0:
            pares += 1
        else:
            impares += 1

        if x % 2 == 0 and y % 2 == 0:
            suma_pares.append(matriz[x][y])

            if matriz[x][y] > mayor_pares:
                mayor_pares = matriz[x][y]
                mayor_coordenadas = [x, y]

            if matriz[x][y] < menor_pares:
                menor_pares = matriz[x][y]
                menor_coordenadas = [x, y]


print(f'Hay un total de {pares} numeros pares y {impares} impares')
print(f'La suma de los numeros que se encuentran en posicion par es: {sum(suma_pares)}')
print(f'El mayor de los numeros que se encuentran en posicion par es: {mayor_pares} y en posicion {mayor_coordenadas}')
print(f'El menor de los numeros que se encuentran en posicion par es: {menor_pares} y en posicion {menor_coordenadas}')