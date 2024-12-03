altura = float(input("Digite a altura da parede em m: "))
largura = float(input("Digite a largura da parede em m: "))
area = altura * largura  
print("Sua parede tem {:.2f} m2.".format(area))   
tinta = area / 2
print("Você precisará de {:.2f} litros de tinta.".format(tinta))