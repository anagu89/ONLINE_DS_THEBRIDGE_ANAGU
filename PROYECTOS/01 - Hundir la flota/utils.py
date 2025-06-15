# PASO 1: importar las librerías necesarias como numpy para los arrays del tablero
# y poner una bonita cabecera de juego :)

import numpy as np          # para crear el array del tablero
import random               # para los barcos, chistes y piratas
from sys import exit        # para poder salir del juego al meter un 0 - EXIT

# PASO 2: función para crear el tablero
# si lo quiero de tamaño pongo "lado = 10" (10x10) o como yo quiera
# en este caso, lo haremos como queramos de grande en el PASO 9

def crea_tablero(lado):                   
    tablero = np.full((lado,lado)," ")
    return tablero

# PASO 3: reglas para colocar barcos

def coloca_barco_plus(tablero, barco, mostrar_proceso):
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]        # calcula el número de filas que tiene el tablero        
    num_max_columnas = tablero.shape[1]     # calcula el número de columnas
    
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]

        if fila < 0  or fila >= num_max_filas:
            if mostrar_proceso:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero.")
                return False
        
        if columna < 0 or columna >= num_max_columnas:
            if mostrar_proceso:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero.")
                return False
        
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            if mostrar_proceso:
                print(f"No puedo poner la pieza {pieza} porque hay otro barco.")
                return False
        
        tablero_temp[pieza] = "O"

    return tablero_temp

# PASO 4: funcion para colocar los barcos

# modo aleatorio

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100, mostrar_proceso = True):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    while True:
        barco = []          # construimos el supuesto barco
        pieza_original = (random.randint(0,num_max_filas - 1), random.randint(0, num_max_columnas - 1))
        if mostrar_proceso:
            print("Pieza original:", pieza_original)
        
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        if mostrar_proceso:
            print("Con orientacion", orientacion, "\n")
        
        fila = pieza_original[0]
        columna = pieza_original[1]
        
        for i in range(eslora - 1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1 #== "O"
            pieza = (fila,columna)
            barco.append(pieza)
        
        tablero_temp = coloca_barco_plus(tablero, barco, mostrar_proceso)
        
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        
        if mostrar_proceso:
            print("Tengo que intentar colocar otro barco.\n")

# modo manual

def crea_barco_manual(tablero, eslora=4, num_intentos=100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    print(f"\nColoca el buque de {eslora}m de eslora.")

    while True:
                
        try:
            fila = input(f"Fila: ").strip()
            columna = input(f"Columna: ").strip()

            if not (fila.isdigit() and columna.isdigit()):      # compruebo que son números enteros
                print("Solo se permiten números, marinero de agua dulce.\n")
                continue

            fila = int(fila)
            columna = int(columna)

            if not (0 <= fila < num_max_filas) or not (0 <= columna < num_max_columnas):    # ver que no me he salido
                print(f"¡Te saliste del tablero rata de sentina!\n")
                continue

            pieza_original = (fila, columna)

        except:
            print(f"Sigue fallando y te tiramos al agua.\n")
            continue

        orientacion = input("¿En qué dirección irá el barco? (N/S/E/O): ").upper().strip()
        
        if orientacion not in ["N", "S", "E", "O"]:
            print("¿Necesitas una brújula para colocarlos bribón?\n")
            continue

        barco = [pieza_original]
        fila = pieza_original[0]
        columna = pieza_original[1]

        for i in range(eslora - 1):
            if orientacion == "N":
                fila -= 1
            elif orientacion == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            elif orientacion == "O":
                columna -= 1

            pieza = (fila, columna)
            barco.append(pieza)       

        fuera_rango = False      # compruebo si el barco está dentro del tablero
        for fila, columna in barco:
            if not (0 <= fila < num_max_filas) or not (0 <= columna < num_max_columnas):
                fuera_rango = True
                break

        if fuera_rango:
            print("La Tierra es plana y tu barco desborda. Intenta de nuevo.\n")
            continue

        tablero_temp = coloca_barco_plus(tablero, barco, mostrar_proceso = True)     # intento colocarlo
        
        if type(tablero_temp) == np.ndarray:
            print("Barco colocado correctamente en la mar.\n")
            print(tablero_temp)
            return tablero_temp

        print("Si pones el barco encima de otro hundes la nave.\n")

# PASO 5: reglas para recibir un disparo
# sustituyo O por X si acierto y O por - si cae en agua

def disparar(tablero, coordenada):

    if tablero[coordenada] == "O":          # si aciero en un barco (O)
        tablero[coordenada] = "X"           # entonces lo hundo (X)
        print("\nTocado\n")
        return True                         # me devuelve True si acierto, para volver a disparar
    
    elif tablero[coordenada] == "X":        # si ya está hundido (X)
        print("\nHundido\n")
        return False
    
    else:
        tablero[coordenada] = "-"           # si disparo al agua (-): == "-"
        print("\nAgua\n")
        return False

# PASO 6: creo una función para reparar todos los buques al final de la partida
# funciona buscando los barcos hundidos (X) y los sustituye por barcos (O)
# hago lo mismo para los disparos al agua y quitar los (-)

def arregla_barcos(tablero):
    tablero[tablero == "X"] = "O"                   # así buscamos si hay X ó O
    #tablero.where(tablero == "X","O", tablero)     # esto es un método de numpy que se podría usar también
    tablero[tablero == "-"] = " "
    return tablero

# print(arregla_barcos(tablero)) <-------- pondría esto para reiniciar el juego