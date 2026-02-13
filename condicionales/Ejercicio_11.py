/Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 

ladoA = float(entrada())
ladoB = float(entrada())
ladoC = float(entrada())

lados = ordenado([ladoA, ladoB, ladoC])
a, b, h = lados[0], lados[1], lados[2]

si ronda(a*2 + b2, 2) == ronda(h*2, 2):
    print("Es un triángulo rectángulo")

if ladoA == ladoB == ladoC:
    print("Es un triángulo equilátero")
elif ladoA == ladoB o ladoB == ladoC o ladoA == ladoC:
    print("Es un triángulo isósceles")
De lo contrario:
    print("Es un triángulo escaleno")