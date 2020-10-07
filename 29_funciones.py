# FUNCIONES
# Una funcion es un bloque de codigo que incluye instrucciones para realizar
# una tarea especifica.


def saludar(nombre, edad):
    print("Hola! " + nombre + " tienes " + edad + " años de edad")
    print("Adios!")


# saludar("Sterling", "28")

# FUNCIONES LAMBDA
# Son funciones anonimas que se ejecutan en una linea, es decir, solo pueden tener una expresion.

resultado = lambda numero: numero + 20

suma = lambda numero1, numero2: numero1 + numero2

# print(resultado(30))
# print(suma(30, 60))

# RETURN
# La declaracion Return nos permite recibir datos de una funcion


def multiplicar(num1, num2):
    return num1 * num2


res_multi = multiplicar(2, 21)
print(res_multi)
