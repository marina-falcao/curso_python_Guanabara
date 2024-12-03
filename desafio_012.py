preco = float(input("Digite o preço do produto: "))
desconto = 0.05
valor_desconto = preco * desconto
preco_sale = preco - valor_desconto
print("Você economizou R$ {}. O valor final é R$ {}.".format(valor_desconto, preco_sale))