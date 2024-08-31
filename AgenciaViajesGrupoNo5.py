# Definición de funciones

def register_user(users, i):
    print("Por favor ingrese su nombre completo:")
    username = input()
    
    print("Por favor ingrese su cédula:")
    citizenship_card = input()
    
    print("Por favor ingrese su email:")
    email = input()
    
    print("Por favor ingrese su número de teléfono:")
    telefono = input()
    
    users.append({
        'username': username,
        'citizenship_card': citizenship_card,
        'email': email,
        'telefono': telefono
    })

def report(users, packages):
    if len(users) > 0:
        print("Registros actuales:", len(users))
        for user in users:
            print(f"ID: {user['id']} Nombre: {user['username']} Cédula: {user['citizenship_card']}")
            # Encontrar y mostrar el paquete asociado (si existe)
            user_package = next((pkg for pkg in packages if pkg['user_id'] == user['id']), None)
            if user_package:
                print(f"Paquete turístico: Ciudad origen: {user_package['city']} | Ciudad destino: {user_package['end_city']} | Fecha de ida: {user_package['start_date']} | Fecha de vuelta: {user_package['end_date']} | Precio total: ${user_package['total_price']}")
            else:
                print("No hay paquete asociado.")
    else:
        print("No hay registros")

def create_package(packages, i):
    print("Seleccione una opción:")
    print("1. Seleccionar paquete turístico existente")
    print("2. Crear nuevo paquete turístico")
    
    option = int(input())
    
    if option == 1:
        select_package(packages, i)
    elif option == 2:
        print("Digite la fecha de ida de su viaje: (dd/mm/aa)")
        start_date = input()
        
        print("Digite la fecha de vuelta de su viaje: (dd/mm/aa)")
        end_date = input()
        
        print("Elige la ciudad de origen (Bogotá, Cali, Medellín, Buenaventura):")
        city = input().strip().lower()
        
        print("Elige la ciudad de destino (Bogotá, Cali, Medellín, Buenaventura):")
        end_city = input().strip().lower()
        
        print("Digite el lugar de hospedaje (Hotel, Apartamento):")
        hospedaje = input().strip().lower()
        
        print("Digite el número de habitaciones:")
        habitaciones = int(input())
        
        print("Digite el número de personas:")
        personas = int(input())
        
        print("Digite el número de adultos:")
        adultos = int(input())
        
        print("Digite el número de niños:")
        menores = int(input())
        
        # Precios de vuelos
        flight_prices = {
            ('bogotá', 'cali'): 130, ('cali', 'bogotá'): 130,
            ('cali', 'medellín'): 120, ('medellín', 'cali'): 120,
            ('cali', 'buenaventura'): 60, ('buenaventura', 'cali'): 60
        }
        flight_price = flight_prices.get((city, end_city), 0)
        
        # Calcular el precio del hospedaje
        if hospedaje == 'hotel':
            hotel_price = personas * 100
        elif hospedaje == 'apartamento':
            hotel_price = personas * 70  # Precio para apartamento, ajuste si es necesario
        else:
            hotel_price = 0
        
        # Calcular el precio total
        total_price = flight_price + hotel_price
        
        # Guardar el paquete turístico
        packages.append({
            'user_id': i,
            'city': city.capitalize(),
            'end_city': end_city.capitalize(),
            'start_date': start_date,
            'end_date': end_date,
            'hospedaje': hospedaje,
            'habitaciones': habitaciones,
            'personas': personas,
            'adultos': adultos,
            'menores': menores,
            'flight_price': flight_price,
            'hotel_price': hotel_price,
            'total_price': total_price
        })
    else:
        print("Opción inválida")

def select_package(packages, user_id):
    if len(packages) == 0:
        print("No hay paquetes turísticos disponibles para seleccionar.")
        return
    
    print("Seleccione un paquete turístico existente:")
    for idx, pkg in enumerate(packages, start=1):
        print(f"{idx}. Ciudad de origen: {pkg['city']}, Ciudad de destino: {pkg['end_city']}, Fecha de ida: {pkg['start_date']}, Fecha de vuelta: {pkg['end_date']}, Precio total: ${pkg['total_price']}")
    
    choice = int(input())
    
    if 1 <= choice <= len(packages):
        selected_package = packages[choice - 1]
        # Asociar el paquete seleccionado al usuario
        selected_package['user_id'] = user_id
        print("Paquete seleccionado y asociado correctamente.")
    else:
        print("Opción inválida")

