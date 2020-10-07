# SENTENCIAS BREAK Y CONTINUE
# Las sentencias break y continue nos permiten manejar el flujo
# de la informacion en un bucle, para cortarla o prevenirla.

dias = [
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sabado",
    "domingo"
]

# FOR anidado
"""
for indice in range(5):
    for indice2 in range(3):
        print(indice, indice2)
"""
""" 
for indice in range(10):
    if indice == 4:
        break
    print(indice)
"""

for dias in dias:
    if dias == "sabado":
        break
    print(dias)
