# VERSION 2.0 DE ADIVINA EL NUMERO

import random

# Variables para modificar el juego
posibilidades = 5
limite = 20

print("Hola, Cómo te llamas?")
name = input()

welcome = ("Muy bien " + name + " estoy pensando un numero entre 1 y " + str(limite) + ", intenta adivinarlo")
print(welcome)
cont = ("a proposito, solo cuentas con " + str(posibilidades) + " posibilidades.")
print(cont)

# Generamos un numero aleatorio entre 1 y 20
adivina = random.randint(1, limite)

intentos = 0

while intentos <= posibilidades:
    numero = int(input("Intenta adivinarlo: "))
    if numero == adivina:
        print("\nGanaste! era el", adivina)
        break
    if intentos == posibilidades - 1:
        print("\nPerdiste! el numero era el", adivina)
        break
    else:
        if numero < adivina and intentos < posibilidades:
            print("Intenta con un numero mas grande.")
        else:
            if numero > adivina and intentos < posibilidades:
                print("Intenta con un numero mas pequeño.")
            intentos += 1
while True:
    print("\nGracias por jugar\nPulsa (1) para jugar de nuevo.\nPulsa (2) para cerrar el juego.")
    volver_jugar = input(">")
    if volver_jugar == "1":
        adivina = random.randint(1, limite)
        intentos = 0
        print(welcome)
        print(cont)
    if volver_jugar == "2":
        print("\nGracias por jugar, hasta la proxima.")
        break
    while intentos <= posibilidades:
        numero2 = int(input("Intenta adivinarlo: "))
        if numero2 == adivina:
            print("\nGanaste! era el", adivina)
            break
        if intentos == posibilidades - 1:
            print("\nPerdiste! el numero era el", adivina)
            break
        else:
            if numero2 < adivina and intentos < posibilidades:
                print("Intenta con un numero mas grande")
            else:
                if numero2 > adivina and intentos < posibilidades:
                    print("Intenta con un numero mas pequeño")
                intentos += 1
