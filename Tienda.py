class Producto():
    def __init__(self, cod, name, prec, stock, cat):
        self.codigo = cod
        self.nombre = name
        self.precio = prec
        self.stock = stock
        self.categoria = cat

    def mostrar(self):
        print("codigo:", self.codigo,
              "\nNombre:", self.codigo,
              "\nPrecio:", self.precio,
              "\nStock:", self.stock,
              "\nCategoria:", self.categoria)


def disminuirStock(tupla):
    if listaVacia(tupla) == 1:
        print("Lista vacia")
        return
    codig = input("Indique el codigo:")
    encontr = False
    for i in tupla:
        if codig == i.codigo:
            cantidad = int(input("Cantidad:"))
            if cantidad <= i.stock:
                i.stock -= cantidad
                encontr = True
                print("Stock disminuyo:-", cantidad)
                return
            else:
                print("Cantidad mayor al stock")
    if not encontr:
        print("Codigo no encontrado")


def aumentarStock(tupla):
    if listaVacia(tupla) == 1:
        print("Lista vacia")
        return
    codig = input("Indique el codigo:")
    encontr = False
    for i in tupla:
        if codig == i.codigo:
            cantidad = float(input("indique la cantidad:"))
            i.stock += cantidad
            encontr = True
            return

    if not encontr:
        print("Codigo no encontrado")


def listaVacia(tupla):
    if len(tupla) == 0:
        return 1
    return 0


def validarCodigo(cod, tupla: tuple[Producto]):
    if listaVacia(tupla) == 1:
        return 2
    encon = False
    for i in tupla:
        if i.codigo == cod:
            encon = True
    if not encon:
        return 1
    else:
        return 0


def llenartupla(cod, tupla):
    resultado = validarCodigo(cod, tupla)
    if resultado == 0:
        return 0
    if resultado == 1 or resultado == 2:
        nom = input("NOMBRE:")
        Precio = float(input("Precio:"))
        stock = int(input("Stock:"))
        Categoria = input("Categoria:")
        prod = Producto(cod, nom, Precio, stock, Categoria)
        return prod


def mostrarDatos(tupla: tuple[Producto]):
    if listaVacia(tupla) == 1:
        print("Lista vacia")
    else:
        for i in tupla:
            i.mostrar()


def buscarProducto(tupla):
    buscar = input("Producto a buscar:")
    encon = validarCodigo(buscar, tupla)
    if encon == 2:
        print("Lista vacia")
    elif encon == 1:
        print("Producto no encontrado")
    else:
        print("Producto encontrado:", buscar)


tuplaProductos = tuple()
while True:
    print("""===== SISTEMA DE PRODUCTOS =====
1. Registrar producto
2. Mostrar productos
3. Buscar producto
4. Modificar producto
5. Eliminar producto
6. Aumentar stock
7. Disminuir stock
8. Ordenar por precio
9. Ordenar por stock
10. Producto con mayor precio
11. Producto con menor stock
12. Filtrar por categoría
13. Valor total del inventario
14. Salir""")
    opc = int(input("Seleccione una opcion:"))
    match opc:
        case 1:
            cod = input("Codigo:")
            resultado = llenartupla(cod, tuplaProductos)
            if resultado == 0:
                print("codigo existente")
            else:
                tuplaProductos += (resultado,)

        case 2:
            mostrarDatos(tuplaProductos)
        case 3:
            buscarProducto(tuplaProductos)
        case 4:
            print()
        case 5:
            print()
        case 6:
            aumentarStock(tuplaProductos)
        case 7:
            disminuirStock(tuplaProductos)

        case 8:
            print()

        case 9:
            print()
