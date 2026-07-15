def Datos_Usario():
    while True:
        try:
            nombre=input("Ingresa tu nombre: ")
            if len(nombre)>100 or len(nombre)<3:
                 print("Error. el nombre no puede tener entree 3 y 100 caracteres.")
                 continue
            rut=input("Ingresa tu rut: ")
            if len(rut)>20 or len(rut)<10:
                 print("Error. dato no valido, el rut tiene que tener entre 10 y 20 numeros.")
                 continue
        except ValueError:
            print("Error. datos mal ingresados.")
        else:
            guardar_diccionario("nombre", nombre)
            guardar_diccionario("rut", rut)
            break

def calcular_notas_y_ponderaciones(cantidad_notas):
                    lista_notas=[]
                    lista_ponderaciones=[]
                    nota_presentacion=0
                    opc_guardado=None
                    try:
                        for i in range(cantidad_notas):
                            while True:
                                nota=float(input(f"Ingrese una nota {i+1}: "))
                                if nota <1 or nota >7:
                                    print("Error, la nota no puede ser mas baja que un 1 ni mas alta que un 7.")
                                    continue
                                ponderacion=float(input(f"Ingrese la ponderacion {i+1}: "))
                                if ponderacion<0 or ponderacion>1:
                                    print("Error, la ponderacion debe estar entre 0 y 1")
                                    continue
                                nota_presentacion+=(nota*ponderacion)
                                lista_ponderaciones.append(ponderacion)
                                lista_notas.append(nota)
                                break
                        if abs(sum(lista_ponderaciones)-1)>0.001:
                            print("Error, las ponderaciones deben sumar 1. porfavor ingrese nuevas notas y ponderaciones.")
                            return None, None, None
                        print(f"La nota de precentacion es un {nota_presentacion:.1f}")
                        opc_guardado=input("¿Desea almacenar estos resultados? (S/N): ").lower()
                        if opc_guardado == "n":
                            print("Datos no guardados.")
                        elif opc_guardado =="s":
                            guardar_diccionario("nota_presentacion", nota_presentacion)
                    except ValueError:
                        print("Error, debe ingresar un numero.")
                    return(lista_notas,nota_presentacion,opc_guardado)

def nota_presentacion_examen(nota_presentacion):
    nota_examen = (4.0 - nota_presentacion * 0.6) / 0.4
    return nota_examen

def guardar_diccionario(clave, valor):
    Alumno[clave]=valor
    print("Se han almazenado los datos")
          
Alumno={}
Datos_Usario()
opc=None
nota_presentacion=None
while opc!=5:
    print("Bienvenido a la calculaodra de notas V2")
    print("1.Calcular nota de presentación.")
    print("2.Calcular nota necesaria para presentarse al examen.")
    print("3.Calcular nota mínima del examen para aprobar.")
    print("4.Mostrar resumen.")
    print("5. Salir.")
    try:
        opc=int(input("Ingrese una opcion(1/5): "))
        match opc:
            case 1:
                cantidad_notas=int(input("¿Cuantas notas parciales tienes?: "))
                if cantidad_notas <=0:
                    print("La cantidad de notas debe ser mayor a 0.")
                    continue
                else:
                    notas, nota_presentacion, opc_guardado=calcular_notas_y_ponderaciones(cantidad_notas)
            case 2:
                try:
                    nota_presentacion_examen(nota_presentacion)
                    if nota_presentacion is None:
                        print("Cálculo cancelado porque las ponderaciones no suman 1.")
                    if nota_presentacion >= 4.0:
                        print(f"Puedes presentarte al examen, actualmente tienes un {nota_presentacion:.1f}")
                    else:
                        print(f"No puedes presentarte al examen, actualmente tienes un {nota_presentacion:.1f}")
                except TypeError:
                    print("Error. Primero calcula la nota de presentacion.")
            case 3:
                try:
                    nota_examen=nota_presentacion_examen(nota_presentacion)
                except TypeError:
                    print("Error. todavia no calcula la nota de presentacion.")
                else:   
                    if nota_examen > 7:
                        print("Aunque obtenga un 7.0, no alcanza a aprobar.")
                    elif nota_examen < 1:
                        print("Ya está aprobado incluso con la nota mínima.")
                    else:
                        print(f"Necesita un {nota_examen:.1f}")
                    respuesta=input("¿Desea guardar este resultado? (S/N): ").lower()
                    if respuesta=="s":
                        guardar_diccionario("nota_examen", nota_examen)
            case 4:
                  print("---RESUMEN---")
                  print("Nombre:",
                        Alumno.get("nombre","Aun no hay datos"))
                  print("Rut:",
                        Alumno.get("rut", "Aun no hay datos"))
                  print("Nota de presentacion:",
                        Alumno.get("nota_presentacion", "Aun no hay datos"))
                  print("Nota examen:",
                        Alumno.get("nota_examen", "Aun no hay datos"))
            case 5:
                print("Adios.")
            case _:
                print("Error. opcion no valida")
    except ValueError:
        print("Error, opcion ingresada no valida.")