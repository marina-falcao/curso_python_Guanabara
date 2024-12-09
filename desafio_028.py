import random
numeros = [0, 1, 2, 3, 4, 5]

num = random.choice(numeros)
print(num)

guess = int(input("Adivinhe o número escolhido pelo PC: "))


while num != guess:
    print("Você errou, tente novamente.")
    guess = int(input("Adivinhe o número escolhido pelo PC: "))

if num == guess:
    print("Parabéns! Você acertou!")

