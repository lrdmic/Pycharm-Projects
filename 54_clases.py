# CLASES Y OBJETOS

class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

    def desactivar(self):  # Metodo desactivar
        self.esta_activo = False

    def add_cursos(self, curso):  # Metodo para anadir cursos
        self.curso_inicial.append(curso)

    def remove_cursos(self, quitar_curso):  # Metodo para remover cursos
        self.curso_inicial.remove(quitar_curso)


estudiante1 = Estudiante("Marcos", 35, "Python")

print(estudiante1.cursos)


class Computadora:
    def __init__(self, monitor, disco_duro, memoria, video_card, motherboard,
                 procesador, case, bocinas, teclado, mouse):
        self.monitor = monitor
        self.disco_duro = disco_duro
        self.memoria = memoria
        self.video_card = video_card
        self.motherboard = motherboard
        self.procesador = procesador
        self.case = case
        self.bocinas = bocinas
        self.teclado = teclado
        self.mouse = mouse

# TAREA PARA EL ESTUDIANTE.
# Crear 2 metodos:
# 1 que permita anadir cursos a los que el estudiante se ha inscrito
# 2 otro metodo que permita eliminar cursos del estudiante
