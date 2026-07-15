Datos=[]
def agregar_nombre(nom_del_socio):
    return nom_del_socio.strip()!=""
def agregar_clases(clases_del_soscio):
    return clases_del_soscio >= 0
def agregar_mensualidad(mensualidad_del_socio):
    return mensualidad_del_socio>0

def agregar_socio(Datos):
    nom_del_socio=input("Ingrese su nombre: ")
    if not agregar_nombre(nom_del_socio):
        print("Nombre invalido.")
        return
    clases_del_soscio=int(input("Ingrese la cantidad de clases: "))
    if not agregar_clases(clases_del_soscio):
        print("Dato invalido")
        return
    mensualidad_del_socio=float(input("Ingrese su mensualidad: "))
    if not agregar_mensualidad(mensualidad_del_socio):
        print("Valor de la mensualidad no valido")
        return
    inf_usuario={
        "nombre":nom_del_socio,
        "clases_disponibles":clases_del_soscio,
        "mensualidad":mensualidad_del_socio,
        "activo":False
        }
    Datos.append(inf_usuario)
    print("Datos de usuario agregados correctamente.")

def buscar_socio(Datos, nom_buscar):
    for i in range(len(Datos)):
        if Datos[i]["nombre"]==nom_buscar:
            return i
    return -1

def eliminar_socio(Datos):
    nom_del_socio=input("Ingrese el nombre del socio a eliminar: ")
    posicion=buscar_socio(Datos, nom_del_socio)
    if posicion != -1:
        del Datos[posicion]
        print("Socio eliminado correctamnete")
    else:
        print(f"El socio '{nom_del_socio}' no se encuentra registrado.")

def actualizar_estado_del_socio(Datos):
    for inf_usuario in Datos:
        if inf_usuario["clases_disponibles"]>0:
            inf_usuario["activo"]=True
        else:
            inf_usuario["activo"]=False

def mostrar_socios(Datos):
    actualizar_estado_del_socio(Datos)
    print("=== LISTA DE SOCIOS ===")
    for inf_usuario in Datos:
        if inf_usuario["activo"]:
            estado="ACTIVO"
        else:
            estado="INACTIVO"
        print(f"Nombre: {inf_usuario['nombre']}")
        print(f"Clases disponibles: {inf_usuario['clases_disponibles']}")
        print(f"Mensualidad: {inf_usuario['mensualidad']}")
        print(f"Estado: {estado}")
        print(f"************************************")

def Menu_principal():
    print("=====MENU PRINCIPAL======")
    print("1. Agregar socios.")
    print("2. Buscar socio")
    print("3. Eliminar socio")
    print("4. Actualizar estado de socios.")
    print("5. Mostrar socios.")
    print("6. Salir.")
    print("==========================")
    pass
def Elegir_opcion():
    while True:
        try:
            opc=int(input("Ingrese una opcion (1/6): "))
            if opc >=1 and opc <=6:
                return opc
            print("opcion fuera de rango")
        except ValueError:
            print("Error. Ingrese un numero entero dentro de los parametros.")

opc = 0

while opc!=6:
    Menu_principal()
    opc=Elegir_opcion()
    if opc==1:
        agregar_socio(Datos)
    elif opc==2:
        nom_buscar=input("Ingrese el nombre del socio a buscar")
        posicion=buscar_socio(Datos, nom_buscar)
        if posicion != -1:
            print("Socio encontrado.")
            print(f"Nombre: {Datos[posicion]['nombre']}")
            print(f"Clases disponibles: {Datos[posicion]['clases_disponibles']}")
            print(f"Mensualidad: {Datos[posicion]['mensualidad']}")
        else:
            print("Socio no encontrado")
    elif opc==3:
        eliminar_socio(Datos)
    elif opc==4:
        actualizar_estado_del_socio(Datos)
    elif opc==5:
        mostrar_socios(Datos)
    elif opc==6:
        print("Gracias por preferirnos. ¡Nos vemos pronto!")
    else:
        print("Error. Ingrese un valor valido.")