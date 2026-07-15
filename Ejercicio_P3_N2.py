opc=None
monto=0
monto_mayor=None
monto_menor=None
while opc !="4":
    print("")
    print("1-Ingresar montos.")
    print("2-Mostrar monto mayor.")
    print("3-Mostrar monto menor.")
    print("4-Salir.")
    opc=input("Ingrese una opcion 1-4:")
    match opc:
        case "1":
            while True:
                try:
                    monto=int(input("Ingresar monto (1-10000): "))
                    if monto >=1 and monto <=10000:
                        if monto_mayor is None or monto>monto_mayor:
                            monto_mayor=monto
                        if monto_menor is None or monto<monto_menor:
                            monto_menor=monto
                        print("Monto ingresado correctamente.")
                        break
                    else:
                        print("Debe estar entre 1 y 10000")
                except ValueError:
                    print("Debe ingresar un numero entero!!")
        case "2":
            if monto_mayor != None:
                print(f"El monto mayor ingresado hasta el momento es: {monto_mayor}")
            else:
                print("No se han ingresado montos.")

        case "3":
            if monto_menor != None:
                print(f"El monto menor ingresado hasta el momento es: {monto_menor}")
            else:
                print("No se han ingresado montos.")
        case "4":
            print("Hasta pronto")
        case _:
            print("Ingrese una opcion valida.")