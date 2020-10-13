class Estudiantes:
    def __init__(self, nombre, edad, curso_inicial):
        self.name = nombre
        self.age = edad
        self.grade = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

        print(f"Se ha creado un estudiante llamado {self.name}")

    def desactivar(self):
        self.esta_activo = False

    def info(self):
        print(f"Estudiante: {self.name}\nEdad: {self.age}\nActivo: {self.esta_activo}\n")

    def __str__(self):
        return f"{self.name}, {self.age} años"
