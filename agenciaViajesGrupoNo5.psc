Funcion report(id,username,citizenshipCard,contador)
	Si contador > 1 Entonces
		Escribir "Registro actuales: ",contador;
		Para i = 1 Hasta contador - 1 Hacer
			Escribir "ID: ", id[i], ", Nombre: ", username[i], ", Cédula:", citizenshipCard[i]
		FinPara
	SiNo
		Escribir "No hay usuarios registrados."
	FinSi
FinFuncion


Algoritmo AgenciaViajesGrupoNo5
	

// Declaración de variables
contador = 1
Dimension id[2] 
Dimension username[2]
Dimension citizenshipCard[2]


Repetir
	Escribir "---------- Menú de inicio ----------"
	Escribir "1. Registrar cliente"
	Escribir "2. Crear paquete turistico"
	Escribir "3. Selecionar paquete turistico predeterminado"
	Escribir "4. Generar reportes"
	Escribir "5. Salir"

	Leer option
	
	Segun option Hacer
		1:
			id[contador] <- contador
			Escribir "Ingrese el nombre:"
			Leer username[contador]
			Escribir "Ingrese la cédula:"
			Leer citizenshipCard[contador]
			contador <- contador + 1
			Escribir "Usuario registrado exitosamente!"
		2:
			Escribir "Por favor indique cuantas personas son:";
			Leer members; 
			
			Escribir "Por favor indique cual hotel desea:";
			Escribir "1. Hotel sencillo, 2. Hotel premium" ;
			Leer hotel
			
			Si hotel = 1 Entonces
				hotelPrice = members * 100
				
			SiNo
				si hotel = 2  Entonces
					hotelPrice = members * 250
				FinSi
			Fin Si
			
			Mientras city <> "BO" Y city <> "CAL" Y city <> "MED" Y city <> "BUN" Hacer
				Escribir "Por favor escriba la ciudad donde se encuentra:";
				Escribir "BO, CAL, MED, BUN";
				Leer city
				Si city <> "BO" Y city <> "CAL" Y city <> "MED" Y city <> "BUN" Entonces
					Escribir "Valor inválido. Por favor, ingrese una ciudad válida."
				FinSi
			FinMientras
			
			Mientras endCity <> "BO" Y endCity <> "CAL" Y endCity <> "MED" Y endCity <> "BUN" Hacer
				Escribir "Por favor escriba la ciudad donde quieres viajar:";
				Escribir "BO, CAL, MED, BUN";
				Leer endCity
				Si endCity <> "BO" Y endCity <> "CAL" Y endCity <> "MED" Y endCity <> "BUN" Entonces
					Escribir "Valor inválido. Por favor, ingrese una ciudad válida."
				FinSi
			FinMientras
			
			Escribir "Por favor la fecha ida:";
			Leer startDate; 
			
			Escribir "Por favor la fecha venida:";
			Leer endDate; 
			
			Segun city Hacer
				"CAL":
					Segun endCity Hacer
						"BO": flightPrice = 260 * 2 * members;
						"MED": flightPrice = 240 * 2 * members;
						"BUN": flightPrice = 120 * 2 * members;
					FinSegun
				"BO":
					Segun endCity Hacer
						"CAL": flightPrice = 260 * 2 * members;
						"MED": flightPrice = 120 * 2 * members;
						"BUN": flightPrice = 240 * 2 * members;
					FinSegun
				"MED":
					Segun endCity Hacer
						"BO": flightPrice = 120 * 2 * members;
						"CAL": flightPrice = 240 * 2 * members;
						"BUN": flightPrice = 260 * 2 * members;
					FinSegun	
			Fin Segun	
		3:
			
		4:
			report(id, username, citizenshipCard,contador)
			Escribir "----------  ---------- ---------- ----------"
			totalPrice = flightPrice + hotelPrice;
			Escribir "Fecha de viaje:", startDate, " al ", endDate; 
			Escribir "Vuelo de ida y vuelta " , city, " a ", endCity  ;
			Escribir "Cantidad de personas: ", members 
			
			Si hotel = 1 Entonces
			    hotelH = "Hotel sencillo";
			SiNo
				hotelH = "Hotel premium";
			Fin Si
			Escribir "Hotel: ", hotelH 
			Escribir "---------- ----- Total ----- ----------"
			Escribir "El total a pagar es de: $" ,totalPrice;
		5:
			Escribir "Hasta pronto";
		De Otro Modo:
			Escribir "Opcion invalida";

	Fin Segun
	
Hasta Que (option = 5);
	

FinAlgoritmo
