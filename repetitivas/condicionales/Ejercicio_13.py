/Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
(mes >= 1 Y mes <= 12) 
   1, 3, 5, 7, 8, 10, 12: ddm <- 31;
   4, 6, 9, 11: ddm <- 30;
   2:
   Si (year % 4 = 0 Y NO (year % 100 = 0)) O year % 400 = 0 Entonces
   ddm <- 29;
   ddm <- 28;
   (dia >= 1 Y dia <= ddm) 
   Escribir "Correcta";
   Escribir "Incorrecta";
