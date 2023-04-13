precoInicial = float(input("Qual é o preço do produto?"))
desconto = 0.05 * precoInicial
precoFinal = precoInicial - desconto
print("O produto que custava R$", precoInicial, "na promoção com desconto de 5% vai custar R$", round(precoFinal, 2))
