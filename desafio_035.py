r1 = int(input("Digite o comprimento da reta 1: "))
r2 = int(input("Digite o comprimento da reta 2: "))
r3 = int(input("Digite o comprimento da reta 3: "))

retas = [r1, r2, r3]
retas.sort()

print(retas)


soma = retas[0] + retas[1]
print(soma)

if soma > retas[2]:
    print("A soma das retas menores é {}, maior que {}, logo, elas podem formar um triângulo.".format(soma, retas[2]))
else:
    print("A soma das retas menores é {}, menor que / igual a {}, logo, elas não podem formar um triângulo.".format(soma, retas[2]))

#outra forma de fazer:
'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar triângulo.")
else: 
    print("Os segmentos não podem formar triângulo.")
'''