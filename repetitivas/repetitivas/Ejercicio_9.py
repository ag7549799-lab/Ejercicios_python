# Algoritmo que dados dos números, uno real (base) y un entero positivo (exponente),
# saque por pantalla el resultado de la potencia sin utilizar el operador de potencia.

base = float(input())

while True:
    exponente = int(input())
    if exponente >= 0:
        break

potencia = 1

for i in range(1, exponente + 1):
    potencia = potencia * base

print(potencia)