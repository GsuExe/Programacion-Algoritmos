Proceso notas_estudiantes
	Definir nota,cant_notas,suma_aprob,suma_reprob Como Real;
	Definir cant_aprob,cant_reprob,contador Como Real;
	
	Escribir "¿Cuántas notas ingresará?: ";
	Leer cant_notas;
	
	contador = 0;
	suma_aprob = 0;
	suma_reprob = 0;
	cant_aprob = 0;
	cant_reprob = 0;
	
	Repetir
		Escribir "Ingrese una nota (Escala 1.0 a 7.0): ";
		Leer nota;
		
		Si 1.0 <= nota y nota < 4.0 Entonces
			Escribir "Reprobado";
			Escribir "";
			suma_reprob = suma_reprob + nota;
			cant_reprob = cant_reprob + 1;
		SiNo
			Si 4.0 <= nota y nota <= 7.0 Entonces
				Escribir "Aprobado";
				Escribir "";
				suma_aprob = suma_aprob + nota;
				cant_aprob = cant_aprob + 1;
			FinSi
		FinSi
		
		contador = contador + 1; 
		
	Hasta Que contador == cant_notas;
	
	Escribir "Usted tiene ",cant_reprob," notas desaprobadas";
	Escribir "Usted tiene ",cant_aprob," notas aprobadas";
	Escribir "Su promedio de notas es ",(suma_aprob + suma_reprob) / cant_notas;
	Escribir "El promedio de notas aprobadas es ",suma_aprob / cant_aprob;
	Escribir "El promedio de notas desaprobadas es ",suma_reprob / cant_reprob;
	
	
FinProceso
