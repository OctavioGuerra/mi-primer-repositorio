def ingresar_notas_y_ponderaciones(cantidad_notas):
                    lista_notas=[]
                    lista_ponderaciones=[]
                    for i in range(cantidad_notas):
                        while True:
                            nota=float(input(f"Ingrese la nota {i+1}: "))
                            if nota <1 or nota >7:
                                print("Error, la nota no debe ser menor a 1 ni mayor a 7")
                                continue
                            ponderacion=float(input(f"Ingrese la ponderacion {1+i}: "))
                            if ponderacion<0 or ponderacion>1:
                                print("Error, la ponderacion debe ser mayor a 0 y menor a 1.")
                                continue
                            lista_ponderaciones.append(ponderacion)
                            lista_notas.append(nota)
                            break
                    return lista_notas,lista_ponderaciones

def calcular_nota_presentacion(lista_notas, lista_ponderaciones):
    nota_ponderada=0
    for i in range (len(lista_notas)):
        nota_ponderada+=lista_notas[i]*lista_ponderaciones[i]
    print(f"Nota ponderada: {nota_ponderada:.2f}")
    return nota_ponderada
        
def calcular_nota_necesaria_examen(nota_ponderada, ponderacion_nota_faltante):
    nota_faltante =(4.0-nota_ponderada)/ ponderacion_nota_faltante
    return nota_faltante

opc=0
lista_notas=[]
lista_ponderaciones=[]
nota_faltante=0
while opc!=4:
    print("===CALCULADORA DE NOTAS===")
    print("1. iNGRESAR NOTAS Y PONDERACION.")
    print("2. CALCULAR NOTA DE PRESENTAION.")
    print("3. CALCULAR NOTA NECESARIA PARA EXAMEN.")
    print("4. SALIR DEL PROGRAMA.")
    try:
        opc=int(input("Ingrese una opcion(1/4): "))
        match opc:
            case 1:
                cantidad_notas=int(input("Ingrese la canidad de notas: "))
                lista_notas, lista_ponderaciones=ingresar_notas_y_ponderaciones(cantidad_notas)
                
            case 2:
                if len(lista_notas)==0:
                    print("Primero debe ingresar las notas.")
                else:
                    calcular_nota_presentacion(lista_notas, lista_ponderaciones)
                
            case 3:
                if len(lista_notas) == 0:
                    print("Primero debe ingresar las notas.")
                else:
                    try:
                        ponderacion_nota_faltante = float(input("Ingrese la ponderación de la nota faltante: "))
                        nota_ponderada = calcular_nota_presentacion(lista_notas,lista_ponderaciones)
                        nota_faltante = calcular_nota_necesaria_examen(nota_ponderada,ponderacion_nota_faltante)
                        print(f"Necesita obtener un {nota_faltante:.2f}")
                    except ValueError:
                        print("Error, ingresó un valor no válido.")
            case 4:
                print("Gracias por usar el programa.")
            case _:
                print("Error, opcion no valida")

    except ValueError:
        print("ERROR.")
