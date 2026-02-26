#Una empresa tiene el registro de las horas que trabaja diariamente un empleado 
#durante la semana (seis días) y requiere determinar el total de éstas, así como 
#el sueldo que recibirá por las horas trabajadas.

	horas_acum = 0;
	sueldo_por_hora =
	float(input("Introduce el sueldo por hora:"))

	
	for dia in range (1, 6):
		print("¿Cuántas horas has trabajado el día ",dia,"?:",end =")
	    horas=int(input()
		horas_acum <- horas_acum + horas;
	
	print(f"Horas acumuladas en la semana:,{horas_acum}")
	print(f"Sueldo:{sueldo_por_hora*horas_acum}")
	#Fin