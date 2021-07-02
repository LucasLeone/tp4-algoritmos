'''
    Se dispone de una matriz de 12x7 elementos, donde las columnas representan días
    de las semanas y las filas los meses del año, cada celda contiene el ingreso de ventas
    que obtuvo el comercio según el día y mes especificado.
        Se pide la siguiente información:
            - Calcular el total de ventas.
            - Calcular las ventas por meses. 
'''
import random

matriz = []

for i in range(0, 12):
    matriz.append([])
    for j in range(0, 7):
        matriz[i].append(random.randint(0, 10))

suma_ventas = 0

for fila in range(0, 12):
    for columna in range(0, 7):
        suma_ventas += matriz[fila][columna]

vector_meses = []

for mes in range(0, 12):
    venta_mes = 0
    for dia in range(0, 7):
        venta_mes += matriz[mes][dia]
    vector_meses.append(venta_mes)

print(f'El total de ventas es: {suma_ventas}')
print('Las ventas por meses son:')
print(f'Enero: {vector_meses[0]}')
print(f'Febrero: {vector_meses[1]}')
print(f'Marzo: {vector_meses[2]}')
print(f'Abril: {vector_meses[3]}')
print(f'Mayo: {vector_meses[4]}')
print(f'Junio: {vector_meses[5]}')
print(f'Julio: {vector_meses[6]}')
print(f'Agosto: {vector_meses[7]}')
print(f'Septiembre: {vector_meses[8]}')
print(f'Octubre: {vector_meses[9]}')
print(f'Noviembre: {vector_meses[10]}')
print(f'Diciembre: {vector_meses[11]}')