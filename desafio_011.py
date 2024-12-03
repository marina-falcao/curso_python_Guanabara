altura = float(input("Digite a altura da parede em m: "))
largura = float(input("Digite a largura da parede em m: "))
area = altura * largura  
print("Sua parede tem {} m2.".format(area))   
tinta = area / 2
print("Você precisará de {} litros de tinta.".format(tinta))