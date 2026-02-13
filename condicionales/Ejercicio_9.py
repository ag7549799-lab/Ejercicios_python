 /Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
num1,num2,num3   

num1=int(input("Dime el numero 1: ")
num2=int(input("Dime el numero 2: ")
num3=int(input("Dime el numero 3: ")

numeros=[num1,num2,num3]
numeros.sort(reverse=True)

print(numeros[0],numeros[1],numeros[2])
