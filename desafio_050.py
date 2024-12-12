s = 0
cont = 0
for n in range(0, 6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        s += num
        cont += 1

print("A soma dos {} valores pares informados na sequência é {}.".format(cont, s))