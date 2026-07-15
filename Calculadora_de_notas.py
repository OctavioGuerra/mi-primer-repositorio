print("¡Bienvenido/a a la Calculadora de Notas!")
ultima_nota_presentacion=0
nota_presentacion=0
cantidad_de_notas=0
opcion=0
while opcion !="4":
    print("1-Calcular notas. ")
    print("2-Calcular nota faltante. ")
    print("3-Calcular nota minima para el examen. ")
    print("4-Salir. ")
    opcion=input("Ingrese una opcion (1-4). ")
    match opcion:
            case "1":
                suma=0
                try:
                    cantidad_de_notas=int(input("Ingrrese la cantidad de notas: "))
                    for indice in range (cantidad_de_notas):
                        nota=float(input("\nIngrese su nota: "))
                        ponderacion=float(input("Ingrese la ponderacion de la nota: "))
                        suma += nota*ponderacion
                        indice+=1
                except ValueError:
                    print("---Error, Solo se puede ingresar NUMEROS.---")
                else:
                    print("\n")
                    nota_presentacion=suma
                    print(f"El promedio final es: {nota_presentacion}")
            case "2":
                try:
                    suma=0
                    suma_ponderacion=0
                    if cantidad_de_notas <= 0:
                        print("No ha ingresado los datos anteriores, porfavor vuelva.")
                    else:
                        for indice in range(cantidad_de_notas):
                            if indice != cantidad_de_notas-1:
                                nota=float(input("\nIngrese la nota: "))
                                ponderacion=float(input("Ingrese la ponderacion de la nota: "))
                                suma+= nota*ponderacion
                                suma_ponderacion+=ponderacion
                            else:
                                ponderacion_faltante= 1-suma_ponderacion
                                ultima_nota_presentacion= (4.0-suma) / ponderacion_faltante
                                print(f"La ultima nota para presentar es: {ultima_nota_presentacion}")
                except ValueError:
                    print("Error solo se permiten numeros")
            case "3":
                if nota_presentacion==0:
                    print("Faltan datos. regrese a las otras opciones.")
                else:
                    nota_examen=(4.0-(nota_presentacion*0.6))/0.4
                    print(f"La nota para el examen es: {nota_examen}")
            
            case "4":
                print("Gracias por usar este programa.")
            case _:
                print("'Opción no válida. Por favor ingrese 1, 2, 3 o 4.")