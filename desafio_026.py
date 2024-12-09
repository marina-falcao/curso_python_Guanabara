frase = input("Digite uma frase: ").strip()
frase = frase.upper()

#quantas vezes aparece letra A
print("A letra A aparece", frase.count('A'), "vezes.")

#posição do primeiro A
print("O primeiro A está na posição", frase.find("A")+1)


#posição do último A
print("O último A está na posição", frase.rfind("A")+1)
