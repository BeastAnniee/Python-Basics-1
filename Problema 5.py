def cmp(a):
    while a not in [0, 1]:
        print("Ingrese una opcion valida")
        a = int(input("Estado del interruptor {}: ".format(i + 1)))
    return a


print("----- Estado de los interruptores -----\nABIERTO = 1 \nCERRADO = 0")
print("---------------------------------------")
stt = []
for i in range(3):
    num = int(input("Estado del interruptor {}: ".format(i + 1)))
    num = cmp(num)
    stt.append(num)
print("---------------------------------------")
if sum(stt) >= 2:
    print("El equipo funcionara")
else:
    print("El equipo no funcionara")