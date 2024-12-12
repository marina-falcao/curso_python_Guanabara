import datetime
maior = 0
menor = 0

data_atual = datetime.date.today()
ano_atual = data_atual.year

for n in range(0, 7):
    ano = int(input("Digite o ano de nascimento com 4 dígitos: "))
    if ano_atual - ano >= 21:
        maior += 1
    else:
        menor += 1

print("Há {} pessoas maiores de idade e {} menores.".format(maior, menor))
