# MEJORANDO NUESTRA CALCULADORA
# CALCULADORA 2.0

num1 = float(input("Ingresa un numero: "))
op = input("Ingresa un operador: ")
num2 = float(input("Ingresa otro numero: "))

if op == "+":
    res = num1 + num2
    print("La suma es: " + str(res))
elif op == "-":
    res = num1 - num2
    print("la resta es: " + str(res))
elif op == "*":
    res = num1 * num2
    print("La multiplicacion es: " + str(res))
elif op == "/":
    res = num1 / num2
    print("La division es: " + str(res))
else:
    print("El operador es invalido!")
