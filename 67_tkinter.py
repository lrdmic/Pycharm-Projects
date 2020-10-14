# INTERFACES GRÁFICAS CON PYTHON Y TKINTER

# CLASE 01 - Introducción y Raiz

# Historia de TKinter: https://guia-tkinter.readthedocs.io/es/develop/chapters/1-intro/1.1-About_Tk.html
# Link a la documentación oficial: https://docs.python.org/3/library/tk.html

"""
EXPLICACIÓN RÁPIDA DE ALGUNOS COMPONENTES
Tk -    Es el contenedor de todos los elementos (widgets) que tendrá nuestra
interfaz.
        Además es al que llamaremos Raiz o Root. Su tamaño puede definirse o
ser modificable.

Frame - El Frame o Marco es por sí mismo un widget aunque no nos permita
        interactuar con el programa.
        El marco será el contenedor de los widgets que utilicemos.

Label - Es un widget en el que podemos mostrar textos estáticos.

Entry - Cuadro de texto para ingresar textos cortos (una sola linea).

Text -  Este widget nos permite escribir textos largos (multilinea).

Button - Es un botón con texto.

Radiobutton - Es un circulo al cual podemos hacerle clic y seleccionar una opción.

Checkbutton - Es un cuadrado que nos permite seleccionar opciones.

Menu -  Son los típicos botones que vemos en las ventanas en la parte superior
que despliegan opciones.

Dialogs - Ventanas emergentes que muestran información al usuario. Como alertas
o ventanas para elegir archivos, etc...

"""

# Importamos la biblioteca Tkinter
from tkinter import *

# Creamos la raiz o root de nuestra app
root = Tk()
# Anadimos un titulo a la ventana
root.title("Academia Coder")
# Anadimos un icono para Windows
root.iconbitmap("python_icon.ico")
# Decimos si puede redimensionarse o no con 0 o 1, true o false
root.resizable(1, 1)
# Definir el alto y ancho que queramos
root.geometry("600x300")
# Cambiar algunas opciones
root.config(bg="black")

# Vamos a hacer un frame hijo de la raiz
frame = Frame(root)

# Empaquetamos el frame dentro de la raiz y le damos su posicionamiento
frame.pack(
    side=RIGHT,
    anchor=S,
)

# Redimencionamos ocupando todo el espacio de la raiz
frame.pack(
    fill="both",
    expand=1
)
# Cambiamos el color del fondo de nuestro marco o frame
frame.config(bg="blue")

# Damos un tamano a nuestro frame
frame.config(width=600, height=300)

# Cambiar el cursor del raton, podemos darle un estilo al borde y un tamano
frame.config(cursor="pirate")
frame.config(relief="sunken")
frame.config(bd=25)

# Podemos asignar algunas configuraciones a la raiz a la vez
root.config(
    bg="black",
    cursor="hand2",
    relief="sunken",
    bd=10
)


# Ejecutamos el metodo del bucle infinito
root.mainloop()  # siempre va al final de nuestro programa
