# TRATANDO CON ERRORES EN PYTHON
# try...except...else...finally

try:
    num1 = int(input("Ingresa un numero: "))
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Entrada invalida, debe ser una entero")
else:
    print("No hubo ningun error")
finally:
    print("Se ejecuta siempre sin importar que pase")

# MEJORAR LA CALCULADORA 2.0 Y ANADIRLE:
# 1- TRATAMIENTO DE ERRORES POSIBLES. (done)
# 2- CICLO INFINITO. (done)
