# PROYECTO: Aplicar lo aprendio
# GUARDAR DATOS DE NUESTROS PROGRAMAS

import pickle

# Importamos nuestra clase estudiantes
from estudiantes import Estudiantes as Est


class ListaEstudiantes:
    estudiantes = []

    def __init__(self):
        archestudiantes = open("lista_estudiantes", "ab+")
        archestudiantes.seek(0)  # Lleva el cursor de nuevo al principio

        try:
            self.estudiantes = pickle.load(archestudiantes)
            print(f"{len(self.estudiantes)} estudiantes cargados correctamente del archivo externo")
        except EOFError:
            print("No se han cargado estudiantes previos")
        finally:
            archestudiantes.close()
            del archestudiantes

    def agregarestudiante(self, e):
        self.estudiantes.append(e)
        self.guardarestudiantes()  # Llamamos al metodo que abre el archivo

    def mostrarestudiantes(self):
        for e in self.estudiantes:
            print(e)

    def guardarestudiantes(self):
        archivoest = open("lista_estudiantes", "wb")
        pickle.dump(self.estudiantes, archivoest)
        archivoest.close()
        del archivoest


lista = ListaEstudiantes()

est1 = Est("Benicio", 18, "Go")
est2 = Est("Tiziana", 14, "C#")

lista.agregarestudiante(est1)
lista.agregarestudiante(est2)

lista.mostrarestudiantes()

# TAREA PARA EL ESTUDIANTE
# Mejorar aun mas el juego de Pokemon:
# Una vez que termina una pelea de pokemon, guardar en un archivo externo que pokemon gano
# y sumarle 1 a las batallas ganadas de dicho pokemon
# Al finalizar una batalla nueva, que el programa nos indique cuantas batallas lleva ganadas
# dicho pokemon.
