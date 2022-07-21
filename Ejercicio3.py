# Ejercicio 3 de laboratorio 7
import numpy as np
N = int(input("ingrese la cantidad de número: "))
nums = []

for x in range(0,N):
  x = int(input(f'ingrese el número {x+1}: '))
  nums.append(x)
print (nums)

objetivo = int(input('ingrese el número principal: '))
nums=np.array(nums)

print('La posición de los números cuya suma es igual al número principal son: ')
for i in nums:
 for n in nums:
  suma = i + n
  if suma == objetivo:
   resultado1=np.where(nums == i)
   resultado2=np.where(nums == n)
   print(resultado1, resultado2)


