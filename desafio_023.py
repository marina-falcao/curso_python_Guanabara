num = input("Digite um numero de 0 a 9999: ")

print("unidade:", num[-1])
print("dezena:", num[-2])
print("centena:", num[1])
print("milhar:", num[0])

#outra forma de fazer:
#num = int(input("Digite um numero de 0 a 9999: "))
#unidade = num // 1 % 10
#dezena = num // 10 % 10
#centena = num // 100 % 10
#milhar = num // 1000 % 10

#print("unidade: {}".format(unidade))
#print("dezena: {}".format(dezena))
#print("centena: {}".format(centena))
#print("milhar: {}".format(milhar))