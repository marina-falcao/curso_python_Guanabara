import datetime

ano_nasc = int(input("Digite seu ano de nascimento: "))
data_atual = datetime.date.today()
ano_atual = data_atual.year
idade = ano_atual - ano_nasc

if idade <= 9:
    print("O atleta tem {} anos e está na categoria mirim.".format(idade))
elif idade > 9 and idade <= 14:
    print("O atleta tem {} anos e está na categoria infantil.".format(idade))
elif idade > 14 and idade <= 19:
    print("O atleta tem {} anos e está na categoria júnior.".format(idade))
elif idade == 20:
    print("O atleta tem {} anos e está na categoria sênior.".format(idade))
else:
    print("O atleta tem {} anos e está na categoria master.".format(idade))