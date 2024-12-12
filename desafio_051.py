prim_num = int(input("Digite o primeiro número da P.A.: "))
razao = int(input("Digite a razão da P.A.: "))

for p in range(1, 11):
    x = prim_num + (p - 1)* razao
    print("O termo {} da P.A. é {}.".format(p, x))

#outra forma de fazer:

'''
primeiro = int(input("Digite o primeiro número da P.A.: "))
razao = int(input("Digite a razão da P.A.: "))
decimo = primeiro + (10 - 1) * razao

for c in range (primeiro, decimo + razao, razao):
    print("{}".format(c))
    
'''