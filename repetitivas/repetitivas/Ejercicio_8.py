# Programa que pida el limite inferior y superior de un intervalo.
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# Se introducen números hasta que sea 0 y da sumas, conteos y avisos de límites.

suma_dentro_intervalo = 0
cont_fuera_intervalo = 0
igual_limites = False

while True:
    lim_inf = int(input())
    lim_sup = int(input())
    if lim_inf < lim_sup:
        break

while True:
    num = int(input())
    
    if num == 0:
        break
    
    if num > lim_inf and num < lim_sup:
        suma_dentro_intervalo = suma_dentro_intervalo + num
    else:
        if num == lim_inf or num == lim_sup:
            igual_limites = True
        cont_fuera_intervalo = cont_fuera_intervalo + 1

print(suma_dentro_intervalo)
print(cont_fuera_intervalo)

if igual_limites:
    print("Has introducido algún número igual a los límites del intervalo")
else:
    print("No has introducido ningún número igual a los límites del intervalo")