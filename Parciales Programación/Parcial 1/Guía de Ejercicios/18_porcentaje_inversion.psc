Proceso porcentaje_inversion
	Definir inv1,inv2,inv3,total Como Entero;
	Definir porcentaje1,porcentaje2,porcentaje3 Como Real;
	
	Escribir "Ingresa la primera inversi�n: ";
	Leer inv1;
	
	Escribir "Ingresa la segunda inversi�n: ";
	Leer inv2;
	
	Escribir "Ingresa la tercera inversi�n: ";
	Leer inv3;
	
	total = inv1 + inv2 + inv3;
	
	porcentaje1 = (100 * inv1) / total;
	porcentaje2 = (100 * inv2) / total;
	porcentaje3 = (100 * inv3) / total;
	
	
	Escribir "El total de la inversi�n es de: $",total;

	Escribir "El porcentaje que invierte la primera persona respecto al total es de: ",porcentaje1,"%";
	Escribir "El porcentaje que invierte la segunda persona respecto al total es de: ",porcentaje2,"%";
	Escribir "El porcentaje que invierte la tercera persona respecto al total es de: ",porcentaje3,"%";
	
FinProceso
