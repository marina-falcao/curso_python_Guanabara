salario = float(input("Qual o seu salário atual? "))
aumento = 0.15
valor_aumento = salario * aumento
novo_salario = salario + valor_aumento
print("Você recebeu R$ {} de aumento! Seu novo salário é R$ {}.".format(valor_aumento, novo_salario))