# Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

tabla = int(input())

for num in range(1, 11):
resultado=num *tabla 
    print(num, "", tabla, "=", num * tabla)