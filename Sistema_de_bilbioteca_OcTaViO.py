libros=[]

def Menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad de préstamo")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")
def leer_opcion():
    while True:
        try:
            opc=int(input("Ingrese una opcion (1/6): "))
            if opc >=1 and opc<=6:
                return opc
            else:
                print("La opcion debe estar entre 1 y 6.")
        except ValueError:
            print("Ingrese un numero entro valido.")       
def validar_titulo(titulo):
    return titulo.strip()!=""
def validar_ejemplares(ejemplares):
    return ejemplares >=0
def validar_valor(valor):
    return valor>0

def agregar_libro(libros):
    titulo=input("Ingrese el titulo del libro: ")
    if not validar_titulo(titulo):
       print("titulo invalido")
       return
    ejemplares=int(input("Ingrese la cantidad de ejemplares: "))
    if not validar_ejemplares(ejemplares):
        print("ejemplar invalido")
        return
    valor=float(input("Ingrese el valor del libro: "))
    if not validar_valor(valor):
        print("valor invalido")
        return
    libro ={"titulo": titulo,
            "ejemplares": ejemplares,
            "valor": valor,
            "prestable": False}
    libros.append(libro)
    print("Libro agregado correctamente.")

def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"]==titulo:
            return i
    return -1

def eliminar_libro(libros):
    titulo=input("Ingrese titulo: ")
    posicion = buscar_libro(libros, titulo)
    if posicion!= -1:
        del libros[posicion]
        print("Libro eliminado corectamente.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado")

def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["ejemplares"]>0:
            libro["prestable"]=True
        else:
            libro["prestable"]=False
            
def mostrar_libros(libros):
    actualizar_disponibilidad(libros)
    print("==== LISTA DE LIBROS ====")
    for libro in libros:
        if libro["prestable"]:
            estado="DISPONIBLE"
        else:
            estado="NO DISPONIBLE"
        print("*********************************")
        print(f"Titulo: {libro['titulo']}")
        print(f"Ejemplares: {libro['ejemplares']}")
        print(f"Valor: {libro['valor']}")
        print(f"Estado: {estado}")  

opc=0
while True:
    Menu_principal()
    opc=leer_opcion()
    if opc==1:
        try:
            agregar_libro(libros)
        except ValueError:
            print("Debe ingresar un valor valido.")
    elif opc==2:
        titulo=input("Ingrese el titulo a buscar: ")
        posicion=buscar_libro(libros, titulo)
        if posicion !=-1:
            print("Libro encontrado")
        else:
            print("Libro no encontrado")
    elif opc==3:
        eliminar_libro(libros)
    elif opc==4:
        actualizar_disponibilidad(libros)
    elif opc==5:
        mostrar_libros(libros)
    elif opc==6:
        print("Gracias por usar el sistema.")
        break