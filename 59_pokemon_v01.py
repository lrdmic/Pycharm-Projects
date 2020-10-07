from utilidades_extra import tirar_dado
# JUEGO DE POKEMON


class Pokemon:  # Creamos la clase Pokemon
    def __init__(self, name, attack):
        self.name = name  # Le asignamos el atributo
        self.attack = attack
        self.vida = 100

    def gano(self):
        print(f"{self.name} GANO ESTA BATALLA!!!")
        print("Mas suerte en tu proxima  vez!!!")


p1 = Pokemon("Pikachu", 15)  # Creamos nuestros pokemon
p2 = Pokemon("Bulbasur", 14)
p3 = Pokemon("Charmander", 16)

# Inicializamos los valores y el turno
p1.vida = 100
p2.vida = 100
turno = tirar_dado(2)

print("Ha Iniciado la batalla")
print(f"{p1.name} se enfrenta a {p2.name}\n")

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
else:   # Sino significa que el pokemon 1 gano
    p1.gano()

# TAREA PARA EL ESTUDIANTE
# 1 Agregar un ciclo infinito que nos permita iniciar mas batallas
# 2 Agregar mas pokemons y permitir al usuario elegir cual utilizar
# 3 No pueden usar el mismo pokemon los 2 jugadores
# 4 casi opcional, seria ideal que la clase pokemon estuviera en un modulo
# Opcional:
# Agregar clases a los pokemon (Tierra, Electricidad, Fuego, Agua)
# por ejemplo, si pokemon 1 es de agua, y pokemon 2 es de fuego
# que el pokemon 1 le reste ataque * 1.5
# asi mismo que el pokemon 2 le reste solo ataque menos al 25%
