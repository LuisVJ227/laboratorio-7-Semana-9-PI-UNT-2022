print("Ingrese el número de filas y columnas de la Matriz A:")
filasA, columnasA = int(input()), int(input())

print("Ingrese el número de filas y columnas de la Matriz B")
filasB, columnasB = int(input()), int(input())

# Se verifica si es posible o no hacer la operación
if columnasA == filasB:
    # Crear la matriz A con el tamaño filasA * columnasA
    matrizA = []
    for i in range(filasA):
        matrizA.append([0] * columnasA)
    # Crear la matriz B con el tamaño filasB * columnasB
    matrizB = []
    for i in range(filasB):
        matrizB.append([0] * columnasB)

    # Colocar los componentes de la Matriz A
    print("Ingrece la Matriz A:")
    for filas in range(filasA):
        for columnas in range(columnasA):
            matrizA[filas][columnas] = float(input(f"Ingresa la posición número {filas+1},{columnas+1} de la Matriz A -> "))

    # Colocar los componentes de la Matriz A
    print("Ingrese la Matriz B:")
    for filas in range(filasB):
        for columnas in range(columnasB):
            matrizB[filas][columnas] = float(input(f"Ingresa la posición número {filas+1},{columnas+1} de la Matriz B -> "))

    # Crear la matriz resultante de tamaño filasA * columnasB
    matrizC = []
    for i in range(filasA):
        matrizC.append([0] * columnasB)

    # Multiplicación entre las matrices A y B
    for i in range(filasA):
        for j in range(columnasB):
            for k in range(filasB):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

    print("La matriz resultante es: ")
    for i in matrizC:
        print(i)

else:
    print('No se puede efectuar la multiplicación')