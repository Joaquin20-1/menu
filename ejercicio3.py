def totalVendido(tupla):
    total = 0
    for i in tupla:
        total += i[2]*i[3]

    print("TOTAL:", total)


def mostrarVentas(tupla):
    for i in tupla:
        print(i)


def ventaMayor(tupla):
    total = 0
    producto = ""
    for i in tupla:
        totalv = i[2]*i[3]
        if totalv > total:
            total = totalv
            producto = f"producto:{i[1]}\nTotal:{total}\ngenero mayor ganancia"
    print(producto)


def buscarProducto(tupla):
    buscar = input("Producto a buscar:")
    for i in tupla:
        if buscar == i[1]:
            return print(i)
    print("no encontrado")


def filtrarCategoria(tupla):
    buscarCat = input("Categoria a buscar:")
    cat = False
    for i in tupla:
        if buscarCat == i[4]:
            print(i)
            cat = True
    if not cat:
        print("Categoria no encontrado")


def stockvendido(tupla):
    tota = 0
    for i in tupla:
        tota += i[3]
    return print("TOTAL VENDIDO:", tota)


ventas = (
    (101, "Laptop", 2500, 2, "Tecnologia"),
    (102, "Mouse", 50, 10, "Tecnologia"),
    (103, "Polo", 40, 5, "Ropa"),
    (104, "Teclado", 120, 3, "Tecnologia"),
    (105, "Zapatillas", 180, 4, "Ropa"),
    (106, "Monitor", 900, 2, "Tecnologia")
)
while True:
    print(""""1. Mostrar ventas
2. Total vendido
3. Venta mayor
4. Buscar producto
5. Filtrar categoría
6. Total de unidades
7. Reporte
8. Salir""")
    opc = int(input("ingrese una opcion:"))
    match opc:
        case 1:
            mostrarVentas(ventas)
        case 2:
            totalVendido(ventas)
        case 3:
            ventaMayor(ventas)
        case 4:
            buscarProducto(ventas)
        case 5:
            filtrarCategoria(ventas)
        case 6:
            stockvendido(ventas)
        case 7:
            print("===== REPORTE =====")
            totalVendido(ventas)
            stockvendido(ventas)
            ventaMayor(ventas)

        case 8:
            print("ADIOS")
            break
        case _:
            print("OPCION INVALIDA")
