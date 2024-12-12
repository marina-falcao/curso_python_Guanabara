nome = ""
genero = []
idade = []
mais_velho = 0
mulheres_menos_20_anos = 0

for n in range(0, 4):
    name = str(input("Qual o seu nome? "))
    gen = str(input("Escolha a opção que melhor te define: M / F / Outro "))
    gen = gen.upper()
    genero.append(gen)
    age = int((input("Qual a sua idade? ")))
    idade.append(age)

    if gen == "F" and age < 20:
        mulheres_menos_20_anos += 1
        (print(mulheres_menos_20_anos))

    if gen == "M" and age > mais_velho:
        mais_velho = age
        print(mais_velho)
        nome = name
        print(name)


idade_media = (idade[0] + idade[1] + idade[2] + idade[3]) / 4
print("A idade média do grupo é {}.".format(idade_media))
print("Há {} mulheres com menos de 20 anos no grupo.".format(mulheres_menos_20_anos))
print("O homem mais velho se chama {} e tem {} anos.".format(nome, mais_velho))

#outra forma de fazer:

'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0

for p in range(1, 5):
    print("--------{}a PESSOA --------".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo: str(input("Sexo [M/F/Outro]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos.".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totmulher20))

'''