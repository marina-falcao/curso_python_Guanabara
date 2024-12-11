
preco = float(input("Digite o preço do produto: "))
condicao_pagto = int(input("Escolha a forma de pagamento: 1 - à vista com dinheiro ou cheque / 2 - à vista no cartão / 3 - até 2x no cartão / 4 - 3x ou mais no cartão: "))
a_vista_din_cheque = preco - (preco * 0.10)
a_vista_cartao = preco - (preco * 0.05)
ate_duas_cartao = preco
tres_ou_mais_cartao = preco + (preco * 0.20)

if condicao_pagto == 1:
    print("Você ganhou 10% de desconto. O produto será R$ {:.2f}.".format(a_vista_din_cheque))
elif condicao_pagto == 2:
    print("Você ganhou 5% de desconto. O produto será R$ {:.2f}.".format(a_vista_cartao))
elif condicao_pagto == 3:
    print("Você não tem desconto. O produto será R$ {:.2f}.".format(ate_duas_cartao))
elif condicao_pagto == 4:
    print("Você pagrá juros de 20%. O produto será R$ {:.2f}.".format(tres_ou_mais_cartao))
else:
    print("Opção inválida. Tente novamente.")
