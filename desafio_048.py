s = 0
cont = 0

for n in range(0, 501, 3):
    if n % 2 != 0:
        print(n)
        s += n
        cont += 1


print("Há {} números ímpares múltiplos de 3 até 500, e sua soma é {}.".format(cont, s))
