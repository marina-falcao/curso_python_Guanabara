salario = float(input("Qual o seu salário atual? "))
aumento = 0.15
valor_aumento = salario * aumento
novo_salario = salario + valor_aumento
print("Você recebeu R$ {:.2f} de aumento! Seu novo salário é R$ {:.2f}.".format(valor_aumento, novo_salario))