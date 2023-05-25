Proceso descuento_sueldo
	Definir sueldo Como Entero;
	
	Escribir "Ingrese su sueldo: ";
	Leer sueldo;
	
	Si sueldo <= 1000 Entonces
		Escribir "El descuento corresponde a: $",sueldo * 0.10;
		sueldo = sueldo - (sueldo * 0.10);
		Escribir "Su sueldo corresponde a: $",sueldo;
	SiNo
		Si sueldo > 1000 y sueldo <= 2000 Entonces
			Escribir "El adicional corresponde a: $",sueldo * 0.05;
			sueldo = sueldo + (sueldo * 0.05);
			Escribir "Su sueldo corresponde a: $",sueldo;
		SiNo
			Si sueldo > 2000 Entonces
				Escribir "El adicional corresponde a: $",sueldo * 0.03;
				sueldo = sueldo + (sueldo * 0.03);
				Escribir "Su sueldo corresponde a: $",sueldo;
			FinSi
		FinSi
	FinSi
	
FinProceso
