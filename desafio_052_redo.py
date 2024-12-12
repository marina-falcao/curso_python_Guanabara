num = int(input("Digite um número inteiro: "))

for n in range(2, 10):
    if num % n == 0:
        print("O número {} não é primo.".format(num))
        break
    else: 
        print("O número {} é primo.".format(num))

#INCOMPLETO