num = int(input("Digite um número inteiro: "))
opcao = int(input("Digite 1 para converter o número para binário, 2 para octal e 3 para hexadecimal: "))

if opcao == 1:
    print("O número escolhido corresponde a:", bin(num))
elif opcao == 2:
    print("O número escolhido corresponde a:", oct(num))
elif opcao == 3:
    print("O número escolhido corresponde a:", hex(num))
else:
    print("Opção inválida, tente novamente.")


