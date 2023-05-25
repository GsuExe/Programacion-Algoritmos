Proceso descuento_monto
	Definir monto Como Entero;
	
	Escribir "Ingrese un monto: ";
	Leer monto;
	
	Si monto > 100 Entonces
		Escribir "El descuento del 10% equivale a: $",monto * 0.10;
		Escribir "El nuevo monto es de: $",monto - (monto * 0.10);
	SiNo
		Si monto < 100 Entonces
			Escribir "El descuento del 2% equivale a: $",monto * 0.02;
			Escribir "El nuevo monto es de: $",monto - (monto * 0.02);
		FinSi
	FinSi
	
FinProceso
