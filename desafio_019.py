import random
aluno_1 = input("Digite o nome do aluno: ")
aluno_2 = input("Digite o nome do aluno: ")
aluno_3 = input("Digite o nome do aluno: ")
aluno_4 = input("Digite o nome do aluno: ")

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

escolhido = random.choice(alunos)
print(escolhido)

print("O aluno escolhido é:", escolhido)