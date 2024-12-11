import datetime

ano_nasc = int(input("Digite seu ano de nascimento: "))
data_atual = datetime.date.today()
ano_atual = data_atual.year
idade = ano_atual - ano_nasc

if idade < 18:
    print("Ainda não é o momento de se alistar. Faltam {} anos.".format(18 - idade))
elif idade == 18:
    print("Chegou a hora de se alistar. Compareça ao local mais próximo.")
else:
    print("Você está {} anos atrasado para se alistar.".format(idade - 18))