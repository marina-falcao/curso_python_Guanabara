num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))

if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else: 
    print("Não existe valor maior, os números são iguais.")