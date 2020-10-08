import pokemon as pok  # Importamos a pokemon que donde se encuentr la class
from utilidades_extra import tirar_dado

# JUEGO DE POKEMON
tipos = "Planta, Fuego, Agua, Tierra"
p1 = pok.Pokemon("Pikachu", 15)  # Creamos nuestros pokemon
p2 = pok.Pokemon("Bulbasaur", 14)
p3 = pok.Pokemon("Charmander", 16)
p4 = pok.Pokemon("Onix", 14)

# Inicializamos los valores y el turno
p1.vida = 100
p2.vida = 100
p3.vida = 100
p4.vida = 100
turno = tirar_dado(2)

while True:
    num1 = input("Ingresa un numero para elegir tu primer Pokemon\n (1) Pikachu."
                 "\n (2) Bulbasaur.\n (3) Charmander.\n (4) Onix\n >>")
    num2 = input("Ingresa otro numero para elegir el Pokemon contrincante\n "
                 "(1) Pikachu.\n (2) Bulbasaur.\n (3) Charmander.\n (4) Onix\n >>")
    f = (print("Ha Iniciado la batalla"))
    print("Es el turno #", turno)
    try:
        if num1 == '1' and num2 == '2':
            print(f"{p1.name} se enfrenta a {p2.name}\n")
        elif num1 == '1' and num2 == '3':
            print(f"{p1.name} se enfrenta a {p3.name}\n")
        elif num1 == '1' and num2 == '4':
            print(f"{p1.name} se enfrenta a {p4.name}\n")
        elif num1 == '2' and num2 == '1':
            print(f"{p2.name} se enfrenta a {p1.name}\n")
        elif num1 == '2' and num2 == '3':
            print(f"{p2.name} se enfrenta a {p3.name}\n")
        elif num1 == '2' and num2 == '4':
            print(f"{p2.name} se enfrenta a {p4.name}\n")
        elif num1 == '3' and num2 == '1':
            print(f"{p3.name} se enfrenta a {p1.name}\n")
        elif num1 == '3' and num2 == '2':
            print(f"{p3.name} se enfrenta a {p2.name}\n")
        elif num1 == '3' and num2 == '4':
            print(f"{p3.name} se enfrenta a {p4.name}\n")
        elif num1 == '4' and num2 == '1':
            print(f"{p4.name} se enfrenta a {p1.name}\n")
        elif num1 == '4' and num2 == '2':
            print(f"{p4.name} se enfrenta a {p2.name}\n")
        elif num1 == '4' and num2 == '3':
            print(f"{p4.name} se enfrenta a {p3.name}\n")
        elif num1 and num2 == '1' or num2 and num1 == '2':
            print("No esta permitido batallar con el mismo pokemon")
        elif num1 and num2 == '3' or num2 and num1 == '4':
            print("No esta permitido batallar con el mismo pokemon")
        while p1.vida > 0 and p2.vida > 0:
            if turno == 1:
                p2.vida = p2.vida - p1.attack
                turno = 2
                print(f"{p1.name} ataca, {p2.name} ahora tiene {p2.vida} de vida")
                print("\n=== PROXIMA RONDA ===")
            else:
                p1.vida = p1.vida - p2.attack
                turno = 1
                print(f"{p2.name} ataca, {p1.name} ahora tiene {p1.vida} de vida")
                print("\n=== PROXIMA RONDA ===")

            # Consultamos si el pokemon 1 perdió
        if p1.vida <= 0:
            p2.gano()
        else:  # Sino significa que el pokemon 1 gano
            p1.gano()

    except ValueError:
        print("Entrada invalida, debe ser un numero")
    finally:
        choice = input("Quieres continuar batallando?\n (1) Para seguir.\n (2) Para salir.\n >>")
        if choice == '2':
            print("Gracias, sigue entrenando")
            break
        else:
            print("Continuamos...")

# if p2.vida <= 0:
#    p1.gano()
# else:
#    p2.gano()

# if p3.vida <= 0:
#    p1.gano()
# else:
#    p3.gano()

# if p4.vida <= 0:
#    p1.gano()
# else:
#    p4.gano()


# TAREA PARA EL ESTUDIANTE
# 1 Agregar un ciclo infinito que nos permita iniciar mas batallas (done)
# 2 Agregar mas pokemons y permitir al usuario elegir cual utilizar (done)
# 3 No pueden usar el mismo pokemon los 2 jugadores
# 4 casi opcional, seria ideal que la clase pokemon estuviera en un modulo
# Opcional:
# Agregar clases a los pokemon (Tierra, Electricidad, Fuego, Agua)
# por ejemplo, si pokemon 1 es de agua, y pokemon 2 es de fuego
# que el pokemon 1 le reste ataque * 1.5
# asi mismo que el pokemon 2 le reste solo ataque menos al 25%
