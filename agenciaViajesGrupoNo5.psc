Funcion registerUser(id, username, citizenshipCard, i)
	Escribir "Por favor ingrese su id:";
	Leer id[i]; 
	Escribir "Por favor ingrese su nombre completo:";
	Leer username[i]; 
	Escribir "Por favor ingrese su cédula:";
	Leer citizenshipCard[i]; 
FinFuncion

Funcion report(id, username, citizenshipCard, city, endCity, startDate, endDate, i, cont)
	Si (cont > 0) Entonces
		Escribir "Registro actuales " , cont;
		Para f = 1 Hasta i Con Paso 1 Hacer
			Escribir id[f] , " ", username[f], " ", citizenshipCard[f], "| Paquete turistico: ", "ciudad origen ", city, "| ", "ciudad destino", endCity, "| ", startDate, " |", endDate, hotel, hotelPrice 
		Fin Para
	SiNo
		Escribir "No hay registros"
	Fin Si
FinFuncion

Funcion flightPrice<-createPackage(city, endCity, endCity, startDate, endDate, i)
	
	
	Escribir "Por favor escriba la ciudad donde te encuentras:";
	Escribir "BO, CAL, MED, BUN";
	Leer city
	
	Escribir "Por favor escriba la ciudad donde quieres viajar :";
	Escribir "BO, CAL, MED, BUN";
	Leer endCity
	
	Escribir "Por favor la fecha ida:";
	Leer startDate; 
	
	Escribir "Por favor la fecha venida:";
	Leer endDate; 
	
	Si city = "CAL" Y endCity = "BO" O city = "BO" Y endCity = "CAL" Entonces
		flightPrice = 130;
	SiNo
		Si city = "CAL" Y endCity = "MED" O city = "MED" Y endCity = "CAL" Entonces
			flightPrice = 120;
		SiNo
			Si city = "CAL" Y endCity = "BUN" O city = "BUN" Y endCity = "CAL" Entonces
				flightPrice = 60;
			Fin Si
		Fin Si	
	Fin Si
	
FinFuncion

Funcion reservation(members,hotel)
	

FinFuncion


	



Algoritmo AgenciaViajesGrupoNo5
	
	Definir username, startDate, endDate, city, endCity Como Cadena;
	Definir option, i, cont, citizenshipCard, id,  members, hotel  Como Entero;
	Definir flightPrice, totalPrice , hotelPrice Como Real; 
	
	
//	Registro
    i = 1;
	cont = 0
	Dimension  id[22];
	Dimension  username[22];
	Dimension  citizenshipCard[22];
	
	
	Repetir
		Escribir "---------- Menú de inicio ----------"
		Escribir "1. Registrar cliente"
        Escribir "2. Crear paquete turistico"
		Escribir "3. Consultar paquete turistico"
        Escribir "4. Realizar reserva"
        Escribir "5. Realizar pago"
        Escribir "6. Generar reportes"
        Escribir "7. Salir"
		Leer option
		
		Segun option Hacer
			1:
				registerUser(id, username, citizenshipCard, i);
				i = i+1;
				cont = cont+1
			2:
				
			3:
				Escribir lista_de_expresiones
			4:
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
			5:
				flightPrice = members * flightPrice
				totalPrice = hotelPrice + flightPrice
				Escribir "El total a pagar es de: $", totalPrice
			6:
				report(id, username, citizenshipCard, city, endCity, startDate, endDate, i, cont)
			7:
				Escribir "Hasta pronto";
			De Otro Modo:
				Escribir "Opcion invalida";
		Fin Segun
		
	Hasta Que (option = 8);
	
	
FinAlgoritmo


