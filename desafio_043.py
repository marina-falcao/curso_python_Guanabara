peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Seu imc é {:.2f} e você está abaixo do peso".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu imc é {:.2f} e você está no peso ideal".format(imc))
elif imc >= 25 and imc < 30:
    print("Seu imc é {:.2f} e você está com sobrepeso".format(imc))
elif imc >= 30 and imc < 40:
    print("Seu imc é {:.2f} e você está com obesidade".format(imc))
else:
    print("Seu imc é {:.2f} e você está com obesidade mórbida".format(imc))