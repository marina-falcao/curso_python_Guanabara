nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Sua média é {}. Você foi reprovado e precisará refazer o semestre.".format(media))
elif media >= 5 and media <= 6.9:
    print("Sua média é {}. Você está em recuperação. Tente fazer as provas novamente.".format(media))
else:
    print("Sua média é {}. Parabéns! Você foi aprovado.".format(media))

