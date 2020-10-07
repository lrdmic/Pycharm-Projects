# Los operadores son signos, simbolos o palabras que el interprete utiliza para hacer una operacion epecifica

# OPERADORES MATEMATICOS
"""
+ Operador de Suma
- Operador de Resta
- Operador de Negativo
* Operador de Multiplicacion
** Operador de Exponente
/ Operador de Division
// Operador de Division Entera
% Operador de Modulo o Resto
"""

# Reglas de precedencia de las operaciones matematicas
"""
En orden de precedencia
1. Parentesis
2. Exponente
3. Multiplicacion
4. Division
5. Suma
6. Resta
"""

numero1 = 10
numero2 = 5

# Realizar todas las operaciones aritmeticas utilizando estos 2 numeros!

resultado = 12 * 5 + 2 / 3 ** 2
# print(resultado)

resultado1 = (12 * 5) + (2 / (3 ** 2))
# print(resultado1)

resultado2 = (12 * 5) + (2 / 3) ** 2
# print(resultado2)


# OPERADORES PARA CADENAS

"""
+ Operador de Concatenacion
* Operador de Repeticion
"""
cadena1 = "Hola "
cadena2 = "Mundo"

cadena_unidas = cadena1 + cadena2

# print(cadena_unidas)

cadenas_repetidas = cadena1 * 3

# print(cadenas_repetidas)

# Operadores de relacion
# Los Operadores de relacion evaluan si 2 valores u objetos cumplen con una condicion
# El resultado de dicha evaluacion es un objeto booleano (bool)

"""
== ¿Igual A?
!= ¿Distinto de?
> ¿Mayor que?
< ¿Menor que?
>= ¿Mayor o igual que?
<= ¿Menor o igual que?
"""

numero1 = 10
numero2 = 5
numero3 = 10.0
numero4 = -10
numero5 = 5
numero_cadena = "10"

igual = numero1 == numero2
# print(igual)
igual = numero2 == numero5
# print(igual)
igual = numero1 == numero4
# print(igual)

# Hacer todas las comprobaciones con los distintos numeros y su respectivo print

distinto = numero1 != numero2
# Hacer todas las comprobaciones con los distintos numeros y su respectivo print

mayor_que = numero1 > numero2
# Hacer todas las comprobaciones con los distintos numeros y su respectivo print

menor_que = numero1 < numero4
# Hacer todas las comprobaciones con los distintos numeros y su respectivo print

mayor_igual = numero1 >= numero3
# Hacer todas las comprobaciones con los distintos numeros y su respectivo print

menor_igual = numero1 <= numero5
# Hacer todas las comprobaciones con los distintos numeros y su respectivo print

# OPERADORES DE ASIGNACION
# Los operadores de asignacion se utilizan para asignar un valor a una variable
"""
= Asignacion simple -> x = y
+= Asignacion suma -> x += y equivale a x = x + y
-= Asignacion resta -> x -= y equivale a x = x - y
*= Asignacion multiplicacion -> x *= y equivale a x = x * y
**= Asignacion exponente -> x **= y equivale a x = x ** y
/= Asignacion division -> x /= y equivale a x = x / y
//= Asignacion division entera -> x //= y equivale a x = x // y
%= Asignacion division entera -> x %= y equivale a x = x % y
"""

numero1 = 1
numero2 = 2
# Podemos asignar varios valores en una misma linea
numero3, numero4, numero5 = 3, 4, 5

# Asignacion suma
numero1 = numero1 + numero2
# print(numero1)
# numero1 = 1
numero1 += numero2
# print(numero1)

# Asignacion resta
numero1 = 1
numero1 = numero1 - numero2
# print(numero1)
numero1 = 1
numero1 -= numero2
# print(numero1)

# Asignacion multiplicacion
numero1 = 1
numero1 = numero1 * numero2
# print(numero1)
numero1 = 1
numero1 *= numero2
# print(numero1)

# Asignacion exponente
numero1 = 1
numero1 = numero1 ** numero2
# print(numero1)

numero1 **= numero2
# print(numero1)

# Asignacion division
numero1 = numero1 / numero2
# print(numero1)
numero1 = 1
numero1 /= numero2
# print(numero1)

# Asignacion division entera
numero1 = 1
numero1 = numero1 // numero2
# print(numero1)
numero1 = 1
numero1 //= numero2
# print(numero1)

# Asignacion division entera
numero1 = 1
numero1 = numero1 % numero2
# print(numero1)
numero1 = 1
numero1 %= numero2
# print(numero1)

# a,b = b, a + b
a = 1
b = 2
# print(a, "valor de A")
a = b
# print(a, "valor de A luego de asignarle B")
b = a + b
# print(a, b)


# OPERADORES LOGICOS Y DE REFERENCIA

# OPERADORES LOGICOS
# Los operadores logicos nos permiten comprobar si se cumplen justamente comparaciones logicas
#  normalmente se comparan valores booleanos pero Python permite operaciones logicas con otros tipos de datos

"""
or -> a or b -> Se cumplen a o b? -> Solo es falso si todos los valores son falsos!
and -> a and b -> Se cumplen a y b? -> solo es verdadero si todos los valores son verdaderos!
not -> not x -> contrario de x
"""
verdadero = True
falso = False

# print("Comparador OR:")
# print(verdadero or falso, "\n")
# print("Comparador AND:")
# print(verdadero and falso, "\n")
# print("Comparador NOT:")
# print(not verdadero, "\n")
# print("Comparador NOT:")
# print(not falso, "\n")

# OPERADORES DE PERTENENCIA
# Los operadores de pertenencia evaluan si un objeto se encuentra dentro de otro
"""
in - Se encuentra en
not in - No se encuentra en
"""

cadena = "AcademiaCoder"

# print('Z' in cadena)
# print('Z' not in cadena)

# OPERADORES DE IDENTIDAD
# Los operadores de identidad nos permiten comprobar si un objeto es igual a otro objeto

"""
is -
is not - 
"""

a = 10
b = 10

print(type(a) is int)
print(a is not complex)

