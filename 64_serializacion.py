# SERIALIZACION
"""
Serializacion es el proceso de convertir un objeto en una secuencia de bytes
para almacenarlo o transmitirlo a la memoria, a una base de datos o a un archivo.
Su proposito principal es guardar el estado de un objeto para poder volver a
crearlo cuando sea necesario. El proceso inverso se denomina deserializacion.

FUENTE: https://docs.microsoft.com/es-es/dotnet/csharp/programing-guide/concepts/serialization/
"""

# PARA SERIALIZAR EN PYTHON UTILIZAREMOS LA LIBRERIA "PICKLE"
import pickle

# 1. SERIALIZAR COLECCIONES
"""estudiantes = [
    "Marcos",
    "Carla",
    "Agustin",
    "Pedro",
    "Maria"
]

archivo_serializado = open("estudiantes", "wb") # Creamos un archivo para guardar el estado

pickle.dump(estudiantes, archivo_serializado) # Volcamos el contenido de la lista en el archivo

archivo_serializado.close()
del archivo_serializado"""

archivo = open("estudiantes", "rb")

lista_estudiantes = pickle.load(archivo)

print(lista_estudiantes)

for e in lista_estudiantes:
    print(e)
# 1. SERIALIZAR OBJETOS

from estudiantes import Estudiantes

"""est1 = Estudiantes("Marcos", 35, "Python")
est2 = Estudiantes("Carla", 20, "JS")
est3 = Estudiantes("Pedro", 26, "C#")

lista_est_obj = [
    est1,
    est2,
    est3
]

arch_est_obj = open("estudiantes_obj", "wb")  # Creamos un archivo para guardar el estado
pickle.dump(lista_est_obj, arch_est_obj)  # Volcamos el contenido de la lista en el archivo

arch_est_obj.close()
del arch_est_obj"""


archivo_est = open("estudiantes_obj", "rb")

lista_estudiantes_obj = pickle.load(archivo_est)

for e in lista_estudiantes_obj:
    print(e.info())
