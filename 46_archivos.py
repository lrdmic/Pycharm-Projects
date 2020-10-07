# ARCHIVOS (de texto)

# Abrir y Cerrar archivos

# w - me crea otro archivo en blanco o con lo que yo le escriba
# a - me agrega texto al final, por supuesto que tengo que decirle que texto
# w+ - permite escribir y leer, pero elimina todo lo anterior
# r+ - permite escribir, pero sobreescribe el contenido al principio


arch_students = open("estudiantes.txt", "a")  # Asi abrimos un archivo
print(arch_students.write("\nCarolina Massutti - ReactJS"))
arch_students.close()  # Asi cerramos un archivo

# Eliminar un archivo, como esta en la carpeta del proyecto, solo se pone el nombre
import os

os.remove("estudiantes2.txt")
