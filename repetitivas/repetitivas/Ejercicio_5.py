#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.

while True:
	car =input()

	if len(car) == 1:
		if car == " ":
			break

    if car.upper() in "AEIOU":
    	print("VOCAL")
    else:
    	print("NO VOCAL")
    	#fin