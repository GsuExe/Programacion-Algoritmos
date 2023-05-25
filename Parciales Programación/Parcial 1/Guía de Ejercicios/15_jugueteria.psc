Proceso jugueteria
	definir payasos,munecas,peso_total,costo_envio Como Entero;
	definir zona Como Caracter;
	
	Escribir "Ingrese cantidad de payasos vendidos: ";
	Leer payasos;
	
	Escribir "Ingrese cantidad de muñecas vendidas: ";
	Leer munecas;
	
	Escribir "Ingrese la zona de destino del paquete (Norte, Centro o Sur): ";
	Leer zona;
	
	peso_total = (payasos * 300) + (munecas * 450);
	
	Si peso_total < 1000 Entonces
		Si Mayusculas(zona) == "NORTE" Entonces
			costo_envio = 3000;
		FinSi
		Si Mayusculas(zona) == "CENTRO" Entonces
			costo_envio = 2000;
		FinSi
		Si Mayusculas(zona) == "SUR" Entonces
			costo_envio = 4000;
		FinSi
	FinSi
	
	
	Si peso_total >= 1000 Entonces
		Si Mayusculas(zona) == "NORTE" Entonces
			costo_envio = 5000;
		FinSi
		Si Mayusculas(zona) == "CENTRO" Entonces
			costo_envio = 3000;
		FinSi
		Si Mayusculas(zona) == "SUR" Entonces
			costo_envio = 7000;
		FinSi
	FinSi
	
	Escribir "El peso total del paquete es de ",peso_total/1000," kg y tiene un costo de envio de $",costo_envio;
	
	
	
FinProceso
