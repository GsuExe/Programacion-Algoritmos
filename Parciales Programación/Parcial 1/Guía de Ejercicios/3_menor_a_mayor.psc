Proceso menor_a_mayor
	Definir num1, num2, num3 Como Entero;
	
	Escribir "Ingrese el primer número: ";
	Leer num1;
	
	Escribir "Ingrese el segundo número: ";
	Leer num2;
	
	Escribir "Ingrese el tercer número: ";
	Leer num3;
	
	Si num1 > 0 y num2 > 0 y num3 > 0 Entonces
		Si num1 > num2 y num1 > num3 Entonces
			Si num2 > num3 Entonces
				Escribir "Orden números ingresados: ";
				Escribir num3," - ",num2," - ",num1;
			SiNo
				Escribir "Orden números ingresados: ";
				Escribir num2," - ",num3," - ",num1;
			FinSi
		FinSi
		
		Si num2 > num1 y num2 > num3 Entonces
			Si num1 > num3 Entonces
				Escribir "Orden números ingresados: ";
				Escribir num3," - ",num1," - ",num2;
			SiNo
				Escribir "Orden números ingresados: ";
				Escribir num1," - ",num3," - ",num2;
			FinSi
		FinSi
		
		Si num3 > num1 y num3 > num2 Entonces
			Si num1 > num2 Entonces
				Escribir "Orden números ingresados: ";
				Escribir num2," - ",num1," - ",num3;
			SiNo
				Escribir "Orden números ingresados: ";
				Escribir num1," - ",num2," - ",num3;
			FinSi
		FinSi
	SiNo
		Escribir "Alguno de los números ingresados NO es un entero positivo";
	FinSi
	
FinProceso
