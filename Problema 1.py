# 1. Desarrollar un programa que solicite un número entero desde teclado
# y determinar si dicho número es par o impar.
x = float(input("Ingrese un número entero:"))
while x % 1 != 0:
    print("El número no es entero")
    x = float(input("Ingrese un número entero"))
if x % 2 == 0:
    print("El número es par")
elif x == 0:
    print("El número es par")
else:
    print("El número no es par")
