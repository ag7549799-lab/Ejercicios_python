#Algoritmo que diga si un número introducido por teclado es o no primo. 
#un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
import math
es_primo =True 
numero_es_primo =int(input("Introduce un numero para comprobar si es primo:"))

if numero_es_primo <= 1:
  es_primo = False
else:
for num in range(2, int(math.sqrt(numero_es_primo)) + 1):
        if numero_es_primo % num == 0:
            es_primo = False
            break

if es_primo:
    print("Es Primo")
else:
    print("No es Primo")