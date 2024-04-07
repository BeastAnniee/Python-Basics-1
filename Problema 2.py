# Desarrollar un programa que solicite tres números al usuario,
# posteriormente el programa debe indicar cual de los tres números es
# el mayor.
ls = []
i = 0
for i in range(3):
    num = float(input("Ingrese el numero {}: ".format(i+1)))
    ls.append(num)
ls_sorted = sorted(ls, reverse=True)
print("El número más alto es: ", ls_sorted[0])
