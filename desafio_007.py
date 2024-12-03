nome = input("Digite o nome do aluno: ")
ativ1 = float(input("Digite a nota do aluno na atividade 1: "))
ativ2 = float(input("Digite a nota do aluno na atividade 2: "))
media = (ativ1 + ativ2) / 2
print("{} tirou {} na atividade 1 e {} na atividade 2. Sua média é {}.".format(nome, ativ1, ativ2, media))