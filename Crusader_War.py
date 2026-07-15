from time import sleep
from random import randint
print("+" *80)
print("siglos XI y XIII (1095-1292)")
print("+" *80)
sleep (1)
print("Antioquía, el ultimo aguante de los cristianos para mantenr la tierra santa\n"
"eres uno de los soldados si es que se te puede nombrar asi.\nUna lanza, un kit medico basico de uso rapido, ropa de tela, casco de cuero y botas\n"
"fueron todo lo que te entregaron antes de partir a la guerra junto a mas de 40.000 hombres igual de prepardos que tu.")
print("+" *80)
sleep(4)
print("Resides junto a otro peloton de campesinos creyentes a las afueras de la ciudad amurallada.\n"
"Escuchando los resos y gritos del general a caballo delate de ti antes de empezar el asedio a la ciudad.\n"
"El ariete derriba la puerta y entras con el monton de campesinos enardecidos por la fe adentro de la ciudad.")
print("+" *80)
sleep(3)
print("_+_" *40)
print("Alcanzas a avanzar entre la multitud de soldados y te encuentras de frente con un soldado rezagado\n"
"El soldado enemigo se pone en posicion, notandose mucho mas preparado que tu gracias a su armadura y sable.")
print("_+_" *40)
vida_jugador=100
vida_cpu=100
dado_jugador=20
dado_enemigo=10
Valor_Item_Curativo=20
cant_Item_Curativo=1
valor_minimo_ataque1=2
valor_minimo_ataque2=15
valor_minimo_ataque3=9
contador_turnos=0
while True:
    print(f"vida jugador: {vida_jugador} puntos \t\t\t vida enemigo: {vida_cpu} puntos \n")
    print("Menu principal")
    print("1.- Patada.")
    print("2.- Estocada con lanza.")
    print("3.- golpear el asta.")
    print("4.- Kit medico de un uso. ")
    try:
        opcion = int(input("Seleccione una accion: "))
    except:
        print("="*30)
        print("Ingrese un numero valido")
        print("="*30)
        continue
    match opcion: 
        case 1:
            lanzamiento= randint(1, dado_jugador)
            contador_turnos=contador_turnos+1
            if lanzamiento >= valor_minimo_ataque1:
                daño =10
                vida_cpu-=daño#vida_cpu0vida_cpu-daño
                print("*"*80)
                print("Te lanzas hacia adelante con una patada en el pecho del enemigo con todo el peso de tu cuerpo\n"
                "Tiras al enemigo al piso y aprovechas para insultarlo\n"
                "El enemigo se recompone moviendo su sable de un lado a otro quitandote de encima\n"
                "Vuelves a tu posicion inicial mientras ves al enemigo levantarse.")
                print("*"*80)
                sleep(3)
            else:
                print("/"*80)
                print("Te intentas lanzar hacia adelante con una patada, pero el enemigo te bloquea y aguanta el golpe\n"
                "En cambio con un movimiento de su sable te da un corte en la pierna obligandote a retroceder apurado.")
                print("/"*80)
                daño=10
                vida_jugador-=daño
                sleep(3)
        case 2:
            contador_turnos=contador_turnos+1
            lanzamiento= randint(1, dado_jugador)
            if lanzamiento >= valor_minimo_ataque2:
                daño =25
                vida_cpu-=daño
                print(">"*80)
                print("Bajas tu lanza y te colocas en posicion de embestida hacia el enemigo\n"
                "Te abalanzas contra el sujeto delante de ti y le atraviezas un costado, sin darle en puntos vitales\n"
                "Aprovechando que le diste retrocedes para reposicionarte y pensar como continuar.")
                print(">"*80)
                sleep(3)
            else:
                print("/"*80)
                print("Al lanzarte hacia adelante con la lanza el enmigo la esquiba y la agarra desde el asta\n"
                "Te acerca a el y recibes de lleno un corte en tu costado, atraveando tu uniforme improvisado de soldado\n"
                "Rapidamente tiras de la lanza para recuperarla y retirarte.")
                print("/"*80)
                daño= 25
                vida_jugador-=daño
                sleep(3)
        case 3:
            contador_turnos=contador_turnos+1
            lanzamiento= randint(1, dado_jugador)
            if lanzamiento >= valor_minimo_ataque3:
                daño =15
                vida_cpu-=daño
                print("="*80)
                print("Tomas tu lanza desde la mitad y te acercas al soldado\n"
                "Balanceas tu arma de un lado a otro y golpeas al enemigo en un costado y los brazos\n"
                "Aprovechando que esta aturdido retrocedes antes de que pueda tomar replecarias.")
                print("="*80)
                sleep(3)
            else:
                print("*"*80)
                print("Antes de que el mango de tu arma golpe la cabeza de tu enemigo este lo agarra y lo detiene\n"
                "El aprovecha que te acercaste y te da un puchetaso de lleno en el estomago y el costado\n"
                "Retrocedes apurado esquivando por poco un golpe que iba a tu cabeza.")
                print("*"*80)
                daño= 10
                vida_jugador-=daño
                sleep(3)
        case 4:
            contador_turnos=contador_turnos+1
            if Valor_Item_Curativo<=0:
                print("X-"*40)
                print("Ya usaste tu kit medico de un uso, cuenta como turno usado...")
                print("X-"*40)
            elif Valor_Item_Curativo>=1:                    
                vida_jugador+=Valor_Item_Curativo
                print(" \u2764\uFE0F "*40)
                print("Le das un uso a tu kit basico de primeros auxilios, que consta de vendajes, una masilla de hiervas curativas,\n"
                "y unas pildoras a las que el general les nombro Matadolores, y efectibamente todo el dolor ceso y con los vendajes el sangrado se detubo\n"
                "Te reincorporas y con fuerza renovada te preparas para seguir con la pelea, encomendando tu alma a dios...")
                print(" \u2764\uFE0F "*40)
                Valor_Item_Curativo-=20
                sleep(3)
        case _:
            print("Opcion no valida \n")
    lanzamiento_enemigo= randint(1, dado_enemigo)
    if lanzamiento_enemigo >= 10:
        print("#"*80)
        print("El enemigo toma su sable y se lanza contra ti con un golpe contundente\n"
        "con un movimiento agil te corta el pecho atravesando tu armadura de cuero\n"
        "retrosede para reposicionarce...")
        daño=25
        vida_jugador-=daño
        print("#"*80)
    elif lanzamiento_enemigo >= 6 and lanzamiento_enemigo <= 9 :
        print("#"*80)
        print("El soldado se acerca a ti preparando su ataque\n"
        "desenvaina su sable y con el pomo del mismo te golpea la frente y el costado\n"
        "al mismo tiempo que te tambaleaz este retrocede...")
        daño=10
        vida_jugador-=daño
        print("#"*80)
    elif lanzamiento_enemigo >= 3 and lanzamiento_enemigo <= 5 :
        print("#"*80)
        print("El enemigo se apresura en atacarte\n"
        "sin tiempo para sacar su espada te da un puñetazo en el estomago\n"
        "enojado este retrocede...")
        daño=5
        vida_jugador-=daño
        print("#"*80)
    else:
        print("#"*80)
        print("El enemigo se queda en su sitio insultandote y maldiciendote en su lengua natal...")
        print("#"*80)
    
    if vida_jugador<=0:
        print(":( "*14)
        print("Mueres contra el soldado, DERROTA.//")
        print(f"Tu partida termino en el turno: {contador_turnos}//")
        print(":( "*14)
        break

    elif vida_cpu<=0:
        print(":) "*14)
        print("El soldado cae muerto al piso desangrado, VICTORIA...//")
        print(f"Tu batalla termino en el turno: {contador_turnos}   //")
        print(":) "*14)
        while True:
            print("<>"*30)
            print("La pelea contra el soldado enemigo termino... el polvo de la batalla circundante se disipa...\n"
            "atraviesas el campo de batalla junto a algunos campesinos y llegas al centro de la ciudad\n"
            "te encuentras con todos los soldados aliados restantes rodeando a un solo hombre... el general enemigo.")
            print("<>"*30)
            sleep(3)
            print("<>"*30)
            print("El general con una armadura dorada y una gran espada girtando para que se acerque el mejor rival...\n"
            "sin dudar de entre la multitud te adelantas... tu un don nadie que casi muere contra un soldado cualquiera retando al general\n"
            "levantas tu lanza y preparas tu casco y te pones en posicion mientras el general se burla de ti...")
            print("<>"*30)
            sleep(3)
            print("<>"*30)
            print("Te pones en posicion sintiendo la adrenalina en tu cuerpo y al imponente general")
            print("<>"*30)
            vida_jugador=100
            vida_cpu_jefe=150
            dado_jugador=20
            dado_enemigo=10
            valor_minimo_ataque1=2
            valor_minimo_ataque2=15
            valor_minimo_ataque3=9
            while True:#While true crea un siclo infinito hasta que se use el comando Break.
                print(f"vida jugador: {vida_jugador} puntos \t\t\t vida General: {vida_cpu_jefe} puntos \n")
                print("Menu principal")
                print("1.- Patada.")
                print("2.- Estocada con lanza.")
                print("3.- golpear el asta.")
                print("4.- Kit medico de un uso. ")
                try:
                    opcion_2=int(input("Seleccione una accion (1-2-3-4): "))
                except:
                    print("="*30)
                    print("Ingrese un numero valido")
                    print("="*30)
                    continue
                match opcion_2:
                    case 1:
                        lanzamiento= randint(1, dado_jugador)
                        contador_turnos=contador_turnos+1
                        if lanzamiento >= valor_minimo_ataque1:
                            daño =10
                            vida_cpu_jefe-=daño
                            print("*"*80)
                            print("Te impones contra el general y le haces un barrido tirandolo al piso \n"
                            "aprovechas y lo golpeas con el pomo de la lanza antes de que se levante \n"
                            "el general al ponerse de pie te pones a lerta y retocedes...")
                            print("*"*80)
                            sleep(3)
                        else:
                            print("/"*80)
                            print("El general resiste la patada y te golpea con la parte plana de su espada en un costado\n"
                            "con dolor retrocedes agradecido de  que fue solo con la parte sin filo...")
                            print("/"*80)
                            daño=10
                            vida_jugador-=daño
                            sleep(3)
                    case 2:
                        lanzamiento= randint(1, dado_jugador)
                        contador_turnos=contador_turnos+1
                        if lanzamiento >= valor_minimo_ataque2:
                            daño =25
                            vida_cpu_jefe-=daño
                            print(">"*80)
                            print("Te avalanzas contra el general y le clavas en un costado la lanza\n"
                            "le retuerces la punta de tu arma en su herida antes de retroceder... haz que sufra.")
                            print(">"*80)
                            sleep(3)
                        else:
                            print("/"*80)
                            print("Te intentas lanzar hacia adelante con la lanza pero el general te interrumpe\n"
                            "agarra la lanza y te da un fuerte golpe en la cabeza con el pomo de su espada\n"
                            "aturdido y con sangre en la frente retrocedes...")
                            print("/"*80)
                            daño=15
                            vida_jugador-=daño
                            sleep(3)                        
                    case 3:
                        lanzamiento= randint(1, dado_jugador)
                        contador_turnos=contador_turnos+1
                        if lanzamiento >= valor_minimo_ataque3:
                            daño =15
                            vida_cpu_jefe-=daño
                            print("="*80)
                            print("Golpeas al general con el asta de tu lanza\n"
                            "dos golpes contundentes en la cabeza y en la pierna...")
                            print("="*80)
                            sleep(3)
                        else:
                            print("/"*80)
                            print("Antes de que el asta golpee al general este la bloquea\n"
                            "te devuelve el golpe con un gancho izquierdo y te deja tambaleando y te obliga a retroceder...")
                            print("/"*80)
                            daño=10
                            vida_jugador-=daño
                            sleep(3)
                    case 4:
                        contador_turnos=contador_turnos+1
                        if Valor_Item_Curativo<=0:
                            print("X-"*40)
                            print("Ya usaste tu kit medico de un uso, cuenta como turno usado...")
                            print("X-"*40)
                        elif Valor_Item_Curativo>=1:                    
                            vida_jugador+=Valor_Item_Curativo
                            print(" \u2764\uFE0F "*40)
                            print("Usas tu Kit medico que no usaste durante tu otra pelea...\n")
                            print(" \u2764\uFE0F "*40)
                            Valor_Item_Curativo-=20
                            sleep(3)
                    case _:
                        print("Opcion no valida \n")
                lanzamiento_enemigo= randint(1, dado_enemigo)
                if lanzamiento_enemigo >= 10:
                    print("#"*80)
                    print("El general intrepido se lanza contra ti dando dos espadazos hacia adelante...\n"
                    "alcanzas a esquivar uno pero el segundo te dio de lleno...")
                    daño=30
                    vida_jugador-=daño
                    print("#"*80)
                elif lanzamiento_enemigo >= 6 and lanzamiento_enemigo <= 9 :
                    print("#"*80)
                    print("Un simple golpe de la espada del general fue suficiente  para hacerte retroceder herido\n"
                    "te palapas la herida y retrocedes...")
                    daño=20
                    vida_jugador-=daño
                    print("#"*80)
                elif lanzamiento_enemigo >= 3 and lanzamiento_enemigo <= 5 :
                    print("#"*80)
                    print("El general enemigo se acerca y te golpea con el lado sin filo de su espada\n"
                    "esto te duele pero agradeces que no fue letal...")
                    daño=15
                    vida_jugador-=daño
                    print("#"*80)
                else:
                    print("#"*80)
                    print("El general se queda en su sitio sin hacer nada...\n"
                    "no grita no insullta ni se rie... solo te observa con pasiencia.")
                    print("#"*80)

                if vida_jugador<=0:
                    print(":( "*14)
                    print("Mueres contra el General, DERROTA... Antioquia no fue conquistada...//")
                    print(f"Tu partida termino en el turno: {contador_turnos}//")
                    print("Precione cualquier tecla para salir")
                    print(":( "*14)
                    exit()
                elif vida_cpu_jefe<=0:
                    print("\U00002B50 "*14)
                    print("El general murio... Los soldados enemigos se rinden... "
                    "Antioquia fue conquistada... VICTORIA.//")
                    print("\U00002B50 "*14)
                    sleep(2)
                    print("+"*30)
                    print("Caes de rodillas cansado... todos los demas soldados, campesinos y generales aliados gritan y celebran\n"
                    "mientras que tu sientes el cuerpo cansado... las heridas ya no te duelen... y sientes la sangre correr por tu frente")
                    print("+"*30)
                    sleep(3)
                    print("+"*30)
                    print("Sientes los parpados cansados y la respiracion se hace lentamente mas leve...\n"
                    "agarras con fuerza tu cruz de madera que llevas en el cuello como relicario...\n"
                    "desides cerrar los ojos y descansar....")
                    print("+"*30)
                    sleep(3)
                    print("\U0001F31F "*20)
                    print(F"Tu partida termino en el turno: {contador_turnos}")
                    print("Precione cualquier tecla para salir :)")
                    print("\U0001F31F "*20)
                    exit()