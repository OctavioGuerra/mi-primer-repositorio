medicamentos={
    #"nombre"0, "laboratorio"1, "categoria"2, "receta"3, "refrigerador"4, "proovedor"5
}

Inventario={
    #"precio"0, "stock"1
}

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de medicamentos por rango de precio")
    print("3. Actualizar precio de un medicamento")
    print("4. Agregar medicamento")
    print("5. Eliminar medicamento")
    print("6. Salir")
    print("=====================================")
def elegir_opcion():#MOSTRAR MENU NO REQUIERE NINGUN PARAMETRO
    while True:
        try:
            opc=int(input("Ingrese una opcion (1/6): "))
            if opc <=6 and opc >=1:
                return opc
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Error, elija un numero entero.")

def revisar_stock_por_categoria(categoria, medicamentos, Inventario):
    stock=0#DEJAR UN ACOMULIDARO FUERA DEL FOR
    for codigo in medicamentos:
        if medicamentos[codigo][2].lower()==categoria.lower():#SI LA CATEGORIA DE MEDICAMENTOS ES IGUAL 
            stock +=Inventario[codigo][1]                     #A LA CATEGORIA INGRESADA ACOMULAR EL STOCK 
    print(f"Stock total: {stock}")                            #DEL INVENTARO EN EL ACOMULADOR

def busqueda_precio(medicamentos, Inventario, pre_min, pre_max):
    resultados=[] #DEJAR UN ACOMULADOR DE LOS RESULTADOS DEL FOR
    for codigo in Inventario: #REPASAR EL INVENTARIO DEJANDO EL CODIGO COMO I
        precio=Inventario[codigo][0]
        stock=Inventario[codigo][1]
        if pre_min <= precio <= pre_max and stock >0: #VERIFICAR EL PRECIO Y STOCK
            nombre=medicamentos[codigo][0] #SI ESTA BIEN SACAR EL NOMBRE DEL MEDICAMENTOS DE MEDICAMENTOS
            resultados.append(f"{nombre}--{codigo}") #AÑADIR EL NOMBRE Y CODIGO A LOS RESULTADOS
    resultados.sort() #ORDENAR LOS RESULTADOS
    if len(resultados)>0: #VERIFICAR LOS RESULTADOS
        print("Medicamentos encontrados: ")
        for resultado in resultados:
            print(resultado)
    else:
        print("No hay medicamentos dentro del rango")    

def buscar_codigo(Inventario, codigo):
    return codigo.upper() in Inventario

def actualizar_precio(Inventario, codigo, nuevo_precio):
    codigo=codigo.upper()
    if buscar_codigo(Inventario, codigo):
        Inventario[codigo][0]= nuevo_precio
        return True
    else:
        return False

def validar_nombre(nombre):
    return nombre.strip()!=""
def validar_laboratorio(laboratorio):
    return laboratorio.strip()!=""
def validar_categoria(categoria):
    return categoria.strip()!=""
def validar_receta(receta):
    receta=receta.upper()
    return receta=="L" or receta== "R" or receta== "C"
def validar_refrigerador(refrigerador):
    refrigerador= refrigerador.lower()
    return refrigerador == "s" or refrigerador =="n"
def validar_proveedor(proveedor):
    return proveedor.strip()!=""
def validar_precio(precio):
    return precio>0
def validar_stock(stock):
    return stock>=0

def agregar_medicamentos(medicamentos,
                         Inventario,
                         codigo,
                         nombre,
                         laboratorio,
                         categoria,
                         receta,
                         refrigerador,
                         proveedor,
                         precio,
                         stock):
    codigo=codigo.upper()
    if buscar_codigo(medicamentos, codigo):
        return False
    medicamentos[codigo]=[
        nombre,
        laboratorio,
        categoria,
        receta.upper(),
        refrigerador.lower()=="s",
        proveedor]
    Inventario[codigo]=[
            precio,
            stock
        ]
    return True

def eliminar_medicamento(medicamentos, Inventario, codigo):
    codigo=codigo.upper()
    if buscar_codigo(medicamentos, codigo):
        del medicamentos[codigo]
        del Inventario[codigo]
        return True
    else:
        return False

opc=0
while opc!=6:
    mostrar_menu()
    opc=elegir_opcion()
    match opc:
        case 1:
            categoria=input("Ingrese la categoria: ")
            revisar_stock_por_categoria(categoria, medicamentos, Inventario)
        case 2:
            while True:
                try:
                    pre_min=int(input("Ingrese precio minimo: "))
                    pre_max=int(input("Ingrese el precio maximo: "))
                    if pre_max < pre_min:
                        print("El precio minimo no puede ser mayor al maximo")
                    else:
                        break
                except ValueError:
                    print("Error, debe ingresar valores enteros.")
            busqueda_precio(medicamentos, Inventario, pre_min, pre_max)
        case 3:
            seguir="s"
            while seguir.lower()=="s":
                codigo=input("Ingrese el codigo: ")
                try:
                    nuevo_precio=int(input("Ingrese el nuevo precio: "))
                    if nuevo_precio >0:
                        if  actualizar_precio(
                                Inventario,
                                codigo,
                                nuevo_precio):
                            print("Precio actualizado.")
                        else:
                            print("El codigo no existe.")
                    else:
                        print("El precio debe ser mayor que cero.")
                except ValueError:
                    print("Error, debe ingresar un numero entero.")
                seguir=input("¿Desea actualizar otro precio? (n/s): ")
        case 4:
            codigo=input("Codigo: ")
            nombre=input("Nombre:")
            laboratorio=input("Laboratorio: ")
            categoria=input("Categoria: ")
            receta=input("Receta (L/R/C): ")
            refrigerador=input("¿Refrigerado? (s/n): ")
            proveedor=input("Proveedor: ")
            try:
                precio=int(input("Precio: "))
                stock=int(input("Stock: "))
            except ValueError:
                print("Precio y stock debe ser numeros.")
                continue
            if not validar_nombre(nombre):
                print("Nombre invalido")
            elif not validar_laboratorio(laboratorio):
                print("Laboratorio invalido")
            elif not validar_categoria(categoria):
                print("Categoria invalida")
            elif not validar_receta(receta):
                print("Receta invalida")
            elif not validar_refrigerador(refrigerador):
                print("Refrigerador invalido")
            elif not validar_proveedor(proveedor):
                print("proveedor invalido")
            elif not validar_precio(precio):
                print("Precio invalido")
            elif not validar_stock(stock):
                print("Stock invalido")
            else:
                if agregar_medicamentos(
                        medicamentos,
                        Inventario,
                        codigo,
                        nombre,
                        laboratorio,
                        categoria,
                        receta,
                        refrigerador,
                        proveedor,
                        precio,
                        stock):
                    print("Medicamentos agregados correctamente.")
                else:
                    print("El codigo ya existe.")
        
        case 5:
            codigo=input("Ingrese el codigo del medicamento: ")
            if eliminar_medicamento(medicamentos, Inventario, codigo):
                print("Medicamento eliminado correctamente")
            else:
                print("El codigo no existe")
        case 6:
            print("Adios.")
        case _:
            print("Error, opcion no valida")