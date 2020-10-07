# LISTAS
# Una lista es una coleccion de elementos, las listas estan ordenadas, y son mutables.

numeros = [5, 2, 23, 55, 1, 9, 6]
frutas = ["Manzanas", "Peras", "Uvas", "Naranjas", "Mandarinas", "Bananas", "Kiwi"]
print("LISTA ORIGINAL DE FRUTAS:")
print(frutas)
print()
# print(frutas[-1])
# print(frutas[-3])
# print(frutas[2:])

# FUNCIONES DE LAS LISTAS
# https://docs.python.org/3/library/array.html
# list, len, append, extend, insert, remove, clear, pop, index, count, sort, reverse, copy
# len -> sirve para averiguar el largo de una lista
print(len(frutas))

# append -> sirve para añadir un elemento a la lista
frutas.append("Piña")
print(frutas)

# extend -> sirve para agregar una lista a otra
lista2 = numeros + frutas
print(lista2)

numeros.extend(frutas)
print(numeros)

# insert -> sirve añadir un indice y mueve una posicion a la derecha los demas miembros de la lista
frutas.insert(2, "Aguacate")
print(frutas)

# remove -> sirve para eliminar un elemento de una lista
frutas.remove("Kiwi")
print(frutas)

# clear -> sirve para borrar todos los elementos de una lista
frutas.clear()
print(frutas)

# pop -> sirve para borrar el ultimo elemento de una lista
frutas.pop()
print(frutas)

# index -> sirve para localizar posicion/indice de un elemento dentro de una lista
print(frutas.index("Manzana"))

# count -> sirve para mostrar cuantas veces aparece un elemento dentro de una lista
print(frutas.count("Kiwi"))

# sort -> sirve para ordenar la lista
frutas.sort()
print(frutas)

numeros.sort()
print(numeros)

# reverse -> sirve para darle vuelta completamente al orden de una lista
numeros.reverse()
print(numeros)

# copy -> sirve para copiar exactamente con todos los atributos y opciones una lista
frutas2 = frutas.copy()
print(frutas2)

