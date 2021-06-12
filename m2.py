'''
    Rellenar una matriz de identidad de 4 por 4.
'''

matriz = []

for i in range(0, 4):
    matriz.append([])
    for j in range(0, 4):
        matriz[i].append(0)

matriz[0][0] = 1
matriz[1][1] = 1
matriz[2][2] = 1
matriz[3][3] = 1

print(matriz)