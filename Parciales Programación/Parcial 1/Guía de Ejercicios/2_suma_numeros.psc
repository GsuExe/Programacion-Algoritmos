Proceso suma_numeros
	Definir num1, num2 Como Entero;
	
	Escribir "Ingrese el primer n�mero: ";
	Leer num1;
	
	Escribir "Ingrese el segundo n�mero: ";
	Leer num2;
	
	Si num1 > 0 y num2 > 0 Entonces
		Escribir "La suma de los n�meros ingresados es: ",num1 + num2;
	SiNo
		Escribir "Alguno de los n�meros ingresados NO es un entero positivo";
	FinSi

FinProceso
