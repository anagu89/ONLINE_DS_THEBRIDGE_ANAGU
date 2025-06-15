from utils import *

print("======================================================================================================")
print("||                                                                                                  ||")      
print("||   *   *  *   *  *   *  ****   *  *****      *       ***        ****  *      ***   *****   ***    ||")
print("||   *   *  *   *  **  *  *   *  *  *   *      *      *   *      *      *     *   *    *    *   *   ||")
print("||   *****  *   *  * * *  *   *  *  ****       *      *****      ****   *     *   *    *    *****   ||")
print("||   *   *  *   *  *  **  *   *  *  *  *       *      *   *      *      *     *   *    *    *   *   ||")
print("||   *   *   ***   *   *  *****  *  *   *      *****  *   *      *      *****  ***     *    *   *   ||")
print("||                                                                                                  ||") 
print("======================================================================================================")
print("\nAUTORA: Ana Gutiérrez Méndez")
print("The Bridge, June 2025\n\n\n")

# PASO 7: inicio del juego

salir = False

while not salir:
    print("\n------------------------------------\n")
    print("Selecciona una opción:")
    print("1 - Jugar")
    print("2 - Reglas del juego")
    print("3 - Chiste náutico")
    print("0 - Salir\n")

    try:
        menu = int(input("Selecciona una opción: "))

        if menu == 1:
            print("\n¡Izad las velas mis valientes marineros!")
            salir = True

        elif menu == 2:
                print("""
==============================================================================================
REGLAS DEL JUEGO
            
· Preparación:
    Cada jugador coloca su flota en un tablero oculto. Los barcos se pueden 
    ubicar en vertical u horizontalmente, pero no pueden superponerse.

· Disparos:
    En cada turno, un jugador indica las coordenadas de una casilla del 
    tablero del oponente. 

· Respuesta del oponente:
    Si la casilla indicada es un barco, el oponente responde "Tocado". 
    Si es un barco y la última pieza del buque, el oponente responde "Hundido". 
    Si es agua, el oponente responde "Agua". 

· Hundir una nave:
    Cuando todos los casilleros de un barco han sido tocados, la nave se considera hundida. 

· Ganador:
    El juego termina cuando un jugador ha hundido todas las naves de la flota de su oponente.
==============================================================================================
                """)
        
        elif menu == 3:

            # lista de chistes
            chiste = [
                "Se levanta el telón y se ve una patera llena de pendrives.\n¿Cómo se llama la película?\nMemorias de África.",
                "- ¡Abordad el barco!\nY el barco quedó precioso.",
                "- ¿Qué hace un pez?\n- ¡Nada!",
                "- ¿Cuántas anclas tiene un barco?\n- Once, porque se dice 'eleven anclas'.",
                "- ¿Dónde está el capitán?\n- ¡Por babor!\n- Por babor, ¿dónde está el capitán?",
                "- ¡Mi capitán, el barco se hunde!\n- Pues tiraos a la mar.\n- Y la Mar quedó preñada.",
                "En una taberna pirata, ¿cuál de ellos es de Lepe?\nEl que lleva dos parches."
            ]

            # imprime un chiste aleatorio, pongo -1 porque los índices empiezan en 0
            # ya importé "random" al inicio de programa
            indice_chiste = random.randint(0, len(chiste) -1)
            print("\nCHISTE")  
            print(chiste[indice_chiste])
        
        elif menu == 0:
            print("¡Tierra a la vista! ¡Hasta pronto!")
            input("Pulsa cualquier tecla para salir.")
            exit()          # ya importé la función exit al principio
            
        else:
            print("Selecciona una de las opciones anteriores.")

    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

# PASO 8: crear los jugadores, primero el contrincante y después nosotros

pirata = [
    "Barbanegra",
    "Francis Drake",
    "Jack Sparrow",
    "Capitán Garfio",
    "Willy el tuerto",
    "Luffy D. Monkey",
    "Cristobal Colón",
    "El Desnarigado de Ceuta",
    "Patapalo"
]

