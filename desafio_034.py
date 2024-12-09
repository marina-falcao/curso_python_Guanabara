salario = float(input("Digite seu salário: "))

if salario > 1250:
    aumento = salario * 0.1
    novo_salario = salario + aumento
    print("Parabéns! Você ganhou um aumento de R$ {:.2f}. Seu novo salário é R$ {:.2f}".format(aumento, novo_salario))
else: 
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print("Parabéns! Você ganhou um aumento de R$ {:.2f}. Seu novo salário é R$ {:.2f}".format(aumento, novo_salario))