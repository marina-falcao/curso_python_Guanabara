distancia = int(input("Digite a distância da sua viagem: "))

if distancia <= 200:
    total = distancia * 0.50
    print("O valor da sua passagem é R$ {:.2f}.".format(total))
else: 
    total = distancia * 0.45
    print("O valor da sua passagem é R$ {:.2f}.".format(total))