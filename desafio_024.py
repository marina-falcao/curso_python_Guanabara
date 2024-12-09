cidade = input("Digite uma cidade: ")
cidade = cidade.lower()
cidade_split = cidade.split()
print(cidade_split)
print("santo" in cidade_split[0])

#outra forma de fazer:
'''
cidade = input("Digite uma cidade: ").strip()
print(cidade[:5].upper() == "SANTO")
'''