#Crea una aplicación que pida un número y calcule su factorial (El factorial de 
#un número es el producto de todos los enteros entre 1 y el propio número y se 
#representa por el número seguido de un signo de exclamación. 

  Leer numero
num = int(input("Introduce un número: "))

 Inicializo variables
contador = 2
resultado = 1

 Mientras contador <= num hacer
while contador <= num:
     resultado = resultado * contador
    resultado = resultado * contador
    
    contador = contador + 1
    contador = contador + 1

# 6. Mostrar resultado
print("El factorial de", num, "es:", resultado)
#fin
//