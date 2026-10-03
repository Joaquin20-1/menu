def mostrar(tupla):
    for i in tupla:
        print(i)


def mostrarstock10(tupla):
    print("stock mayor a 10")
    for i in tupla:
        if i[2] > 10:
            print(i)


def dinerostock(tupla):
    total = 0
    for i in tupla:
        total += i[1]*i[2]

    return total


def buscarProducto(tupla, producto):
    for i in tupla:
        if producto == i[0]:
            return "Producto encontrado"

    return "Producto no encontrado"


productos = (
    ("Laptop", 2500, 10),
    ("Mouse", 50, 20),
    ("Teclado", 100, 15),
    ("Monitor", 800, 5),
    ("Audifonos", 150, 12)
)

mostrar(productos)
mostrarstock10(productos)
print(f"DINERO TOTAL: {dinerostock(productos)}")
buscar = input("producto:")
print(buscarProducto(productos, buscar))
