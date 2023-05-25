Proceso segundos_a_minutos
	Definir seg, seg_restante,minutos Como Entero;
	
	Escribir "Ingresa tiempo en segundos: ";
	Leer seg;
	
	seg_restante = 60 - (seg mod 60);
	minutos = (seg + seg_restante) / 60;
	
	Escribir "Faltan ",seg_restante," segundos para completar ",minutos," minutos";
	
FinProceso
