Proceso tabla_multiplicar
	Definir num Como Entero;
	
	Escribir "Ingrese un número: ";
	Leer num;
	
	Si num > 0 Entonces
		Escribir "Tabla de multiplicar del número ",num;
		Escribir num, " * ","1 = ",num*1;
		Escribir num, " * ","2 = ",num*2;
		Escribir num, " * ","3 = ",num*3;
		Escribir num, " * ","4 = ",num*4;
		Escribir num, " * ","5 = ",num*5;
	SiNo
		Escribir "El número ingresado NO es un entero positivo";
	FinSi
	
FinProceso
