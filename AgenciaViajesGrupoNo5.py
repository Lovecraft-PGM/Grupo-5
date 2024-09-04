def registerUser(id, count, save):
    id.append(len(id) + 1)  # Agregar el siguiente ID a la lista
    username = input("Por favor ingrese su nombre completo:");
    mail = input("Por favor ingrese su correo electronico:");
    citizenshipCard = input("Por favor ingrese la cédula:");
    print("Usuario registrado exitosamente!")

    save.append({
        "id": id[-1],  
        "username": username,
        "citizenshipCard": citizenshipCard,
        "email": mail
    })


def report(save):
    if len(save) > 0:
        print("Registros actuales:", len(save))
        for i in save:
            print(f"ID: {i["id"]} Nombre: {i["username"]} Cédula: {i["citizenshipCard"]} , Correo: {i["email"]}");
    else:
        print("No hay registros de usuarios")

def createPackage(packageNew):

    # Inicializar variables
    cities = ["CTG", "CLO", "MDE", "BOG"];
    members = int(input("Ingrese el número de miembros: "));

    # Validar ciudad de origen
    while True:
        city = input("Por favor escriba la ciudad donde se encuentra (Bogotá(BOG), Cartagena(CTG), Cali(CLO), Medellín(MDE)): ").upper();
        if city in cities:
            break
        print("Valor inválido. Por favor, ingrese una ciudad válida diferente a la de origen.")

    # Validar ciudad de destination
    while True:
        endCity = input("Por favor escriba la ciudad donde quieres viajar (Bogotá(BOG), Cartagena(CTG), Cali(CLO), Medellín(MDE)): ").upper();
        if endCity in cities and endCity != city:
            break
        print("Valor inválido. Por favor, ingrese una ciudad válida diferente a la de origen.")

    # Obtener fechas
    startDate = input("Por favor ingrese la fecha de ida (DD/MM/AA): ")
    endDate = input("Por favor ingrese la fecha de vuelta (DD/MM/AA): ")

    #Precio del vuelo 
    flightPrices = {
        ("CLO", "BOG"): 260, ("BOG", "CLO"): 260,
        ("CLO", "MDE"): 240, ("MDE","CLO"): 240,
        ("CLO", "CTG"): 170, ("CTG", "CLO"): 170, 
    }
    #Sacar los datos del diccionario 
    flightPrice = flightPrices.get((city, endCity), 0) * 2 * members
    
    hotel = int(input("Por favor indique cual hotel desea\n"
    ".1. Hotel sencillo, 2. Hotel premium: "));
   
    # Precios de hospedaje
    if hotel == 1:
        hotelPrice = members*100
    elif hotel == 2:
        hotelPrice = members*250
    else:
        print("Opción de hotel inválida")
    
    
    print(f"El price total del vuelo es: ${flightPrice}")
    print(f"El price total por la hospedad de {members} personas en un {hotel}, es: ${hotelPrice}")
    
    totalPrice = flightPrice + hotelPrice;
    
    packageNew.append({
        "city": city,
        "endCity": endCity,
        "startDate": startDate,
        "endDate": endDate,
        "members": members,
        "flightPrice": flightPrice,
        "hotel": hotel,
        "hotelPrice": hotelPrice,
        "totalPrice": totalPrice
    })

# def ViewPackages(defaultPackages):
#     print("Paquetes turísticos nacionales en Colombia:")
#     for i, package in defaultPackages.items():
#         if package["destination"] in ["Amazonas", "Quindío", "Cancún", "Bogotá", ...]:  # Agregar más destinations colombianos
#             print(f"{i}. {package['namePackage']} - {package['destination']}")
#             print(f"  Duración: {package['days']} días")
#             print(f"  Precio: ${package['price']}")
#             print(f"  Actividades: {', '.join(package['members'])}")
#             print("--------------" )
  
            
# defaultPackages = {
#   1: {
#     "namePackage": "Aventura en la Selva",
#     "destination": "Amazonas",
#     "days": 7,
#     "price": 1500,
#     "members": 2
#   },
#   2: {
#     "namePackage": "Relax en la Playa",
#     "destination": "San Andres",  
#     "days": 5,
#     "price": 1200,
#     "members": 4
#   },
#   3: {
#     "namePackage": "Valle del cocora",
#     "destination": "Quindio",
#     "days": 10,
#     "price": 2500,
#     "members": 3
#   }
# }

# for idPackage, informationPackage in defaultPackages.items():
#     print(f"Paquete {idPackage}:")
#     print(f"  Nombre: {informationPackage['namePackage']}")
#     print(f"  Destino: {informationPackage['destination']}")
#     print(f"  Duración: {informationPackage['days']} días")
#     print(f"  Precio: ${informationPackage['price']}")
#     print(f"  Cantidad personas:{informationPackage['members']}")
#     print("------------------------------")   

      
def main():
    count = 0
    
    # Inicializamos la lista vacia
    save = []  
    packageNew = []
    defaultPackages = []
    package = []
   
    id = []  

    while True:
        print("---------- Menú de inicio ----------\n"
              "1. Registrar cliente\n"
              "2. Crear paquete turistico\n"
              "3. Generar reportes\n"
              "4. Salir")

        option = int(input("Elige una opcion:"))

        if option == 1:
            registerUser(id, count, save)
        elif option == 2:
            if save:
                createPackage(packageNew);
            else:
                print("Primero debe registrarse")
            print("Hasta pronto")  
        # elif option == 3:
        #     # ViewPackages(defaultPackages);
        #     print("Hasta pronto")  
        elif option == 3:
            report(save)
            if packageNew:
                for package in packageNew:
                    print("----------  Detalles del Paquete  ----------")
                    print(f"Fecha de viaje: {package["startDate"]} al {package["endDate"]}")
                    print(f"Vuelo de ida y vuelta {package["city"]} a {package["endCity"]}")
                    print(f"Cantidad de personas: {package["members"]}")
                    hotel = "Hotel sencillo" if package["hotel"] == 1 else "Hotel premium"
                    print(f"Hotel: {hotel}")
                    print(f"Precio total: ${package["totalPrice"]:.2f}")
            else:
                print("No hay packages registrados")
        elif option == 4:
            print("Hasta pronto")  
        else: 
            print("Por favor ingrese una opción valida");   

# Ejecución del programa
main()   
           
