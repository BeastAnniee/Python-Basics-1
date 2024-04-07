def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre 0"


def potencia(a, b):
    return a ** b


def div_entera(a, b):
    return a // b


def modulo(a, b):
    return a % b


operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: potencia,
    6: div_entera,
    7: modulo,
}
ent = float(input("1 - Entrar a la calculadora \n2 - Salir \n---> "))
while ent == 1:
    print(""" ------- CALCULADORA BASICA ------- 
    OPERACIONES DISPONIBLES:
    1. SUMA
    2. RESTA
    3. MULTIPLICACIÓN 
    4. DIVISIÓN
    5. POTENCIA
    6. DIVISION ENTERA
    7. MÓDULO
 ----------------------------------""")
    op = float(input("Ingrese la operación deseada: "))
    op = int(op)
    while op not in operaciones:
        print("Seleccione una opción valida")
        op = float(input("Ingrese la operación deseada: "))
    print("----------------------------------")
    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))
    print("----------------------------------")
    print("RESULTADO: ", operaciones[op](x, y))
    print("----------------------------------")
    ent = float(input("1 - Seguir calculando \n2 - Salir \n---> "))
