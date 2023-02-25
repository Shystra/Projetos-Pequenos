Produto = float(input("How many is the product? R$  "))
Porcentagem_Desconto = float(input("How many is the rebeat? "))

Desconto = Produto - (Produto * Porcentagem_Desconto / 100)

print("O valor do produto com desconto é R$ {:.2f}".format(Desconto))
