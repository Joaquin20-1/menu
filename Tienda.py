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


def infoOrdenar(tupla):
    if listaVacia(tupla) == 1:
        return 0
    else:
        print("""1. Menor → mayor
2. Mayor → menor""")
        opc = int(input("ingrese una opcion"))
        return opc


def ordenamientoPrecioA(tupla1):
    tupla = list(tupla1)
    if len(tupla) == 1:
        return 1
    for i in range(len(tupla)-1):
        for j in range(len(tupla)-1-i):
            if tupla[j].precio > tupla[j+1].precio:
                tupla[j], tupla[j+1] = tupla[j+1], tupla[j]
    return list(tupla)


def ordenamientoPrecioD(tupla2):
    tupla = list(tupla2)
    if len(tupla) == 1:
        return 1
    for i in range(len(tupla)-1):
        for j in range(len(tupla)-1-i):
            if tupla[j].precio < tupla[j+1].precio:
                tupla[j+1], tupla[j] = tupla[j], tupla[j+1]
    return list(tupla)


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
            opc = infoOrdenar(tuplaProductos)
            if opc == 0:
                print("tupla vacia")
            else:
                match opc:
                    case 1:
                        resultadoA = ordenamientoPrecioA(tuplaProductos)
                        if resultadoA == 1:
                            print("Tupla ordenada Asendente")
                        else:
                            tuplaProductos = resultadoA
                            print("Tupla ordenada Asendente")
                    case 2:
                        resultadoD = ordenamientoPrecioD(tuplaProductos)
                        if resultadoD == 1:
                            print("Tupla ordenada Desendentemente")
                        else:
                            tuplaProductos = resultadoD
                            print("Tupla ordenada Desendentemente")
                    case _:
                        print("Opcion invalida")
        case 9:
            print()
