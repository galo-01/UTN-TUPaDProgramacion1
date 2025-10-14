

with open("productos.txt", "w") as archivo:
    archivo.write("coca loca,120.5,30\n")
    archivo.write("pepsi,350.0,15\n")
    archivo.write("papas 3D,80.0,50\n")
print("Archivo productos.txt creado correctamente.")


def leer_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                nombre, precio, cantidad = linea.split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    return productos


productos = leer_productos()

print("\n Lista de productos actuales:")

for p in productos:
     print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

nombre = input("[Ingrese nombre del producto]: ").strip()
precio = float(input("[Ingrese precio del producto]:"))
cantidad = int(input("[Ingrese cantidad del producto]:"))
productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
print(f"✅ Producto '{nombre}' agregado correctamente.")


nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado → Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("[!] Producto no encontrado.")





with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")





print("//// FIN PROGRAMA ////")