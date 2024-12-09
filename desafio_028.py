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

#outra forma de fazer:

'''
from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input("Em que número eu pensei?"))
print("processando...")
sleep(3)
if jogador = computador:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("Ganhei! Eu pensei no número {}, e não no {}.".format(computador, jogador))
'''