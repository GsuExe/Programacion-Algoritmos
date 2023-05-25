Proceso credito_bancario
	Definir nombre,rut,nacionalidad,morosidad Como Caracter;
	Definir credito,cuota,edad,sueldo,antiguedad Como Entero;
	
	Escribir "Ingrese su nombre y apellido: ";
	Leer nombre;
	
	Escribir "Ingrese su RUT (Con puntos y guión): ";
	Leer rut;
	
	Escribir "Ingrese su edad: ";
	Leer edad;
	
	Escribir "¿Posee nacionalidad chilena? (SI o NO): ";
	Leer nacionalidad; 
	
	Escribir "¿Presenta alguna deuda previa y/o vencida? (SI o NO): ";
	Leer morosidad;
	
	Escribir "Ingrese en años el tiempo que lleva ejerciendo un trabajo: ";
	Leer antiguedad;
	
	Escribir "Ingrese su sueldo: ";
	Leer sueldo;
	
	Escribir "Ingrese el monto solicitado: ";
	Leer credito;
	
	Escribir "Ingrese la cantidad de cuotas en que desea pagar el monto solicitado (de 3 a 84 cuotas): ";
	Leer cuota;
	
	Si edad >= 24 y edad <= 79 y mayusculas(nacionalidad) == "SI" y mayusculas(morosidad) == "NO" y antiguedad >= 3 y sueldo >= 250000 y credito >= 500000 y cuota >= 3 y cuota <= 84 Entonces
		Escribir "Sexo";
	SiNo
		Escribir "-------------------------------------------";
		Escribir mayusculas(nombre),"   ", rut;
		Escribir "-------------------------------------------";
		Escribir "No cumple con los requisitos";
	FinSi
	
FinProceso

