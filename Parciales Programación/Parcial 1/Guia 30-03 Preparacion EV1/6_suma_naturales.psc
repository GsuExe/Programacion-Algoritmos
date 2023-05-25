Proceso suma_naturales
	Definir cant_numero,contador,suma Como Entero;
	
	Escribir "Ingrese cantidad de primeros números naturales: ";
	Leer cant_numero;
	
	suma = 0;
	
	Para contador = 1 Hasta cant_numero Hacer
		suma = suma + contador;
	FinPara
	
	Escribir "La suma de los ",cant_numero," primeros números naturales es: ",suma;
	
	
FinProceso
