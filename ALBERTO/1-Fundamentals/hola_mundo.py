print("Hola bootcamp")

# ============================================

from random import randint
random_number = randint(1,5)

vidas = 2

while vidas != 0:
    valor = int(input("Dime un número: "))
    print("\nTu número elegido es: ", valor)

    if (valor == random_number):
        print("You win")
        break 

    elif valor != random_number:
        vidas = vidas - 1
        print("Te quedan", vidas, "vidas")
    
print("You lose")