Proceso operaciones_dos_enteros
	Definir num1,num2 Como Entero;
	
	Escribir "Ingrese el primer n�mero: ";
	Leer num1;
	
	Escribir "Ingrese el segundo n�mero: ";
	Leer num2;
	
	Si num1 mod num2 == 0 Entonces
		Escribir "El n�mero ",num1," es divisible por el n�mero ",num2;
	SiNo
		Escribir "El n�mero ",num1," NO es divisible por el n�mero ",num2;
	FinSi
	
	Si num2 mod num1 == 0 Entonces
		Escribir "El n�mero ",num2," es divisible por el n�mero ",num1;
	SiNo
		Escribir "El n�mero ",num2," NO es divisible por el n�mero ",num1;
	FinSi
	
	Si num1 > num2 Entonces
		Escribir "El n�mero ",num1," es mayor";
	FinSi
	
	Si num2 > num1 Entonces
		Escribir "El n�mero ",num2," es mayor";
	FinSi
	
	Si num1 == num2 Entonces
		Escribir "Los n�meros ingresados son iguales";
	FinSi
	
	Si num1 mod 2 <> 0 y num2 mod 2 <> 0 Entonces
		Escribir "Los n�meros ingresados son impares";
	SiNo
		Escribir "Los n�meros ingresados NO son impares";
	FinSi
	
	
	
	
	
FinProceso
