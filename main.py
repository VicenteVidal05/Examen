productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'FS1230HD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'integrada']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    marca = marca.lower()
    total_stock = 0
    for modelo, info in productos.items():
        if info[0].lower() == marca:
            total_stock += stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total_stock}")

def busqueda_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return False

    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if cantidad > 0 and p_min <= precio <= p_max:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")

    if resultados:
        resultados.sort()
        print(f"Los notebooks entre los precios consultas son: {resultados}")
    else:
        print("No hay notebooks en ese rango de precios.")
    return True

def ordenar_productos():
    if not productos:
        print("No hay notebook disponibles para mostrar")
        return
    print("------- Listado de Notebooks Ordenados --------")
    sorted_items = sorted(productos.items(), key=lambda x: (x[1][0].lower(), x[0].lower()))
    for modelo, info in sorted_items:
        marca = info[0]
        ram = info[2]
        disco = info[4]
        print(f"{marca} - {modelo} - {ram} - {disco}")
    print("------------------------------------------------")

def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")
        opcion = input("Ingrese opción: ")

        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        elif opcion == '2':
            while True:
                p_min = input("Ingrese precio mínimo: ")
                p_max = input("Ingrese precio máximo: ")
                if busqueda_precio(p_min, p_max):
                    break
        elif opcion == '3':
            ordenar_productos()
        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    main()
