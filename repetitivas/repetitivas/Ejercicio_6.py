#Algoritmo que imprima todos los números pares entre dos números que 
#se le pidan al usuario.

num1 = int(input())
num2 = int(input())

if num1 % 2 != 0:
    num1 = num1 + 1

for num in range(num1, num2, + 1, 2):
    print(num, end = " ")
    #fin