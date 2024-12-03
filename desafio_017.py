import math
cateto_oposto = float(input("Digite a medida do cateto oposto: "))
cateto_adjacente = float(input("Digite a medida do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print("A hipotenusa do triângulo é {}.".format(hipotenusa))