def view_packages(packages):
    if len(packages) > 0:
        print("Paquetes turísticos disponibles:")
        for i, package in enumerate(packages, start=1):
            print(f"Paquete {i}:")
            print(f"Ciudad de origen: {package['city']}")
            print(f"Ciudad de destino: {package['end_city']}")
            print(f"Fecha de ida: {package['start_date']}")
            print(f"Fecha de vuelta: {package['end_date']}")
            print(f"Tipo de hospedaje: {'Hotel' if package['hospedaje'] == 'hotel' else 'Apartamento'}")
            print(f"Número de habitaciones: {package['habitaciones']}")
            print(f"Número de personas: {package['personas']}")
            print(f"Número de adultos: {package['adultos']}")
            print(f"Número de niños: {package['menores']}")
            print(f"Precio del vuelo: ${package['flight_price']}")
            print(f"Precio del hospedaje: ${package['hotel_price']}")
            print(f"Precio total: ${package['total_price']}")
            print("-----------------------------------")
    else:
        print("No hay paquetes turísticos disponibles.")

def reservation():
    print("Por favor indique cuántas personas son:")
    members = int(input())
    
    print("Por favor indique cuál hotel desea:")
    print("1. Hotel sencillo, 2. Hotel premium")
    hotel = int(input())
    
    if hotel == 1:
        hotel_price = members * 100
    elif hotel == 2:
        hotel_price = members * 250
    else:
        hotel_price = 0
    
    return hotel_price

def pay(hotel_price, flight_price):
    total_price = hotel_price + flight_price
    print(f"El total a pagar es de: ${total_price}")

# Paquetes turísticos predeterminados
default_packages = [
    {'city': 'Bogotá', 'end_city': 'Cali', 'start_date': '01/10/2024', 'end_date': '07/10/2024', 'hospedaje': 'hotel', 'habitaciones': 2, 'personas': 2, 'adultos': 2, 'menores': 0, 'flight_price': 130, 'hotel_price': 200, 'total_price': 330},
    {'city': 'Cali', 'end_city': 'Medellín', 'start_date': '15/11/2024', 'end_date': '20/11/2024', 'hospedaje': 'apartamento', 'habitaciones': 1, 'personas': 1, 'adultos': 1, 'menores': 0, 'flight_price': 120, 'hotel_price': 70, 'total_price': 190},
    {'city': 'Medellín', 'end_city': 'Buenaventura', 'start_date': '05/12/2024', 'end_date': '10/12/2024', 'hospedaje': 'hotel', 'habitaciones': 3, 'personas': 4, 'adultos': 2, 'menores': 2, 'flight_price': 60, 'hotel_price': 400, 'total_price': 460}
]

def main():
    users = []
    packages = default_packages.copy()  # Inicializamos con paquetes predeterminados
    i = 1
    hotel_price = 0
    flight_price = 0
    
    while True:
        print("---------- Menú de inicio ----------")
        print("1. Registrar cliente")
        print("2. Crear paquete turístico")
        print("3. Ver paquetes turísticos")
        print("4. Realizar reserva")
        print("5. Realizar pago")
        print("6. Generar reportes")
        print("7. Salir")
        
        option = int(input())
        
        if option == 1:
            register_user(users, i)
            i += 1
        elif option == 2:
            create_package(packages, i)
        elif option == 3:
            view_packages(packages)
        elif option == 4:
            print("Por favor indique cuántas personas:")
            members = int(input())
            print("Por favor indique cuál hotel desea:")
            print("1. Hotel sencillo, 2. Hotel premium")
            hotel = int(input())
            hotel_price = reservation(members, hotel)
        elif option == 5:
            if 'hotel_price' in locals() and 'flight_price' in locals():
                pay(hotel_price, flight_price)
            else:
                print("Debe realizar primero una reserva.")
        elif option == 6:
            report(users, packages)
        elif option == 7:
            print("Hasta pronto")
            break
        else:
            print("Opción inválida")

# Ejecutar el programa
main()
           
