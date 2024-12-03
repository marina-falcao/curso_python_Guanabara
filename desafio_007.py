nome = input("Digite o nome do aluno: ")
ativ1 = float(input("Digite a nota do aluno na atividade 1: "))
ativ2 = float(input("Digite a nota do aluno na atividade 2: "))
media = (ativ1 + ativ2) / 2
print("{} tirou {:.1f} na atividade 1 e {:.1f} na atividade 2. Sua média é {:.1f}.".format(nome, ativ1, ativ2, media))