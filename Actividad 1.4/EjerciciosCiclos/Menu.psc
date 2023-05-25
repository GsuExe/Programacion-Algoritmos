Proceso menu
	Definir opcion Como Entero;
	opcion = 0;
	
	//Variables que se utilizarán con la opción 1
	Definir num1,num2 Como Entero;
	Definir lista Como Caracter; 
	
	//Variable que se utilizará con la opción 2
	Definir nombre Como Caracter; 
	
	//Variable que se utilizará con la opción 3
	Definir fecha Como Entero; 
	
	
	Repetir
		//Menú 
		Escribir "***********************";
		Escribir "1.- Mostrar impares";
		Escribir "2.- Mostrar largo del nombre";
		Escribir "3.- Calcular edad";
		Escribir "4.- SALIR";
		Escribir "***********************";
		Escribir "Ingrese una opción: ";
		Leer opcion;
		Escribir ""; 
		
		Si opcion >= 1 y opcion <= 4 Entonces;
			
			//Escribir impares
			Si opcion == 1 Entonces;
				
				Escribir "Ingrese un rango de números ";
				
				Escribir "Primer número: ";
				leer num1;
				
				Escribir "Último número: ";
				leer num2;
				Escribir ""; 
				
				lista = ""; 
				
				Mientras num1 <= num2 Hacer
					Si num1 mod 2 == 0 Entonces;
						lista = lista + ConvertirATexto(num1) + " - ";
						num1 = num1 + 1;
					FinSi
					
					Si num1 mod 2 <> 0 Entonces;
						lista = lista + ConvertirATexto(num1) + " - ";
						num1 = num1 + 2;
					FinSi
					
				FinMientras
				
				lista = lista + ConvertirATexto(num2);
				Escribir lista;
				Escribir ""; 
				
			FinSi
			
			//Longitud de nombre
			Si opcion == 2 Entonces;
			
				Escribir "Ingrese su nombre: ";
				leer nombre; 
				
				Escribir "Su nombre tiene una cantidad de ",LONGITUD(nombre)," carácteres";
				Escribir ""; 
				
			FinSi
			
			//Calcular edad
			Si opcion == 3 Entonces;
				
				Escribir "Ingrese su año de nacimiento: ";
				Leer fecha;
				
				Si fecha > 1930 Entonces;
					Escribir "En el año 2023 usted va a cumplir ",2023 - fecha," años";
					Escribir ""; 
				SiNo
					Escribir "Fecha ingresada fuera del rango"; 
					Escribir ""; 
					
				FinSi
				
				
		    FinSi
		SiNo
			Escribir "OPCIÓN NO VÁLIDA, INGRESE NUEVAMENTE";
			Escribir ""; 
		FinSi
		
		
	Hasta Que opcion == 4

	
FinProceso
