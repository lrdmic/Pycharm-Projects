# MEJORANDO NUESTRA CALCULADORA
# CALCULADORA 2.0

operadores = "+, -, *, /"

while True:
    num1 = float(input("Ingresa un numero: "))
    op = input("Ingresa un operador: ")
    num2 = float(input("Ingresa otro numero: "))
    try:
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
        elif op not in operadores:
            print("Operador incorrecto")
    except ZeroDivisionError as err:
        print(err)
    except ValueError:
        print("Entrada invalida, debe ser un numero")
    finally:
        print("\nIngresa:\n(1) para continuar")
        print("(2) para finalizar")
        choice = input(">>")
        if choice == "2":
            print("Nos vemos luego\n")
            break
        else:
            print("Sigamos calculando!")
