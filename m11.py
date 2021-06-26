'''
    Los resultados de las últimas elecciones al gobierno en el pueblo X han sido las siguientes:
        Distrito    Candidato   Candidato   Candidato   Candidato
                        A           B           C           D
          12.1         194         48          206         45
          13.2         180         20          320         16
          14.3         221         90          140         20
          15.4         432         50          821         14
          16.5         820         61          946         18
    Escribir un programa que haga las siguientes tareas:
         Imprimir la tabla anterior con cabeceras incluidas.
         Calcular e imprimir el número total de votos recibidos por cada candidato y el
        porcentaje total de votos emitidos. Asimismo visualizar el candidato más votado.
         Si algún candidato recibe más del 50 por 100 de los datos, el programa imprimirá
        un mensaje declarándolo ganador.
         Si ningún candidato recibe más de 50 por 100 de los datos, el programa debe
        imprimir el nombre de los dos candidatos más votados, que serán los que pasen a
        la segunda ronda de las elecciones
'''

matriz = [['Distrito', 'Candidato', 'Candidato', 'Candidato', 'Candidato'],
          [' ', 'A', 'B', 'C', 'D'],
          [12.1, 194, 48, 206, 45],
          [13.2, 180, 20, 320, 16],
          [14.3, 221, 90, 140, 20],
          [15.4, 432, 50, 821, 13],
          [16.5, 820, 61, 946, 18]]

print(matriz)

x = 2
y = 1
candidato_a = 0
candidato_b = 0
candidato_c = 0
candidato_d = 0
for x in range(2, len(matriz)):
    if y == 1:
        candidato_a += matriz[x][y]

y += 1

for x in range(3, len(matriz)):
    if y == 2:
        candidato_b += matriz[x][y]

y += 1

for x in range(4, len(matriz)):
    if y == 3:
        candidato_c += matriz[x][y]

y += 1

for x in range(5, len(matriz)):
    if y == 4:
        candidato_d += matriz[x][y]

total = candidato_a + candidato_b + candidato_c + candidato_d

print(candidato_a)

porcentaje_a = (candidato_a * 100) / total
porcentaje_b = (candidato_b * 100) / total
porcentaje_c = (candidato_c * 100) / total
porcentaje_d = (candidato_d * 100) / total

print(f'Los porcentajes de votos de cada candidatos son: A = {porcentaje_a}%, B = {porcentaje_b}, C = {porcentaje_c}%, D = {porcentaje_d}')

if candidato_a > candidato_b and candidato_a > candidato_c and candidato_a > candidato_d:
    print(f'El candidato mas votado fue el candidato A con {candidato_a}')
elif candidato_b > candidato_a and candidato_b > candidato_c and candidato_b > candidato_d:
    print(f'El candidato mas votado fue el candidato B con {candidato_b}')
elif candidato_c > candidato_a and candidato_c > candidato_b and candidato_c > candidato_d:
    print(f'El candidato mas votado fue el candidato C con {candidato_c}')
elif candidato_d > candidato_a and candidato_d > candidato_b and candidato_d > candidato_c:
    print(f'El candidato mas votado fue el candidato B con {candidato_b}')

if porcentaje_a > 50:
    print('El ganador fue el A!!!')
elif porcentaje_b > 50:
    print('El ganador fue el B!!!')
elif porcentaje_c > 50:
    print('El ganador fue el C!!!')
elif porcentaje_d > 50:
    print('El ganador fue el D!!!')
else:
    print('No gano nadie!')
    

candidatos_vector = [candidato_a, candidato_b, candidato_c, candidato_d]
candidatos_mayores = [candidatos_vector[2], candidatos_vector[3]]

for i in range(1, len(candidatos_vector)):
    for j in range(0, len(candidatos_vector) - i):
        if (candidatos_vector[j + 1] < candidatos_vector[j]):
            aux = candidatos_vector[j]
            candidatos_vector[j] = candidatos_vector[j+1]
            candidatos_vector[j+1] = aux

print('Pasan a la siguientes fases los siguientes candidatos:')
if candidatos_vector[2] == candidato_a:
    print('Candidato A')

if candidatos_vector[2] == candidato_b:
    print('Candidato B')

if candidatos_vector[2] == candidato_c:
    print('Candidato C')

if candidatos_vector[2] == candidato_d:
    print('Candidato D')

if candidatos_vector[3] == candidato_a:
    print('Candidato A')

if candidatos_vector[3] == candidato_b:
    print('Candidato B')

if candidatos_vector[3] == candidato_c:
    print('Candidato C')

if candidatos_vector[3] == candidato_d:
    print('Candidato D')