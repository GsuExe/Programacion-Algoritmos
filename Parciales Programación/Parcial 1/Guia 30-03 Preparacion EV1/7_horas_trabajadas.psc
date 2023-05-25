Proceso horas_trabajadas
	Definir horas,tarifa,total Como Entero;
	
	Definir opcion Como Caracter;
	
	Definir total_salarios Como Entero;
	
	opcion = ""; 
	total_salarios = 0;
	
	Escribir "Ingrese la tarifa de pago por hora: ";
	Leer tarifa;
	
	Repetir
		
		Escribir "Ingrese la cantidad de horas trabajadas: ";
		Leer horas;
		
		total = 0;
		
		Si horas > 40 Entonces
			total = 40 * tarifa;
			total = total + (horas - 40) * (tarifa + (tarifa * 0.5));
			Escribir "Su salario corresponde a: $",total;
		Sino
			total = 40 * tarifa; 
			Escribir "Su salario corresponde a $",total;
		FinSi
		
		total_salarios = total_salarios + total; 
		
		Escribir ""; 
		Escribir "¿Desea calcular el salario de otro trabajador?";
		Escribir "SI/NO";
		leer opcion;
		Escribir ""; 
		
		
	Hasta Que opcion == "NO"; 
	
	Escribir ""; 
	Escribir "La suma de los salarios de los trabajadores es de: $", total_salarios; 
	
	
	
FinProceso
