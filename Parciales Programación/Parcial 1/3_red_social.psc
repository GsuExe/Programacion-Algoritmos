Proceso red_social
	Definir red, edad, pareja, contador Como Entero;
	Definir cont_ig, cont_tiktok,cont_solteros Como Entero;
	Definir promedio_edad Como Entero;
	
	
	Escribir "************************";
	Escribir "ENCUESTA RED SOCIAL PREFERIDA";
	Escribir "************************";
	Escribir "";
	
	cont_ig = 0;
	cont_tiktok = 0;
	cont_solteros = 0;
	promedio_edad = 0;
	
	
	Para contador <- 1 Hasta 50 Hacer
		
		Repetir
			Escribir "Porfavor, escoger su red social preferida: ";
			Escribir "1) Instagram";
			Escribir "2) Tiktok";
			Leer red;
			
			Si red <> 1 y red <> 2 Entonces
				Escribir "Opción ingresada no válida";
				Escribir "";
			FinSi
			
		Hasta Que red == 1 o red == 2;
		
		
		
		Si red == 1 Entonces
			cont_ig = cont_ig + 1;
		SiNo
			Si red == 2 Entonces
				cont_tiktok = cont_tiktok + 1;
			FinSi
		FinSi
		
		
		Repetir
			Escribir "";
			Escribir "Porfavor, ingrese su edad: ";
			Leer edad;
			
			Si edad < 12 o edad > 18 Entonces
				Escribir "Edad ingresada NO está entre los 12 y 18 años";
				Escribir "";

			FinSi
			
		Hasta Que edad >= 12 y edad <= 18;
		
		promedio_edad = promedio_edad + edad;
		
		
		
		Repetir
			Escribir "";
			Escribir "¿Usted tiene pareja?";
			Escribir "1) SI";
			Escribir "2) NO";
			Leer pareja;
			
			Si pareja <> 1 y pareja <> 2 Entonces
				Escribir "Opción ingresada no válida";
			FinSi
			
		Hasta Que pareja == 1 o pareja == 2;  
		
		
		Si pareja == 2 y red == 1 Entonces
			cont_solteros = cont_solteros + 1;
		FinSi
		
		
		Escribir "";
		Escribir "¡¡¡PERSONA ENCUESTADA CORRECTAMENTE!!!";
		Escribir "";
		
		
	FinPara
	
	Escribir "--------------------------";
	Escribir "¡¡¡PROCESO FINALIZADO!!!";
	Escribir "--------------------------";
	Escribir "";
	
	Escribir "Resultados: ";
	
	Si cont_ig > cont_tiktok Entonces
		Escribir "Red Social más utilizada: Instagram";
	SiNo
		Si cont_ig < cont_tiktok Entonces
			Escribir "Red Social más utilizada: TikTok";
		Sino
			Escribir "Red Social más utilizada: Empate entre ambas";
		FinSi
	FinSi
	
	Escribir "Promedio de edad de usuarios de Instagram y TikTok: ",promedio_edad/50," años";
	Escribir "Cantidad de jóvenes que utilizan Instagram y además, estan solteros: ",cont_solteros;
	
	
	
FinProceso
