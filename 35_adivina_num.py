# ADIVINA EL NUMERO 1.0

# Procedemos a importar la libreria random
import random

adivina = random.randint(1, 10)

print("Hola, COmo te llamas? ")
name = input()

print("Muy bien " + name + " estoy pensando un numero entre 1 y 10, intenta adivinarlo")
print("A proposito, solo tienes 3 posibilidades")

num = int(input("Intenta adivinar: "))

if num == adivina:
    print("Ganaste!")
else:
    if num > adivina:
        print("Intenta con un numero mas pequeno")
    else:
        print("Intenta con un numero mas grande")

    print("\nTe quedan 2 intentos")
    num = int(input("Intenta otra vez: "))

    if num == adivina:
        print("Ganaste!")
    else:
        if num > adivina:
            print("Intenta con un numero mas pequeno")
        else:
            print("Intenta con un numero mas grande")

        print("\nTe queda 1 intento")
        num = int(input("Intenta otra vez: "))

        if num == adivina:
            print("Ganaste!")
        else:
            print("Perdiste!")
