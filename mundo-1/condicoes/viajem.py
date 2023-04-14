distancia = int(input("Qual a distância da viajem em KM? "))
print('Valor da passagem: ')
print((distancia * 0.50) if (distancia <= 200) else (distancia * 0.45))
