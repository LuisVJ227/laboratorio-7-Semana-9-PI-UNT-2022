# Definimos la función

def EsPalisandro(Number):
    a = 0
    b = len(Number) - 1
    for i in range(0, len(Number)):
        if Number[a] == Number[b]:
            a = a+1
            b = b-1
        else:
            return False
    return True

# Pedimos un numero al usuario

Numero = int(input("Ingrese un número: "))

# Convertimos el número en "String"

Numero = str(Numero)

if EsPalisandro(Numero):
    print(EsPalisandro(Numero),f". El número {Numero} es un palisandro")
else:
    print(EsPalisandro(Numero),f". El número {Numero} no es un palisandro")