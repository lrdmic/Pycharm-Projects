# CALCULADORA BASICA - PROYECTO NRO 1
# Solicitar al usuario 2 numero y realizar la suma de ellos

# Declaramos las variables
# Utilizamos Input para que se guarde lo que el usuario ingresa
num1 = input("Ingresa un numero: ")
num2 = input("Ingresa otro numero: ")

# Realizamos la suma y guardamos el resultado
suma = float(num1) + float(num2)
resta = float(num1) - float(num2)
mult = float(num1) * float(num2)
div = float(num1) / float(num2)
pot = float(num1) ** float(num2)
modulo_resto = float(num1) % float(num2)

# Imprimimos el resultado y un mensaje de despedida
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicacion es:", mult)
print("La division es:", div)
print("La potencia es:", pot)
print("El modulo o resto es:", modulo_resto)
print("GRACIAS!")


# TAREA PARA EL ESTUDIANTE
# Agregar a la calculadora el resto de las operaicones aritmeticas disponibles en Python
# y mostrar en pantalla todos los resultados

