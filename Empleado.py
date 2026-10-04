class empleado():
    def __init__(self, cod, nom, edad, sueldo, area):
        self.codigo = cod
        self.nombre = nom
        self.edad = edad
        self.sueldo = sueldo
        self.area = area

    def mostrar(self, tupla):
        print("------DATOS-------")
        print(f"codigo:{self.codigo}"
              f"\nNombre:{self.nombre}"
              f"\nEdad:{self.edad}"
              f"\nSueldo:{self.sueldo}"
              f"\nArea:{self.area}")
        print("-"*18)


def Registrar():
    nom = input("NOMBRE:")
    cod = input("Codigo:")
    edad = int(input("Edad:"))
    sueldo = float(input("Sueldo:"))
    area = input("Area:")
    emple = empleado(cod, nom, edad, sueldo, area)
    return emple


def RecorrerTupla(tupla: tuple[empleado]):
    for i in tupla:
        i.mostrar(tupla)


def buscarEmpleado(tupla: tuple[empleado]):
    buscar = input("EMPLEADO A BUSCAR:")
    for i in tupla:
        if i.nombre == buscar:
            return print(f"Empleado encontrado:{i.nombre}\nCodigo:{i.codigo}")
    print("empleado no encontrado")


def mayorSueldo(tupla: tuple[empleado]):
    sueldo = 0
    nomemp = ""
    for i in tupla:
        if i.sueldo > sueldo:
            sueldo = i.sueldo
            nomemp = f"Nombre:{i.nombre}\nSueldo:{i.sueldo}"
    if nomemp != "":
        print(nomemp)
    else:
        print("no hay ningun Registro")


def promedioSueldos(tupla: tuple[empleado]):
    total = 0
    for i in tupla:
        total += i.sueldo
    if len(tupla) > 0:
        total /= len(tupla)
        print("Promedio:", total)
    else:
        print("Lista vacia")


def filtrarPorArea(tupla):
    if len(tupla) == 0:
        print("lista vacia")
        return
    area = input("ingrese su area:")
    encont = False
    for i in tupla:
        if area == i.area:
            i.mostrar(tupla)
            encont = True
    if not encont:
        print("dato no encontrado")


def aumentarSueldo(tupla):
    if len(tupla) == 0:
        print("lista vacia")
        return
    cod = input("ingrese el codigo:")
    porcen = float(input("INGRESE EL PORCENTAJE:"))
    for i in tupla:
        if cod == i.codigo:
            i.sueldo += i.sueldo*(porcen/100)
            i.mostrar(tupla)


empleados = ()
while True:
    print("""1. Registrar empleados
2. Mostrar empleados
3. Buscar empleado
4. Mayor sueldo
5. Promedio de sueldos
6. Filtrar por área
7. Aumentar sueldo
8. Salir""")
    opc = int(input("SELECCIONE UNA OPCION:"))
    match opc:
        case 1:
            empleados += (Registrar(),)
        case 2:
            RecorrerTupla(empleados)
        case 3:
            buscarEmpleado(empleados)
        case 4:
            mayorSueldo(empleados)
        case 5:
            promedioSueldos(empleados)
        case 6:
            filtrarPorArea(empleados)
        case 7:
            aumentarSueldo(empleados)
        case 8:
            print("ADIOS")
            break
        case _:
            print("OPCION INVALIDA")
