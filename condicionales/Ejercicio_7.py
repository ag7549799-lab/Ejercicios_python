//Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
la base y el exponente. 
	'Dime la base:';
	Escribir 'Dime el exponente:';
	Leer exponente;
	exponente>0 
		'La potencia es ',base^exponente;
		exponente=0 
			'La potencia es 1';
		'La potencia es ',1/(base^abs(exponente));
		
