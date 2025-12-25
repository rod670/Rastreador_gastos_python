import csv
import os
Archivo_gastos = "mis_gastos.csv"
def inicializar_archivo():
    if not os.path.exists(Archivo_gastos):
        with open(Archivo_gastos, "w", newline= '') as registro:
            escritor = csv.writer(registro)
            escritor.writerow(["Concepto", "Monto", "Fecha"])
def registrar_gastos():
    print("Registrar nuevo gasto...")
    concepto = input("¿En que gastaste? ").strip()
    while True:
        try:
            monto = float(input("¿Cuánto gastaste? "))
            break
        except ValueError:
            print("Ingresa únicamente numeros válidos")
    fecha = input("Ingresa la fecha (DD/MM/AAAA): ")
    with open(Archivo_gastos, "a", newline= '') as registro:
        escritor = csv.writer(registro)
        escritor.writerow([concepto, monto, fecha])
        print("Gasto registrado")
def gastos():
    print("Historial de gastos...")
    if not os.path.exists(Archivo_gastos):
        print("Aún no tienes gastos registtrados")
        return
    total = 0.0
    with open(Archivo_gastos, "r") as registro:
        lector = csv.reader(registro)
        next(lector)
        print(f"{'Concepto':<20} | ${'Monto':<10} | {'Fecha':<12}")
        print("-" * 46)
        for fila in lector:
            concepto = fila[0].capitalize().strip()
            monto = float(fila[1])
            fecha = fila[2]
            total +=monto
            print(f"{concepto:<20} | ${monto:<9.2f} | {fecha:<12}")
            print("-"*46)
        print(f"Total gastado: ${total:.2f}")
def filtro_monto():
    minimo = input("Ingresa el monto minimo para observar los gastos igual o mayores a este: ")
    if minimo.isdigit():
        minimo = float(minimo)
        total = 0
        with open(Archivo_gastos, "r") as registros:
            lector = csv.reader(registros)
            next(lector)
            print(f"{'Concepto':<20} | ${'Monto':<10} | {'Fecha':<12}")
            print("-" * 46)
            encontrado = False
            for fila in lector:
                nombre = fila[0].capitalize().strip()
                precio = float(fila[1])
                fecha = fila[2]
                if precio >= minimo:
                    print(f"{nombre:<20} | ${precio:<9.2f} | {fecha:<12}")
                    print("-"*46)
                    total += precio
                    encontrado = True
            print(f"Total: {total:.2f}")
            if encontrado == False:
                print(f"No se ha encontrado gastos registrados con un precio igual o mayor a {minimo}")
    else:
        print("Monto inválido. Procure ingresar únicamente números")
def filtro_nombre():
    producto = input("Ingresa el nombre del producto que deseas filtrar (Procura que este escrito igual que como tú lo registraste): ").capitalize().strip()
    total = 0
    with open(Archivo_gastos, "r") as registros:
        lector = csv.reader(registros)
        next(lector)
        print(f"{'Concepto':<20} | ${'Monto':<10} | {'Fecha':<12}")
        print("-" * 46)
        encontrado = False
        for fila in lector:
            nombre = fila[0].capitalize().strip()
            precio = float(fila[1])
            fecha = fila[2]
            if nombre.capitalize() == producto:
                print(f"{nombre:<20} | ${precio:<9.2f} | {fecha:<12}")
                print("-"*46)
                total += precio
                encontrado = True
        print(f"Total: {total:.2f}")
        if encontrado == False:
            print(f"No se ha encontrado productos registrados con el nombre de {producto}")
def filtro_fecha():
    fecha_filtro = input("Ingresa la fecha que deseas filtrar. Recuerda que el formato es DD/MM/AAAA: ").strip()
    total = 0
    with open(Archivo_gastos, "r") as registros:
        lector = csv.reader(registros)
        next(lector)
        print(f"{'Concepto':<20} | ${'Monto':<10} | {'Fecha':<12}")
        print("-" * 46)
        encontrado = False
        for fila in lector:
            nombre = fila[0].capitalize().strip()
            precio = float(fila[1])
            fecha = fila[2]
            if fecha == fecha_filtro:
                print(f"{nombre:<20} | ${precio:<9.2f} | {fecha:<12}")
                print("-"*46)
                total += precio
                encontrado = True
        print(f"Total: {total:.2f}")
        if encontrado == False:
            print(f"No se han encontrado registros de gastos en la fecha {fecha_filtro}")
def filtro_gastos():
    print("---Menú---")
    print("1._ Filtrar por monto gastado")
    print("2._ Filtrar por producto comprado")
    print("3._ Filtrar por fecha de gasto")
    print("4._ Ver todos el registro de gastos")
    seleccion = input("Ingresa una opción: ")
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if seleccion == 4:
            gastos()
        elif seleccion == 1:
            filtro_monto()
        elif seleccion == 2:
            filtro_nombre()
        elif seleccion == 3:
            filtro_fecha()
        else:
            print("Opción inválida. Seleccione únicamente las opciones válidas.")
    else:
        print("Ingrese únicamente las opciones que se muestran.")
def menu():
    inicializar_archivo()
    while True:
        print("---Registro de gastos personales---")
        print("1._ Agregar gasto")
        print("2._ Ver gastos")
        print("3._ Salir")
        opcion = input("Elige una opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                registrar_gastos()
            elif opcion == 2:
                filtro_gastos()
            elif opcion == 3:
                break
            else:
                print("Opción inválida. Selecciona una de las opciones visibles")
        else:
            print("Ingrese una de las opciones válidas")
            continue
menu()