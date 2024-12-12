
preco = float(input("Digite o preço do produto: "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista com dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

condicao_pagto = int(input("Digite a opção: "))

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
    parcelas = int(input("Quantas parcelas? "))
    print("Você pagará juros de 20%. O produto será R$ {:.2f} dividido em {} vezes.".format(tres_ou_mais_cartao, parcelas))
else:
    print("Opção inválida. Tente novamente.")
