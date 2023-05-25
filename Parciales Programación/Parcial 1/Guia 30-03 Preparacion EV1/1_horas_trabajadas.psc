Proceso horas_trabajadas
	Definir horas,tarifa,total Como Entero;
	
	Escribir "Ingrese la cantidad de horas trabajadas: ";
	Leer horas;
	
	Escribir "Ingrese la tarifa de pago por hora: ";
	Leer tarifa;
	
	total = 0;
	
	Si horas > 40 Entonces
		total = 40 * tarifa;
		total = total + (horas - 40) * (tarifa + (tarifa * 0.5));
		Escribir "Su salario corresponde a: $",total;
	Sino
		total = 40 * tarifa; 
		Escribir "Su salario corresponde a $",total;
	FinSi
	
FinProceso
