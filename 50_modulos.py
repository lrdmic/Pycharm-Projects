# import utilidades_extra as ue
import random
from docx import Document
from utilidades_extra import tirar_dado as td

# MODULOS
# ue - para llamar a un modulo que su nombre es muy largo (es como abreviarlo
# para utilizarlo).
# Tambien se pueden llamar importar funciones especificas dentro de un modulo
# se puede tambien darle un alias, en caso de que la funcion tenga un nombre
# muy largo.

# Un modulo es un archivo que podemos importar dentro de un archivo en el cual
# estamos trabajando y hacer uso de su contenido, como funciones y variables.

print(td(6))

print(random.randint(10, 15))

# PIP
# Gestor de paquetes, gestor de modulos o librerias creadas por terceros.
# para Windows es así sin usar source solo escribir la ruta en la consola. .\venv>Scripts\activate
document = Document()
