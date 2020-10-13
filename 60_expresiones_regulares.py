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

cadena = "Hola estudiantes de AcademiaCoder. En AcademiaCoder los estudiantes " \
         "aprenderan programacion."

# Ejemplo de cadena de multiples lineas
cadena2 = """Hola estudiantes de AcademiaCoder. 
En AcademiaCoder los estudiantes parenderan programacion,
Recuerden que nos centramos en el desarrollo web"""

a_buscar = "estudiantes"

buscado = re.search(a_buscar, cadena)
# print(re.search(a_buscar, cadena))

# if re.search(a_buscar, cadena):
#   print("Se ha encontrado")
# else:
#    print("No se ha encontrado")

# Comentado por la clase 61 de AcademiaCoder
""" 
print(buscado)
print(buscado.start())
print(buscado.end())
print(buscado.end()-1)
print(buscado.span())
print(buscado.group())
print(a_buscar)
"""
# Clase 2 - re.findall, re.split, re.sub
# En esta clase aprenderemos a utiizar estos metodos de la libreria re

print(re.findall(a_buscar, cadena))  # Nos imprime un resultado con las
# coincidencias encontradas (los match)

re_findall = re.findall(a_buscar, cadena)
print(re_findall)  # Esta es otra forma de hacer lo mismo de arriba
print(len(re_findall))  # Con esto podemos saber cuantas veces ha encontrado una cadena

re_split = re.split("\s", cadena)  # Separar cadenas por el caracter indicado, en este caso es el espacio en blaco
print(re_split)

re_sub = re.sub(a_buscar, "desarrolladores", cadena)  # Va a buscar la palabra indicada en a_buscar
# y la sustituira por desarrolladores y lo va a guardar en cadena.
print(re_sub)

# Clase 3 - Anclas y Metacaracteres (Sintaxis de Regex)
# ^, $, []
# ^ que comiencen con
# $ que terminen con
# [] encuentra lo que este dentro de
lista = [
    "Marcos - Python",
    "Carlos - Javascript",
    "Ana - Javascript",
    "Marcos - PHP",
    "Natalia - Vue",
    "Violeta - Python",
    "Ana - Vue",
    "Carla - PHP",
    "Mario - Programacion",
    "Benicio - Programación"
]

for linea in lista:
    if re.findall('^Marcos', linea):
        print(linea)
    if re.findall('Programaci[oó]n', linea):  # Nos encuentra un conjunto de caracteres que se encuentren dentro
        print(linea)

# Clase 4 - Rangos, Rango Negado, Clases Predefinidas, Cuantificadores y Otros Metacaracteres

cadena1 = "abcdef ghi" \
          "0123456789-"

# Rangos []

# [a-d] esto significaria que buscamos cualquier letra comprendida entre a y d, es decir, "abcd"


# [0-7] esto significaria que buscamos cualquier numero comprendido entre 0 y 7, es decir, "01234567"

print(re.findall("[a-d2-5]", cadena1))

# Rango Negado ^

print(re.findall("[^a-d2-5]", cadena1))

# Clases Predefinidas

# \d corresponde a [0-9]
# \D corresponde a lo que no es un digito decimal
# \w todas las letras minus., mayus., numeros y guiones bajos
# \W ni numeros, ni letras.
# \s corresponde a espacios en blanco (espacio, tabulaicones, nuevas lineas...)

print(re.findall("[\w]", cadena1))

"""
CUANTIFICADORES

Son caracteres que multiplican el patron que les precede.
Mientras que con las clases de caracteres podemos buscar un digito, o una letra;
con los cuantificadores podemos buscar cero o mas letras, al menos 7 digitos, 
o entre tres y cinco letras mayusculas. Los cuantificadores son:
 
?: coincide con cero o una ocurrencia del patron. DIcho de otra forma, hace
que el patron sea opcional.
+: coincide con una o mas ocurrencias del patron.
*: coincide con cero o mas ocurrencias del patron.
{x}: coincide con exactamente x ocurrencias del patron.
{x, y}: coincide con al menos x y no mas de y ocurrencias. Si se omite x,
el minimo es cero, y si se omite y, no hay maximo. Esto permite especificar
a los otros como casos particulares: ? es {0,1}, + es {1,} y * es {,} o {0,}.
Ejemplos:

.* : cualquier cadena, de cualquier largo (incluyendo una cadena vacia)
[a-z]{3,6}: entre 3 y 6 letras minusculas
\d{4,}: al menos 4 digitos
.*[hH]ola!?: una cadena cualquiera, seguida de hola o Hola, y terminando (o no) con un !
"Mi nombre es Sterling, hola!"
"Mi nombre es Sterling, hola"

Otros Metacaracteres
Existen otros metacaracteres en el lenguaje de las expresiones regulares:

?: Ademas de servir como cuantificador, puede modificar el comportamiento de otro.
De forma predeterminada, un cuantificador coincide con la mayor cadena posible.
Cuando se le coloca un ?, se indica que se debe coincidir con la menor cadena posible.
Esto es: dada la cadena bbbb, b+ coincide con la cadena entera, mientras que 
b+? coincide solamente con b.
Es decir, la menor cadena que cumple el patron.

(): agrupan patrones. Sirven para que aquel pedazo de la cadena que coincida
con el patron sea capturado; o para delimitar el alcance de un cuantificador.
Ejemplo: ab+ coinicide con ab, abb, abbbb, ...,
mientras que (ab)+ coincide con ab, abab, ababab...
| : permite definir opciones para el patron: perro|gato coincide con perro y con gato. 
"""
