nome = input("Digite seu nome completo: ")

#maiusculas e minusculas
print(nome.upper())
print(nome.lower())

#caracteres totais do nome sem espaços
espaco = nome.count(' ')
total = len(nome)
nome_s_espaco = total - espaco
print("Seu nome tem {} letras.".format(nome_s_espaco))

#numero de letras do primeiro nome
prim_nome = nome.split()
print("Seu primeiro nome tem" , len(prim_nome[0]), "letras")
