#PROFE NECESITO UN 2.0 o mas PORFA
peliculas={

}
#titutlo0 genero1 duracionmin2 clasificacion3 idioma4 es_3d4

cartelera={

}
#precio0 cupos1

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese una opcion (1/6): "))
            if opcion>6 and opcion<1:
                print("Error, la opcion no puede ser menor que 1 ni mayor que 6.")
            return opcion
        except ValueError:
            print("Error, la opcion debe ser un numero entero.")

def cupos_genero(genero, peliculas, cartelera):
    cupos_disponibles=0
    for genero in peliculas:
        if peliculas[genero][1].lower()==genero.lower:
            cupos_disponibles+=cartelera[genero][1]
    print(f"El total de cupos disponibles es: {cupos_disponibles}")

def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados=0
    for codigo in cartelera:
        precio=cartelera[codigo][0]
        cupos=cartelera[codigo][1]
        if p_min<=precio<=p_max and cupos>0:
            titulo=peliculas[codigo][0]
            resultado.append({titulo}--{codigo})
        resultado.sort()
        if len(resultado)>0:
            print("Las películas encontradas son:")
            for resultado in resultados:
                print(resultado)

def buscar_codigo(codigo):
    return codigo.upper()

def actualizar_precio(codigo, nuevo_precio, cartelera):
    codigo=codigo.upper()
    if buscar_codigo(codigo):
        cartelera[codigo][0]=nuevo_precio
        return True

def validacion_codigo(codigo):
    return codigo.strip()!=""
def validacion_titulo(titulo):
    return titulo.strip()!=""
def validacion_genero(genero):
    return genero.strip()!=""
def validacion_duracion(duracion):
    return duracion >0
def validacion_clasificacion(clasificacion):
    return clasificacion.upper() == "A" or "B" or "C"
def validacion_idioma(idioma):
    return idioma.strip()!=""
def validacion_si_es_3d(es_3d):
    es_3d=es_3d.lower()
    if es_3d == "s":
        return True
def validacion_precio(precio):
    return precio >0
def validacion_cupos(cupos):
    return cupos >=0

def agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    codigo=codigo.upper()
    if validacion_codigo(peliculas, codigo):
        return False
    peliculas[codigo]=[titulo, genero, duracion, clasificacion.upper(), idioma, es_3d.lower()]
    cartelera[codigo]=[precio, cupos]
    return True
    

def eliminar_pelicula(peliculas, cartelera, codigo):
    codigo=codigo.upper()
    if buscar_codigo(peliculas, codigo):
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    else:
        return False

opcion=0
while opcion!=6:
    menu()
    opcion=leer_opcion()
    match opcion:
        case 1:
            genero=input("Ingrese el genero de la pelicual para buscar: ")
            cupos_genero(genero, peliculas, cartelera)
        case 2:
            try:
                p_min=int(input("Ingrese el precio minimo: "))
                p_max=int(input("Ingrese el precio maximo: "))
            except ValueError:
                print("Debe ingresar valores enteros")
                continue
            else:
                busqueda_precio(p_min, p_max, peliculas, cartelera)
        case 3:
            continuar="s"
            while continuar=="s":
                try:
                    codigo=input("Ingrese el codigo a buscar: ")
                    nuevo_precio=int(input("Ingrese el nuevo precio: "))
                except ValueError:
                    print("Error, el precio debe ser un entero positivo")
                else:
                    actualizar_precio(codigo, nuevo_precio, cartelera)
                    if actualizar_precio is True:
                        print("Precio actualizado")
                    elif actualizar_precio is False:
                        print("El código no existe")
        case 4:
            codigo=input("Ingrese código de película:")
            validacion_codigo(codigo)
            if not validacion_codigo(codigo):
                print("Error al ingrsar el codigo")
            titulo=input("Ingrese título: ")
            validacion_titulo(titulo)
            if not validacion_titulo(titulo):
                print("Error al ingrsar el titulo")
            genero=input("Ingrese género: ")
            validacion_genero(genero)
            if not validacion_genero(genero):
                print("Error al ingrsar el genero.")
            duracion=int(input("Ingrese duración (minutos): "))
            validacion_duracion(duracion)
            if not validacion_duracion(duracion):
                print("Error al ingresar la duracion")
            clasificacion=input("Ingrese clasificación: ")
            validacion_clasificacion(clasificacion)
            if not validacion_clasificacion(clasificacion):
                print("Error al ingresar la clasificacion:")
            idioma=input("Ingrese idioma: ")
            validacion_idioma(idioma)
            if not validacion_idioma(idioma):
                print("Error al ingresar el idioma.")
            es_3d=input("¿Es 3D? (s/n): ")
            validacion_si_es_3d(es_3d)
            if not validacion_si_es_3d(es_3d):
                print("Error, ingrese (s) o (n).")
            precio=int(input("Ingrese precio: "))
            validacion_precio(precio)
            if not validacion_precio(precio):
                print("Error al ingresar el precio.")
            cupos=int(input("Ingrese cupos: "))
            validacion_cupos(cupos)
            if not validacion_cupos(cupos):
                print("Error al ingresar los cupos")
            agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
            print("Película agregada")
        case 5:
            codigo=input("Ingrese el codigo de la pelicula a borrar: ")
            eliminar_pelicula(peliculas, cartelera, codigo)
            if eliminar_pelicula is True:
                print("Película eliminada")
            else:
                print("El código no existe")
        case 6:
            print("Programa finalizado.")
        case _:
            print("Debe seleccionar una opción válida")