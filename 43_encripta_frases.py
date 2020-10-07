# ENCRIPTADOR DE FRASES

# "Hola AcademiaCoder", Como estan hoy?
# Caracter elegido xX
# "Hxlx XcxdxmxxCxdxr, Cxmx xstxn hxy?"

# Mi frase:
# Mi nombre es Sterling, quiero aprender Python desde cero en AcademiaCoder
# Mx nxmbrx xs Stxrlxng, qxxxrx xprxndxr Pythxn dxsdx cxrx xn XcxdxmxxCxdxr

# Variables para modificar el programa
print("Ingresa el caracter a utilizar para encriptar: ")
caracter_elegido = input(">>")


def encriptar(frase, caracter):
    encriptada = ""
    for letra in frase:
        if letra.lower() in "aeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + caracter.upper()
            else:
                encriptada = encriptada + caracter
        else:
            encriptada = encriptada + letra
    return encriptada

# Funcion anidada donde ingresamos una frase y la guarda en encriptar


while True:
    print(encriptar(input("Ingresa una frase:\n>"), caracter_elegido))

    print("\nIngresa:\n(1) para encriptar otra frase")
    print("(2) para finalizar")
    choice = input(">")
    if choice == "2":
        print("Nos vemos luego!!")
        break
    if choice == "1":
        print("----0----\n")

# TAREA PARA LOS ESTUDIANTES
# 1 - Hacer que el usuario pueda decidir que letra utilizar para encriptar (done)
# 2 - Jugar con el codigo y hacer mas interesante el encriptador (maybe done)
# Por ejemplo: hacer algo para identificar que se encriptaron caracteres con acento.
