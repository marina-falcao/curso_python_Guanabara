import random

print('-' *20, "JOKENPO", '-' *20)
print('''Escolha a sua opção:
      [ 1 ] Pedra
      [ 2 ] Papel
      [ 3 ] Tesoura
''')
opcao = int(input("Digite sua escolha: "))

PC = [1, 2, 3]

escolhido = random.choice(PC)
print(escolhido)

if opcao == 1 and escolhido == 1:
    print("Ambos escolhemos pedra - empate.")
elif opcao == 1 and escolhido == 2:
    print("Ganhei! Papel enrola a pedra!")
elif opcao == 1 and escolhido == 3:
    print("Você ganhou! Pedra quebra tesoura!")
elif opcao == 2 and escolhido == 1:
    print("Você ganhou! Papel enrola a pedra!")
elif opcao == 2 and escolhido == 2:
    print("Ambos escolhemos papel - empate")
elif opcao == 2 and escolhido == 3:
    print("Ganhei! Tesoura corta papel.")
elif opcao == 3 and escolhido == 1:
    print("Ganhei! Pedra quebra tesoura!")
elif opcao == 3 and escolhido == 2:
    print("Você ganhou! Tesoura corta papel!")
elif opcao == 3 and escolhido == 3:
    print("Ambos escolhemos tesoura - empate")
else:
    print("Opção inválida. Tente novamente. ")