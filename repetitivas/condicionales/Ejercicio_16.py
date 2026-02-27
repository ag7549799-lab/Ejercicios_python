//Algoritmo para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.
        tiempo<5 
		       coste<-tiempo*100;
		       tiempo<8 
	           coste<-(tiempo-5)*80+500;
	           tiempo<10 
			   coste<-(tiempo-8)*70+240+500;
			   coste<-(tiempo-10)*50+140+240+500;
			
	Si Mayusculas(es_domingo)="S" Entonces
		coste<-coste+coste*0.03;
		Mayusculas(turno)="M" 
			coste<-coste+coste*0.15;
			coste<-coste+coste*0.10;
	 "El coste de la llamada:", coste/100," euros.";