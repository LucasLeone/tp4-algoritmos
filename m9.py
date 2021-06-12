'''
    Se dispone de una matriz N elementos. Se desea diseñar un algoritmo que permita
    insertar el valor de X e Y en el lugar k-ésimo y Q-ésimo de la mencionada matriz.
'''

matriz = []

for i in range(0, 5):
    matriz.append([])
    for j in range(0, 5):
        matriz[i].append(0)

while True:
    print('---- Nuevo valor ----')
    num = int(input('Ingrese el numero que desea insertar: '))
    x = int(input('Ingrese la fila en donde lo quiere ingresar: '))
    if x > 4 or x < 0:
        print('Fila inexistente')
        break
    y = int(input('Ingrese la columna en donde lo quiere ingresar: '))
    if y > 4 or y < 0:
        print('Columna inexistente')
        break

    matriz[x][y] = num

    continua = input('Desea continuar [S/N]? ')
    continua = continua.lower()
    if continua == 's':
        pass
    elif continua == 'n':
        break
    else:
        print('Opcion incorrecta, se va a continuar')

print(matriz)