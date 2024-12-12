num = int(input("Digite um número: "))
cont = 0

for n in range(0, 11):
    result = num * cont
    print("{} * {} == {}".format(num, cont, result))
    cont += 1