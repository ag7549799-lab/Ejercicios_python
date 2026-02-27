#Algoritmo para determinar cuánto ahorrará una persona en un año, 
#si al final de cada mes deposita cantidades variables de dinero; 
#además, se quiere saber cuánto lleva ahorrado cada mes.

ahorro_acum = 0

for mes in range(1, 12):
    print(f"¿Cuánto has ahorrado en el mes {mes}?:", end="")
    cant_mensual = float(input())
    ahorro_acum = ahorro_acum + cant_mensual
    print(f"En el mes {mes} llevas ahorrado {ahorro_acum}")
    #Fin 