Proceso masculino_femenino
	Definir nombre,edad,genero,num Como Caracter;
	
	Escribir "Ingrese su nombre: ";
	Leer nombre;
	
	Escribir "Ingrese su edad: ";
	Leer edad;
	
	Escribir "Ingrese su genero (Masculino o Femenino): ";
	Leer genero;
	
	Escribir "Ingrese su número de celular: ";
	Leer num;
	
	Si genero == "Masculino" o MAYUSCULAS(genero) == "M" Entonces
		Escribir "Nombre: ",nombre;
		Escribir "Edad: ",edad;
	FinSi
	
	Si genero == "Femenino" o Mayusculas(genero) == "F" Entonces
		Escribir "Nombre: ",nombre;
		Escribir "Número de celular: ",num;
	FinSi
	
FinProceso
