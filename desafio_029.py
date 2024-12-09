velocidade = int(input("Digite a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você ultrapassou a velocidade máxima. Sua multa será de {:.2f} reais".format(multa))
else: 
    print("Você está dentro do limite de velocidade. Boa viagem!")
