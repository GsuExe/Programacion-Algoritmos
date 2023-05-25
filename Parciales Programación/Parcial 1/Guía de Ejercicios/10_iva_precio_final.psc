Proceso iva_precio_final
	//10.Mostrar el precio del IVA de un producto y su precio final.
	Definir neto, impuesto Como Entero;
	Definir IVA Como Real;
	IVA=0.19;
	Escribir "Ingrese el valor: $";
	Leer neto;
	impuesto=neto*IVA;
	Escribir "Neto: $", neto;
	Escribir "IVA: $", impuesto;
	Escribir "Total: $",(neto+impuesto);
FinProceso
