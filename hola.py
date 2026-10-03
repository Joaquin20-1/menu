class persona():
    def __init__(self, nombre, edad, genero, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    def mostrarDatos(self):
        print(
            f"Hola, soy {self.nombre}, tengo {self.edad} años, soy {self.genero} y trabajo como {self.ocupacion}.")

    def calcularDesc(self):
        try:
            if self.edad > 18:
                print("tienes un 20 % de descuento")
            else:
                print("No tienes descuento")
        except TypeError:
            print("datos invalidos")


def llenarlista():
    nom = input("INGRESE EL NOMBRE:")
    edad = int(input("INGRESE LA EDAD:"))
    gene = input("INGRESE EL GENERO:")
    ocp = input("INGRESE LA OCUPACION:")
    return nom, edad, gene, ocp


def recorrer(tupla: tuple[persona]):
    for i in tupla:
        i.mostrarDatos()


def eliminarPorPosci(pos, tupla: tuple):
    return tupla[:pos] + tupla[pos+1:]


def ordenamientoburbuja(tupla: tuple[persona]):
    lista = list(tupla)
    for i in range(len(tupla)-1):
        for j in range(len(tupla)-1-i):
            if lista[j].edad > lista[j+1].edad:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return tuple(lista)


def suma(a):
    a += 10
    return a


tupla = tuple()
while True:
    print("""
1:Registrar persona
2:Eliminar persona
3:Mostrar personas
4:Salir         
5:Calcular promo  
6:ordenar codigo                                                                                     
""")
    opc = int(input("Ingrese una opción: "))
    match opc:
        case 1:
            nom, edad, gene, oco = llenarlista()
            person = persona(nom, edad, gene, oco)
            tupla += (person,)
        case 2:
            dato = int(input("INGRESE LA POSICION"))-1
            tupla = eliminarPorPosci(dato, tupla)
            recorrer(tupla)
        case 3:
            recorrer(tupla)
        case 4:
            print("ADIOS")
            break
        case 5:
            try:
                person.calcularDesc()
            except Exception:
                print("inserte persona")
        case 6:
            tupla = ordenamientoburbuja(tupla)
            recorrer(tupla)
        case _:
            print("DATO INVALIDO")
