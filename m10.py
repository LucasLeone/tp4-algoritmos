'''
    Una agencia de venta de vehículos automóviles distribuye quince modelos diferentes y
    tiene en su plantilla diez vendedores. Se desea un programa que escriba un informe
    mensual de las ventas por vendedor y modelos, así como el número de automóviles
    vendido por cada vendedor y el número total de cada modelo vendido por todos los
    vendedores. Asimismo para entregar el premio al mejor vendedor, necesita saber cual
    es el vendedor que más coches ha vendido.
'''
import random

matriz = []

for i in range(0, 10):
    matriz.append([])
    for j in range(0, 15):
        matriz[i].append(random.randint(0, 5))

print('Cada fila correspone a las ventas de cada vendedor, cada columna corresponde al modelo del auto vendido')

x = 1
for fila in matriz:
    print(f'El vendedor {x} vendio {sum(fila)} autos.')
    print('     Los modelos vendidos fueron: ')
    print('         ', fila)
    print(' ')
    x += 1

for a in range(0, 10):
    suma_modelo = 0
    
    for b in range(0, 15):
        suma_modelo += matriz[a][b]
    
    print(f'Las ventas del modelo {a + 1} son: {suma_modelo}')

mayor_vendedor = 0
y = 0
for fila in matriz:
    suma_fila = sum(fila)
    if suma_fila > mayor_vendedor:
        mayor_vendedor = suma_fila
        y = matriz.index(fila)

print(' ')
print(f'El mayor vendedor fue {y + 1} vendiendo un total de {mayor_vendedor} autos')
print(' ')