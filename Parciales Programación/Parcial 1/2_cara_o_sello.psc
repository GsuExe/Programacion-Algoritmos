Proceso cara_o_sello
	Definir opcion,oportunidad,azar1,suma_puntos Como Entero;
	
	Escribir "**********************************";
	Escribir "¡¡¡JUEGO DE CARA O SELLO!!!";
	Escribir "**********************************";
	
	oportunidad = 1;
	suma_puntos = 0;
	
	Repetir
		
		Escribir "Oportunidad N°",oportunidad,", porfavor escoger una opción: ";
		Escribir "1) Cara";
		Escribir "2) Sello";
		Leer opcion;
		
		azar1 = Aleatorio(1,2);
		
		Si opcion == 1 o opcion == 2 Entonces
			Si opcion == 1 Entonces
				Si opcion == azar1 Entonces
					
					Escribir "SU ELECCIÓN HA SIDO: CARA";
					Escribir "Lanzando moneda...";
					Escribir "¡¡¡HA SALIDO CARA!!!";
					Escribir "¡¡¡USTED GANA 100 PUNTOS!!!";
					suma_puntos = suma_puntos + 100;
					oportunidad = oportunidad + 1;
				SiNo
					Si opcion <> azar1 Entonces
						
						Escribir "SU ELECCIÓN HA SIDO: CARA";
						Escribir "Lanzando moneda...";
						Escribir "¡¡¡HA SALIDO SELLO!!!";
						Escribir "¡¡¡USTED PIERDE 25 PUNTOS!!!";
						suma_puntos = suma_puntos - 25;
						oportunidad = oportunidad + 1;
						
					FinSi
				FinSi
			SiNo
				Si opcion == 2 Entonces
					Si opcion == azar1 Entonces
						
						Escribir "SU ELECCIÓN HA SIDO: SELLO";
						Escribir "Lanzando moneda...";
						Escribir "¡¡¡HA SALIDO SELLO!!!";
						Escribir "¡¡¡USTED GANA 100 PUNTOS!!!";
						suma_puntos = suma_puntos + 100;
						oportunidad = oportunidad + 1;
					SiNo
						Si opcion <> azar1 Entonces
							
							Escribir "SU ELECCIÓN HA SIDO: SELLO";
							Escribir "Lanzando moneda...";
							Escribir "¡¡¡HA SALIDO CARA!!!";
							Escribir "¡¡¡USTED PIERDE 25 PUNTOS!!!";
							suma_puntos = suma_puntos - 25;
							oportunidad = oportunidad + 1;
							
						FinSi
				    FinSi
			    FinSi
			FinSi
		SiNo
			Escribir "Opción ingresada no válida";
		FinSi
		
		
		
		Escribir "";
	
		
	Hasta Que oportunidad == 4;
	
	Escribir "¡¡¡JUEGO FINALIZADO!!!";
	Escribir "Su puntaje es de: ",suma_puntos;
	
	
	Si suma_puntos >= 200 Entonces
		Escribir "¡¡¡CORRE POR TU BOLETO DE LOTERÍA!!!";
	SiNo
		Escribir "SIGA PARTICIPANDO";
	FinSi
	
FinProceso