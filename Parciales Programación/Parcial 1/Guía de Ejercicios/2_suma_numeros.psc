Proceso suma_numeros
	Definir num1, num2 Como Entero;
	
	Escribir "Ingrese el primer número: ";
	Leer num1;
	
	Escribir "Ingrese el segundo número: ";
	Leer num2;
	
	Si num1 > 0 y num2 > 0 Entonces
		Escribir "La suma de los números ingresados es: ",num1 + num2;
	SiNo
		Escribir "Alguno de los números ingresados NO es un entero positivo";
	FinSi

FinProceso
