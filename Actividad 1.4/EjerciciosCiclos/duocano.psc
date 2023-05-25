Proceso duocano
	Definir opcion1 Como Caracter;
	opcion1 = ""; 
	
	Definir opcion2 Como Caracter; 
	opcion2 = "";
	
	
	Definir orden,total Como Entero;
	orden = 0;
	total = 0;
	
	
	Repetir
		
		Escribir "***********************";
		Escribir "a) Realizar Venta";
		Escribir "b) Cerrar Turno";
		Escribir "c) Salir";
		Escribir "***********************";
		Escribir "Ingrese una opción: ";
		Leer opcion1;
		Escribir ""; 
		
		Si Minusculas(opcion1) == "a" o Minusculas(opcion1) == "b" o Minusculas(opcion1) == "c" Entonces
			Si Minusculas(opcion1) == "a" Entonces
				Repetir
					Escribir "MENÚ DUOCANO";
					Escribir "1.- DuocChoripan $1200";
					Escribir "2.- DuocItaliano $1500";
					Escribir "3.- DuocVegano $2000";
					Escribir "4.- Salir";
					Escribir "Ingrese una opción: ";
					Leer opcion2;
					Escribir "";
					
					Si opcion2 == "1" o opcion2 == "2" o opcion2 == "3" o opcion2 == "4" Entonces
						Si opcion2 == "1" Entonces
							orden = orden + 1200;
							Escribir "Has vendido un DuocChoripan";
							Escribir ""; 
							total = total + 1200; 
						FinSi
						
						Si opcion2 == "2" Entonces
							orden = orden + 1500; 
							Escribir "Has vendido un DuocItaliano";
							Escribir ""; 
							total = total + 1500; 
						FinSi
						
						Si opcion2 == "3" Entonces
							orden = orden + 2000;
							Escribir "Has vendido un DuocVegano"; 
							Escribir ""; 
							total = total + 2000;
						FinSi
						
						Si opcion2 == "4" Entonces
							Escribir "¡¡ORDEN LISTA!!";
							Escribir "Total a pagar: $",orden; 
							Escribir ""; 
							orden = 0; 
						FinSi
					SiNo
						Escribir "OPCIÓN NO VÁLIDA, INGRESE NUEVAMENTE";
						Escribir ""; 
					FinSi
					
					
					
				Hasta Que opcion2 == "4" 
				
			FinSi
			
			Si Minusculas(opcion1) == "b" Entonces
				Escribir "CIERRE DE TURNO";
				Escribir "Recaudación del turno: $",total;
				Escribir "";
				Escribir "¡¡Comienza un nuevo turno!!";
				Escribir ""; 
				total = 0;
			FinSi
			
		SiNo
			Escribir "OPCIÓN NO VÁLIDA, INGRESE NUEVAMENTE"; 
			Escribir ""; 
		FinSi
		
		
		
		
		
	Hasta Que Minusculas(opcion1) == "c" 
	
FinProceso