# ya importé "random" al inicio de programa
# imprime un pirata aleatorio, pongo -1 porque los índices empiezan en 0

indice_pirata = random.randint(0, len(pirata) -1) 
contrincante = pirata[indice_pirata]
print(f"Tu contrincante es {contrincante}.")

jugador = input("¿Cuál es tu nombre marinero? ")
print(f"¡Que empiece la ballata {jugador}!")

# PASO 9: crear tablero del tamaño deseado de los jugadores

tamano = 0

while tamano < 8:

    try:

        tamano = int(input("\nIntroduce los lados del tablero: "))

        if tamano >= 8:
            tablero = crea_tablero(tamano)
            print(f"\n=== HUNDIR LA FLOTA ===\nTablero de juego: {tamano}x{tamano} \n")
            
        else:
            print(f"Tablero demasiado pequeño. Crea con más de {tamano} casillas, por favor.\n¡Al menos 8!")

    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

tablero_jugador = tablero       # ambos tableros miden lo mismo
tablero_contrincante = tablero

# selecciono si quiero ver el tablero del contrincante durante la partida
while True:
    ver_tablero_contrincante = input(f"¿Quieres ver el tablero de {contrincante} durante la partida?")
    ver_tablero_contrincante = ver_tablero_contrincante.lower().strip()  # .strip() para quitar los espacios

    if ver_tablero_contrincante == "si":
        print(f"Sí, necesito ayuda contra {contrincante}.\n")
        ver_tablero_contrincante = True
        break
    
    elif ver_tablero_contrincante == "no":
        print(f"No, no pienso hacer trampas contra {contrincante}.\n")
        ver_tablero_contrincante = False
        break
    
    else:
        print(f"Por favor {jugador}, responde si o no.\n")

if ver_tablero_contrincante == True:
    print(f"\nTablero de {contrincante}\n\n{tablero_contrincante}\n\n")

print(f"\nTablero de {jugador}\n\n{tablero_jugador}\n\n")

# PASO 10: colocar los buques
# coloco 6 barcos para el contrincante aleatoriamente 

print(f"\nColoquemos lo buques de {contrincante}")
print(f"_______________________________________\n")
tablero_contrincante = (crea_barco_aleatorio(tablero_contrincante, eslora = 2, mostrar_proceso = ver_tablero_contrincante))   # 3 barcos de 2m eslora
tablero_contrincante = (crea_barco_aleatorio(tablero_contrincante, eslora = 2, mostrar_proceso = ver_tablero_contrincante))
tablero_contrincante = (crea_barco_aleatorio(tablero_contrincante, eslora = 2, mostrar_proceso = ver_tablero_contrincante))
tablero_contrincante = (crea_barco_aleatorio(tablero_contrincante, eslora = 3, mostrar_proceso = ver_tablero_contrincante))   # 2 naves de 3m eslora
tablero_contrincante = (crea_barco_aleatorio(tablero_contrincante, eslora = 3, mostrar_proceso = ver_tablero_contrincante))
tablero_contrincante = (crea_barco_aleatorio(tablero_contrincante, eslora = 4, mostrar_proceso = ver_tablero_contrincante))   # 1 buque de 4m de eslora

if ver_tablero_contrincante == True:
    print(f"\nTablero de {contrincante}\n\n{tablero_contrincante}\n\n")
else:
    print(f"\nTablero de {contrincante} preparado.")


# coloco 6 barcos para el jugador de forma manual o aleatoria

while True:
    manual = input(f"¿Quieres colocar tus buques manualmente?")
    manual = manual.lower().strip()
    
    if manual == "si":
        print(f"Sí, colocaré mis buques manualmente.\n")
        manual = True
        break
    
    elif manual == "no":
        print(f"No, estoy demasiado débil. Colócalos de forma aleatoria.\n")
        manual = False
        break
    
    else:
        print(f"Escribe bien {jugador}, ¿o es que tienes aceite en las manos?\n")

print(f"\nColoquemos lo buques de {jugador}")
print(f"_______________________________________\n")

