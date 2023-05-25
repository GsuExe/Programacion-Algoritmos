Proceso descuento_entrada
	Definir edad,entrada Como Entero;

	Escribir "Ingrese su edad: ";
	Leer edad;
	
	entrada = 25000;
	Escribir "Precio normal de la entrada: $",entrada;
	
	Si edad <= 15 Entonces
		Escribir "Después de aplicar el descuento, el precio de la entrada es de: $",entrada-(entrada * 0.05);
	SiNo
		Si edad <= 20 Entonces
			Escribir "Después de aplicar el descuento, el precio de la entrada es de: $",entrada-(entrada * 0.10);
		SiNo
			Si edad <= 50 Entonces
				Escribir "Después de aplicar el descuento, el precio de la entrada es de: $",entrada-(entrada * 0.20);
			SiNo
				Si 50 < edad Entonces
					Escribir "Después de aplicar el descuento, el precio de la entrada es de: $",entrada-(entrada * 0.30);
				FinSi
			FinSi
		FinSi
	FinSi
	
	
FinProceso
