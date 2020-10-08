# EXPRESIONES REGULARES o REGEX
# Modulo re

"""
Las expresiones regulares nos permiten trabajar con textos, mas especificamente para
realizar busquedas de texto a traves de metodos y utilizando una sintaxis propia
de la libreria de expresiones regulares que utilicemos en cada lenguaje. Normalmente
la sintaxis utilizada para los patrones de busqueda es compartida por la mayoria de
los lenguajes de programacion.

PODEMOS UTILIZAR EXPRESIONES PARA:
- Saber si existe una cadena de caracteres (palabra) dentro de un texto
- Conocer cuantas veces se encuentra una cadena de caracteres dentro de un texto
- Detectar si un texto se ajusta a un formato especifico por ejemplo un
correo electronico "texto" "@" "texto" "." "com" "." "do"
- etc...
"""

import re

# Clase 1 - re.search
# Este metodo nos buscara la primer coincidencia de una cadena de caracteres dentro de un texto
# devolvera un objeto si es localizado o None si no es encontrado.

cadena = "Hola estudianes de AcademiaCoder."

a_buscar = "estudiantes"

buscado = re.search(a_buscar, cadena)
# print(re.search(a_buscar, cadena))

# if re.search(a_buscar, cadena):
#   print("Se ha encontrado")
# else:
#    print("No se ha encontrado")

print(buscado)
print(buscado.start())
print(buscado.end())
print(buscado.end()-1)
print(buscado.span())
print(buscado.group())