for eslora in [2, 2, 2, 3, 3, 4]: # <--- para no tener que estar copia y pega todo el rato
    
    if manual:
        tablero_jugador = crea_barco_manual(tablero_jugador, eslora = eslora)
    else:
        tablero_jugador = crea_barco_aleatorio(tablero_jugador, eslora = eslora, mostrar_proceso = True)

print(f"\nTablero de {jugador}\n\n{tablero_jugador}\n\n")

# PASO 11: turnos
# selecciono qué jugador empieza primero. Si turno = True empezamos, si es False empieza la máquina

print(f"¿Qué pirata comienza la partida? (escribe un número)\n1 - {jugador}\n2 - {contrincante}\n")

while True:

    try:
        turno = int(input())  

        if turno == 1:
            turno = True
            print(f"\n{jugador} comenzará la partida.\n")
            break

        elif turno == 2:
            turno = False
            print(f"\n{contrincante} comenzará la partida.\n")
            break

        else:
            print("Escribe un número válido, ¿o es que llevas un garfio?")
            continue

    except ValueError:
        print("Escribe un número válido, ¿o es que llevas un garfio?")
        continue

# PASO 12: 
# preguntar al tablero si tiene O (barcos) en alguna posición
# retorna True cuando encuentre un barco y False cuando no haya o esté hundido
# print(tablero_jugador == "O") <--- si quiero imprimir el tablero indicando los barcos

game_over_jugador = not np.any(tablero_jugador == "O")
game_over_contrincante = not np.any(tablero_jugador == "O")

# PASO 13: ataque

while True:

    if not np.any(tablero_jugador == "O"):          # veo si me quedan barcos para seguir jugando
        print(f"GAME OVER\n{jugador} se perdió en el Pacífico.")
        input("Pulsa cualquier tecla para salir.")
        break 

    if not np.any(tablero_contrincante == "O"):     # veo si al contrincante le quedan barcos para seguir jugando
        print(f"YOU WIN\n{contrincante} naufragó en una isla desierta.")
        input("Pulsa cualquier tecla para salir.")
        break 

    # si es el turno del jugador (turno = True)
    if turno:
        print(f"Es el turno de {jugador}.\n")

    while turno:
        print("Escribe las coordenadas:")

        try:
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
        
        except ValueError:
            print(f"Escribe sólo números del 1 al {tamano}\n")
            continue
            
        if not (1 <= fila <= tamano) or not (1 <= columna <= tamano):
            print(f"({fila},{columna})")
            print("\nEscribe un número válido, ¿o es que llevas un garfio?\n")
            continue

        print(f"({fila},{columna})")
        acierto = disparar(tablero_contrincante, (fila -1, columna -1))
            
        print(f"\nTablero de {contrincante}\n{tablero_contrincante}\n\n")

        if not acierto:
            turno = False  # fin del turno del jugador si ha fallado
        break

    # veo otra vez si al contrincante le quedan barcos para seguir jugando
    # si no lo hago le estaría dando un turno más teniendo todos los barcos hundidos!!

    if not np.any(tablero_contrincante == "O"):          
        print(f"YOU WIN\n{contrincante} naufragó en una isla desierta.")
        input("Pulsa cualquier tecla para salir.")
        break    

    # si es el turno del contrincante (turno = False)
    if not turno:
        print(f"Es el turno de {contrincante}.\n")

        fila = random.randint(1, tamano)
        columna = random.randint(1, tamano)
        
        print(f"({fila},{columna})")
        acierto = disparar(tablero_jugador, (fila - 1, columna -1))
        
        print(f"\nTablero de {jugador}\n{tablero_jugador}\n\n")

        if not acierto:
            turno = True  # fin del turno del contrincante si ha fallado
    
    # veo otra vez si me quedan barcos para seguir jugando
    # si no lo hago tendría un turno más teniendo todos mis barcos hundidos!!

    if not np.any(tablero_jugador == "O"):
        print(f"GAME OVER\n{jugador} se perdió en el Pacífico.")
        input("Pulsa cualquier tecla para salir.")
        break