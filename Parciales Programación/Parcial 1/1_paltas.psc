Proceso paltas
	Definir cant_cajones,primera_categoria,segunda_categoria,total,cuota Como Entero;
	Definir opcion Como Entero;
	
	Escribir "**********************************";
	Escribir "COMPRA DE PALTAS";
	Escribir "**********************************";
	Escribir "";
	
	primera_categoria = 15000;
	segunda_categoria = 7500;
	total = 0;
	
	Repetir 
		Escribir "¿Cuántos cajones de palta desea comprar?";
		Leer cant_cajones;
		Escribir "";
		
		Si cant_cajones < 0 Entonces
			Escribir "Cantidad de cajones ingresados no válidos, ingrese nuevamente";
			Escribir "";
		FinSi
	Hasta Que cant_cajones >= 0 
	
	Repetir
		Escribir "Porfavor, elegir una categoría: ";
		Escribir "1) Primera Categoría";
		Escribir "2) Segunda Categoría";
		Leer opcion;
		Escribir "";
		
		Si opcion <> 1 y opcion <> 2 Entonces
			Escribir "Opción no válida, ingrese nuevamente";
			Escribir "";
		FinSi
	Hasta Que opcion == 1 o opcion ==2 
	
	Si opcion == 1 Entonces
		total = total + (cant_cajones * primera_categoria);
	SiNo
		Si opcion == 2 Entonces
			total = total + (cant_cajones * segunda_categoria);
		FinSi
	FinSi
	
	Repetir
		Escribir "¿En cuántos días desea pagar la factura?";
		Leer cuota;
		
		Si cuota < 0 Entonces
			Escribir "Cuota ingresada no válida, ingrese nuevamente";
		FinSi

	Hasta Que cuota >= 1
	
	Si cuota > 90 Entonces
		total = total + (total * 0.20);
	FinSi
	
	Escribir "";
	Escribir "Total a pagar es de: $",total;
	
FinProceso