# LISTAS ANINADAS o LISTAS DE 2 DIMENSIONES
# Son listas que estan dentro de otras listas
#    0, 1, 2
grilla_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for fila in grilla_numeros:
    for col in fila:
        print(col)
