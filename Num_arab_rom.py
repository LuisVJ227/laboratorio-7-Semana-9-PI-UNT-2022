print("CONVERTIR NÚMEROS ARÁBIGOS A NÚMEROS ROMANOS")
print("---------------------------------")

numero = int(input("Ingrese el número en arábigo: "))

if 0 < numero < 4000:
    def printRoman(numero):
        arab = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
        rom = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12

        while 0 < numero < 4000:
            div = numero // arab[i]
            numero %= arab[i]

            while div:
                print(rom[i], end = "")
                div -= 1
            i -= 1     
      
    if __name__ == "__main__":
        print("El número en romano es:", end = " ")
        printRoman(numero)

else:
    print("Este conversor admite números mayores a 0 y menores a 4000")
