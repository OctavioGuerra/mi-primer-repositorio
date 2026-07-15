corta=0
larga=0
while True:
    try:
        N_palabras=int(input("Ingrese la cantidad de palabra: "))
    except ValueError:
        print("Error, Debe ingresar un numero entero.")
        continue
    if N_palabras <=0:
        print("Debe ingresar una cantidad mayor a cero.")
        continue
    else:
        break
for i in range (N_palabras):
    while True:
        Palabra=input(f"Ingrese la palabra numero {1+i}: ")
        if len(Palabra)<2:
            print("La palabra debe tener al menos 2 letras.")
        else:
            break
    if len(Palabra)>6:
        print("Palabra larga.")
        larga +=1
    else:
        print("Palabra corta.")
        corta +=1
print("Resultados.") 
print(f"Palabras largas: {larga}")
print(f"Palabras Cortas: {corta}")   