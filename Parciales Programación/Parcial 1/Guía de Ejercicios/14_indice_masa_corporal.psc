Proceso indice_masa_corporal
	Definir peso,estatura,imc Como Real;
	
	Escribir "Ingrese su peso (en kg.): ";
	Leer peso;
	
	Escribir "Ingrese su estatura (en metros): ";
	Leer estatura;
	
	imc = peso/(estatura * estatura);
	
	Escribir "Tu �ndice de masa corporal es: ",imc;
	
FinProceso
