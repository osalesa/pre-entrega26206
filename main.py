productos = []

while True:

    print("="*40)
    print("Sistema de inventario para ferreteria")
    print("="*40)
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Eliminar productos")
    print("5. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        print("--- Sección para agregar productos ---")

        nombre = input("Nombre del  producto: ").strip()
        while nombre == "":
            print("ERROR: por favor ingrese un producto")
            nombre = input("Nombre del  producto: ").strip()

        categoria = input("Ingrese una categoría: ").strip()
        while categoria == "":
            print("ERROR: Por favor ingrese una categoria.")
            categoria = input("Ingrese una categoría: ").strip()
        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("ERROR: Por favor solo números enteros.")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre, categoria, precio]
        productos.append(datos)

    elif opcion == "2":
        print("--- Lista de productos ---")

        if len(productos) == 0:
            print("La lista esta vacia")
        else:
            for i in range(len(productos)):
                print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoría: {productos[i][1]}\n-Precio: ${productos[i][2]}")


    elif opcion == "5":
        print("¡Gracias por usar nuestro sistema de gestión!")
        break
    else:
        print("Opción no encontrada, por favor elija una opción entre 1 y 5")
        