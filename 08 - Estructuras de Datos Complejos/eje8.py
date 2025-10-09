

def pedir_entero(mensaje: str, minimo: int = 0) -> int:
    while True:
        try:
            n = int(input(mensaje))
            if n < minimo:
                print(f"[!] Debe ser un entero ≥ {minimo}.")
                continue
            return n
        except ValueError:
            print("[!] Debe ser un nuero entero válido.")

stock = {"manzanas": 15, "naranjas": 8, "leche": 20}


while True:
    print(
        """
        ==== MENÚ ====
        1) Consultar stock
        2) Agregar unidades 
        3) Agregar nuevo producto
        0) Salir
    """)
    opcion = input("[Elija una opción]:").strip()

    if opcion == "0":
        break

    elif opcion == "1":
        nombre = input("[Producto a consultar]: ").strip().lower()
        if nombre in stock:
            print(f"Stock de '{nombre}': {stock[nombre]} unidades")
        else:
            print(f"'{nombre}' no existe")

    elif opcion == "2":
        nombre = input("[Ingrese de producto]:").strip().lower()
        if nombre in stock:
            cant = pedir_entero("[Ingrese las unidacdes ]", minimo=1)
            stock[nombre] += cant
            print(f"Nuevo stock de '{nombre}': {stock[nombre]}")
        else:
            print(f" '{nombre}' no existe")

    elif opcion == "3":
        nombre = input("[Ingrese el nombre de nuevo producto]:").strip().lower()
        if nombre in stock:
            print(f" '{nombre}' ya existe con stock {stock[nombre]}.")
        else:
            cant = pedir_entero("Stock inicial: ", minimo=0)
            stock[nombre] = cant
            print(f"Agregado '{nombre}' con stock {cant}.")

    else:
        print("- Opción invalida, intentá de nuevo -")


print("//// FIN PROGRAMA ////")