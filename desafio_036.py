valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Em quantos anos você quer pagar a casa? ")) 
meses = anos * 12
#print(meses)
porcentagem = salario * 0.3
#print(porcentagem)
prestacao = valor_casa / meses
#print(prestacao)

if prestacao > porcentagem:
    print("Seu empréstimo foi negado, pois a parcela excede 30% do seu salário. Favor aumentar o número de parcelas.")
else:
    print("Parabéns, seu empréstimo foi aprovado. Você pagará {} parcelas de R$ {}.".format(anos, prestacao))
