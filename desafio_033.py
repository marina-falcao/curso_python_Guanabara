num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

numeros = [num1, num2, num3]
numeros.sort()

print(numeros)
print("O menor número digitado é {} e o maior número digitado é {}.".format(numeros[0], numeros[-1]))


#outra forma de fazer:
'''
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and  c > b:
    maior = c

print("O menor número digitado é {} e o maior número digitado é {}.".format(menor, maior))
'''