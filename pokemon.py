# Clase Pokemon

class Pokemon:  # Creamos la clase Pokemon
    def __init__(self, name, attack):
        self.name = name  # Le asignamos el atributo
        self.attack = attack
        self.vida = 100

    def gano(self):
        print(f"{self.name} GANO ESTA BATALLA!!!")
        print("Mas suerte en tu proxima  vez!!!\n")
