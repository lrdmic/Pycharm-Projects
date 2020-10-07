# DECLARACION IF (CONDICIONALES)
# Esta declaracion condicional nos permite condicionar una accion si una condicion se cumple
# u otra accion en caso de que no se cumpla


"""
EJEMPLO REAL:
Voy a salir,

SI hace calor,
    saldré en camiseta

SINO SI hace frio,
     saldré abrigado

SINO SI esta lloviendo,
     llevaré paraguas

SINO
     me quedaré en casa


si_es_hombre = True
eres_alto = True

print("Antes del If\n")

if si_es_hombre and eres_alto:
    print("Sorprendente eres un hombre y alto")
elif si_es_hombre and not eres_alto:
    print("Eres muy bajito")
elif not si_es_hombre and eres_alto:
    print("No eres un hombre, y tampoco eres alto")
else:
    print("Lamentablemente no eres un hombre y tampoco eres alto")

print("\nFuera del IF")
"""

# UTILIZANDO CONDICIONALES Y COMPARACIONES

"""
def mayor_edad(num):
    if num >= 18:
        return True
    else:
        return False


edad = input("Ingresa tu edad: ")

if mayor_edad(int(edad)):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""


def mayor_numero(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


numero = mayor_numero(99, 556, 300)
print(numero)
