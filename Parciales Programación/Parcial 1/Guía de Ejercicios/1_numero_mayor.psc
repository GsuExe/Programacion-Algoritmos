Proceso numero_mayor
	Definir num1, num2, num3 Como Entero;
	
	Escribir "Ingrese el primer número: ";
	Leer num1;
	
	Escribir "Ingrese el segundo número: ";
	Leer num2;
	
	Escribir "Ingrese el tercer número: ";
	Leer num3;
	
	Si num1 > num2 Entonces
		Si num1 > num3 Entonces
			Escribir "El primer número ingresado es mayor: ",num1;
		Sino 
			Escribir "El tercer número ingresado es mayor: ",num3;
		FinSi
	FinSi
	
	Si num2 > num1 Entonces
		Si num2 > num3 Entonces
			Escribir "El segundo número ingresado es mayor: ",num2;
		Sino 
			Escribir "El tercer número ingresado es mayor: ",num3;
		FinSi
	FinSi
	
	Si num3 > num1 Entonces
		Si num3 > num2 Entonces
			Escribir "El tercer número ingresado es mayor: ",num3;
		Sino 
			Escribir "El segundo número ingresado es mayor: ",num2;
		FinSi
	FinSi
	
FinProceso
