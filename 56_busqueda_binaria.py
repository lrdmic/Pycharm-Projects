# BUSQUEDA BINARIA

lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]
lista.sort()
print(lista)

# 1ro. buscar el punto medio
# 2do. comprobar si el punto medio es el valor buscado
# 3ro. si el numero es menor al valor que buscamos aumentamos inicio 1 sobre el puntero
# 4to. si el numero es menor al valor que buscamos disminuimos el final 1 bajo el puntero
# 5to. si inicio mayor o igual que final entonces el numero el valor no se encuentra en la lista


def busqueda_binaria(valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        puntero = (inicio + fin) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            fin = puntero - 1
    return None


def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El numero {valor} no fue encuentrado"
    else:
        return f"El numero {valor} se encuentra en la posicion {res_busqueda}"


# print(buscar_valor(15))  # Aqui le pasamos el valor que queremos que busque

while True:
    val = int(input("Ingresa el numero a buscar: "))
    print(buscar_valor(val))
    choice = input("Quieres continuar buscando?\n (1) Para seguir.\n (2) Para salir.\n >>")
    if choice == '1':
        print("Continuamos...")
    else:
        print("Gracias, nos vemos luego")
        break


# TAREA PARA ESTUDIANTE, Realizar las modificaciones al codigo
# para poder ingresar los valores directamente desde consola
# y agregar un ciclo infinito realizar todas las busquedas que queramos
# y poder terminar el ciclo
