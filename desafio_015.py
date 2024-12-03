km = float(input("Digite a quantidade de km rodados pelo carro: "))
dias = float(input("Digite o número de dias do aluguel: "))
preco_km = 0.15 * km
preco_dias = 60 * dias
valor_final_aluguel = preco_km + preco_dias

print("O valor do aluguel pelos km rodados é de R$ {:.2f}. O valor de aluguel por {:.0f} dias é de R$ {:.2f}. O valor total a ser pago é de R$ {:.2f}.".format(preco_km, dias, preco_dias, valor_final_aluguel))