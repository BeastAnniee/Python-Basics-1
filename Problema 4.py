def clave_1(a):
    if a == 1:
        return 6
    elif 2 <= a <= 6:
        return 14
    elif a >= 7:
        return 20


def clave_2(a):
    if a == 1:
        return 7
    elif 2 <= a <= 6:
        return 15
    elif a >= 7:
        return 22


def clave_3(a):
    if a == 1:
        return 10
    elif 2 <= a <= 6:
        return 20
    elif a >= 7:
        return 30


claves = {
    1: clave_1,
    2: clave_2,
    3: clave_3,
}

ent = float(input("1 - Entrar al programa \n2 - Salir \n---> "))
while ent not in [1, 2]:
    print("¡¡Ingrese una opcion valida!!")
    ent = float(input("1 - Entrar al programa \n2 - Salir \n---> "))
while ent == 1:
    print("----- CALCULO DE VACACIONES -----")
    name = input("Ingrese el nombre del empleado: ")
    clave = float(input("Ingrese la clave del departamento: "))
    clave = int(clave)
    while clave not in claves:
        print("¡¡Ingrese una opcion valida!!")
        clave = input("Ingrese la clave del empleado: ")
    antiguedad = float(input("Ingrese la antigüedad del empleado (en años): "))
    while antiguedad < 0:
        print("¡¡Ingrese una opcion valida!!")
        antiguedad = float(input("Ingrese la antigüedad del empleado (en años): "))
    print("-------------------------------")
    print("EMPLEADO: ", name)
    print("DIAS DE DESCANSO: ", claves[clave](antiguedad))
    print("-------------------------------")
    ent = float(input("1 - Seguir \n2 - Salir \n---> "))
    while ent not in [1, 2]:
        print("¡¡Ingrese una opcion valida!!")
        ent = float(input("1 - Seguir \n2 - Salir \n---> "))
