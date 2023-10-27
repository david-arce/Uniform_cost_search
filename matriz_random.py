import random

def llenar_matriz(matriz, numero, cantGatos, cantAmos, cantObstaculos, muriel, coraje):
    rows, cols = len(matriz), len(matriz[0])
    posiciones = set()  # Utilizamos un conjunto para evitar posiciones repetidas
    
    while cantGatos > 0:
        fila = random.randint(0, rows - 1)
        columna = random.randint(0, cols - 1)
        
        # Verifica si la posición ya ha sido ocupada
        if (fila, columna) not in posiciones:
            matriz[fila][columna] = numero[0]
            posiciones.add((fila, columna))
            cantGatos -= 1
    while cantAmos > 0:
        fila = random.randint(0, rows - 1)
        columna = random.randint(0, cols - 1)
        
        # Verifica si la posición ya ha sido ocupada
        if (fila, columna) not in posiciones:
            matriz[fila][columna] = numero[1]
            posiciones.add((fila, columna))
            cantAmos -= 1
    while cantObstaculos > 0:
        fila = random.randint(0, rows - 1)
        columna = random.randint(0, cols - 1)
        
        # Verifica si la posición ya ha sido ocupada
        if (fila, columna) not in posiciones:
            matriz[fila][columna] = numero[2]
            posiciones.add((fila, columna))
            cantObstaculos -= 1
    while muriel > 0:
        fila = random.randint(0, rows - 1)
        columna = random.randint(0, cols - 1)
        
        # Verifica si la posición ya ha sido ocupada
        if (fila, columna) not in posiciones:
            matriz[fila][columna] = numero[3]
            posiciones.add((fila, columna))
            muriel -= 1
    while coraje > 0:
        fila = random.randint(0, rows - 1)
        columna = random.randint(0, cols - 1)
        
        # Verifica si la posición ya ha sido ocupada
        if (fila, columna) not in posiciones:
            matriz[fila][columna] = numero[4]
            posiciones.add((fila, columna))
            coraje -= 1
    return matriz
        

# # Tamaño de la matriz
# filas = 5
# columnas = 8

# # Número a colocar en posiciones aleatorias
# numero = [3, -2, 0, 4]

# # Cantidad de veces que se debe colocar el número
# cantGatos = 2
# cantAmos = 3
# cantObstaculos = 11
# cantMuriel = 1

# # Inicializar una matriz con ceros
# matriz = [[1] * columnas for _ in range(filas)]

# # Llena la matriz con el número en posiciones aleatorias
# matriz_aleatoria = llenar_matriz(matriz, numero, cantGatos, cantAmos, cantObstaculos, cantMuriel)

# # Imprime la matriz resultante
# for fila in matriz:
#     print(fila)

        
