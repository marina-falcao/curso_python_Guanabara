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
    if retas[0] == retas[1] == retas[2]:
        print("Todos os lados são iguais, o triângulo será equilátero.")
    elif retas[0] == retas[1] or retas[0] == retas[2] or retas[1] == retas[2]:
        print("Duas retas são iguais. O triângulo será isóceles")
    elif retas[0] != retas[1] != retas[2]:
        print("Todos os lados são diferentes, o triângulo será escaleno.")
else:
    print("A soma das retas menores é {}, menor que / igual a {}, logo, elas não podem formar um triângulo.".format(soma, retas[2]))