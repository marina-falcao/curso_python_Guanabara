lista_peso = []

for n in range(0, 5):
    peso = int(input("Digite seu peso em kg: "))
    lista_peso.append(peso)

lista_peso.sort()

print("O menor peso informado é {} kg e o maior é {} kg.".format(lista_peso[0], lista_peso[-1]))

#outra forma de fazer:
'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {}a pessoa: ".format(p)))
    if p == 1: (SE FOR A PRIMEIRA PESSOA, O PESO REGISTRADO VAI TANTO PRO MARCADOR DE MAIOR QUANTO DE MENOR, POIS NÃO HÁ BASE PRA COMPARAÇÃO.)
        maior = peso
        menor = peso  
    else:
        if peso > maior:  (SE O PESO REGISTRADO FOR MAIS ALTO QUE A VARIÁVEL MAIOR, ELA PASSA A TER O VALOR DESSE PESO. IDEM PRA MENOR. )
            maior = peso
        if peso < menor:
            menor = peso

print("O maior peso lido foi de {}kg.".format(maior))
print("O menor peso lido foi de {}kg.".format(menor))

'''